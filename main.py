from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_main import Ui_MainWindow
from excel import export_excel
from requisicoes import request_cnpj
from database import Database
import html
import sys

CAMPOS = ('cnpj', 'nome_empresa', 'logradouro', 'numero', 'complemento',
          'bairro', 'municipio', 'uf', 'cep', 'telefone', 'email')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()   #atributo relacionado as alterações internas do sistema
        self.ui.setupUi(self)
        self.setWindowTitle("SysDev - Sistema de cadastro de empresas")
        appIcon = QIcon(u"./imgs/logo_sysdev_240px.png")
        self.setWindowIcon(appIcon)
        self.table = self.ui.Table
        self.database = Database('localhost', 3306, 'root', '')
        self.show_registers_from_database()

        #botões para alteração de páginas no tableWidget
        self.ui.btn_home.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_home))
        self.ui.btn_cadastrar.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_cadastrar))
        self.ui.btn_sobre.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_sobre))
        self.ui.btn_contatos.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_contatos))

        #botões para as alterações principais da tabela
        self.ui.btnAdicionar.clicked.connect(self.insert_row_from_qt)
        self.ui.btnExcluir.clicked.connect(self.delete_row)
        self.ui.btnExcel.clicked.connect(self.gerar_excel)
        self.ui.btnAlterar.clicked.connect(self.update_database)

        self.ui.tabWidget.currentChanged.connect(self.show_registers_from_database)

        self.ui.txt_cnpj.textChanged.connect(self.auto_complete)
        self.ui.txt_nome_empresa.textChanged.connect(self.alterar_nome_empresa)


    def alterar_nome_empresa(self):
        nome_escapado = html.escape(self.ui.txt_nome_empresa.text())
        texto_rico = f'<html><head/><body><p align="center"><span style=" font-size:16pt; font-weight:700;">{nome_escapado}</span></p></body></html>'
        self.ui.nomeEmpresa.setText(texto_rico)

    def auto_complete(self):
        cnpj = self.ui.txt_cnpj.text()
        new_cnpj = cnpj.replace(' ', '').replace('-', '').replace('.', '').replace('/', '')
        if len(new_cnpj) == 14:
            request = request_cnpj(new_cnpj)
            self.ui.txt_nome_empresa.setText(request['nome'])
            self.ui.txt_logradouro.setText(request['logradouro'])
            self.ui.txt_numero.setText(request['numero'])
            self.ui.txt_complemento.setText(request['complemento'])
            self.ui.txt_bairro.setText(request['bairro'])
            self.ui.txt_municipio.setText(request['municipio'])
            self.ui.txt_uf.setText(request['uf'])
            self.ui.txt_cep.setText(request['cep'])
            self.ui.txt_telefone.setText(request['telefone'])
            self.ui.txt_email.setText(request['email'])


    def insert_qt_rows(self, *valores):
        row_index = self.table.rowCount()
        self.table.insertRow(row_index)

        for column, valor in enumerate(valores):
            item = QTableWidgetItem(str(valor))
            item.setData(Qt.ItemDataRole.UserRole, str(valor))
            if column == 0:
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row_index, column, item)

    def insert_row_from_qt(self):
        entries = [
            self.ui.txt_cnpj.text().replace('-', '').replace(' ', '').replace('.', '').replace('/', ''),
            self.ui.txt_nome_empresa.text(),
            self.ui.txt_logradouro.text(),
            self.ui.txt_numero.text(),
            self.ui.txt_complemento.text(),
            self.ui.txt_bairro.text(),
            self.ui.txt_municipio.text(),
            self.ui.txt_uf.text(),
            self.ui.txt_cep.text().replace('-', '').replace(' ', '').replace('.', ''),
            self.ui.txt_telefone.text(),
            self.ui.txt_email.text()
        ]

        self.database.insert_empresa(*entries)
        self.insert_qt_rows(*entries)

    def show_registers_from_database(self):
        registers = self.database.select_empresa()
        self.table.setRowCount(0)
        for i in registers:
            self.insert_qt_rows(*i)

    def delete_row(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            return
        cnpj = self.table.item(selected_row, 0).data(Qt.ItemDataRole.UserRole)
        self.database.delete_empresa(cnpj)
        self.table.removeRow(selected_row)

    def update_database(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            return

        cnpj_original = self.table.item(selected_row, 0).data(Qt.ItemDataRole.UserRole)
        dados_alterados = {}

        for column, campo in enumerate(CAMPOS):
            if column == 0:
                continue
            item = self.table.item(selected_row, column)
            if item is None or item.text() == item.data(Qt.ItemDataRole.UserRole):
                continue
            dados_alterados[campo] = item.text()

        if not dados_alterados:
            return

        if self.database.update_empresa(dados_alterados, cnpj_original):
            for column in range(self.table.columnCount()):
                item = self.table.item(selected_row, column)
                if item is not None:
                    item.setData(Qt.ItemDataRole.UserRole, item.text())

    def gerar_excel(self):
        row_count = self.table.rowCount()
        column_count = self.table.columnCount()
        row_data = []
  
        row_data.append(CAMPOS)

        for row in range(row_count):
            register = []
            for column in range(column_count):
                item = self.table.item(row, column)
                
                if item is not None:
                    register.append(item.text())
                else:
                    register.append("") 
            row_data.append(register)  
        export_excel(row_data)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())