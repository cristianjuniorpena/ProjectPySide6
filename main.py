from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog)
from ui_main import Ui_MainWindow
from exportExcel import export_to_excel
from requestCNPJ import request_cnpj
from database import Database
from config import Settings
import html
import sys
from validate_docbr import CNPJ

FIELDS = ('cnpj', 'nome_empresa', 'logradouro', 'numero', 'complemento',
          'bairro', 'municipio', 'uf', 'cep', 'telefone', 'email')
VALIDATE_CNPJ = CNPJ()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()   #atributo relacionado as alterações internas do sistema
        self.ui.setupUi(self)
        self.setWindowTitle("SysDev - Sistema de cadastro de empresas")
        appIcon = QIcon(u"./imgs/logo_sysdev_240px.png")
        self.setWindowIcon(appIcon)
        self.table = self.ui.Table
        self.settings = Settings.get_environment_variables_from_env()
        self._connect_alert = False
        self.database = Database(
            self.settings.db_host,
            self.settings.db_port,
            self.settings.db_user,
            self.settings.db_password,
            self.settings.db_name,
        )
        self.get_registers_from_database()

        #botões para alteração de páginas no tableWidget
        self.ui.btn_home.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_home))
        self.ui.btn_cadastrar.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_cadastrar))
        self.ui.btn_sobre.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_sobre))
        self.ui.btn_contatos.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.pg_contatos))

        #botões para as alterações principais da tabela
        self.ui.btnAdicionar.clicked.connect(self.insert_rows_in_qt)
        self.ui.btnExcluir.clicked.connect(self.delete_row)
        self.ui.btnExcel.clicked.connect(self.generate_excel)
        self.ui.btnAlterar.clicked.connect(self.update_row)

        self.ui.tabWidget.currentChanged.connect(self.get_registers_from_database)
        self.ui.txt_cnpj.textChanged.connect(self.auto_complete)
        self.ui.txt_nome_empresa.textChanged.connect(self.change_empresa_name)
        self.ui.btn_limpar.clicked.connect(self.clear_field)


    def change_empresa_name(self):
        escaped_name = html.escape(self.ui.txt_nome_empresa.text())
        rich_text = f'<html><head/><body><p align="center"><span style=" font-size:16pt; font-weight:700;">{escaped_name}</span></p></body></html>'
        self.ui.nomeEmpresa.setText(rich_text)

    def auto_complete(self):
        cnpj = self.ui.txt_cnpj.text()
        new_cnpj = cnpj.replace(' ', '').replace('-', '').replace('.', '').replace('/', '')
        if len(new_cnpj) == 14 and VALIDATE_CNPJ.validate(new_cnpj):
            ok, data = request_cnpj(new_cnpj, self.settings.receitaws_token)
            if not ok:
                QMessageBox.warning(self, 'Auto-complete', data)
                return
            self.ui.txt_nome_empresa.setText(data.get('nome', ''))
            self.ui.txt_logradouro.setText(data.get('logradouro', ''))
            self.ui.txt_numero.setText(data.get('numero', ''))
            self.ui.txt_complemento.setText(data.get('complemento', ''))
            self.ui.txt_bairro.setText(data.get('bairro', ''))
            self.ui.txt_municipio.setText(data.get('municipio', ''))
            self.ui.txt_uf.setText(data.get('uf', ''))
            self.ui.txt_cep.setText(data.get('cep', ''))
            self.ui.txt_telefone.setText(data.get('telefone', ''))
            self.ui.txt_email.setText(data.get('email', ''))

    def clear_field(self):
        self.ui.txt_nome_empresa.setText('')
        self.ui.txt_logradouro.setText('')
        self.ui.txt_numero.setText('')
        self.ui.txt_complemento.setText('')
        self.ui.txt_bairro.setText('')
        self.ui.txt_municipio.setText('')
        self.ui.txt_uf.setText('')
        self.ui.txt_cep.setText('')
        self.ui.txt_telefone.setText('')
        self.ui.txt_email.setText('')


    def insert_rows(self, *valores):
        row_index = self.table.rowCount()
        self.table.insertRow(row_index)
        for column, valor in enumerate(valores):
            item = QTableWidgetItem(str(valor))
            item.setData(Qt.ItemDataRole.UserRole, str(valor))
            if column == 0:
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row_index, column, item)

    def insert_rows_in_qt(self):
        entries = [
            self.ui.txt_cnpj.text().replace('-', '').replace(' ', '').replace('.', '').replace('/', ''),
            self.ui.txt_nome_empresa.text(),
            self.ui.txt_logradouro.text(),
            self.ui.txt_numero.text(),
            self.ui.txt_complemento.text(),
            self.ui.txt_bairro.text(),
            self.ui.txt_municipio.text(),
            self.ui.txt_uf.text().upper(),
            self.ui.txt_cep.text().replace('-', '').replace(' ', '').replace('.', ''),
            self.ui.txt_telefone.text(),
            self.ui.txt_email.text()
        ]
        ok, message = self.database.insert_empresa(*entries)
        if ok:
            self.insert_rows(*entries)
        else:
            QMessageBox.critical(self, 'Erro ao inserir', message)

    def get_registers_from_database(self):
        ok, registers = self.database.select_empresa()
        self.table.setRowCount(0)
        if not ok:
            if not self._connect_alert:
                self._connect_alert = True
                QMessageBox.warning(self, 'Conexão com o banco', 'Não foi possível conectar ao MySQL. Verifique o .env e consulte o README.')
            return
        for i in registers:
            self.insert_rows(*i)


    def delete_row(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            return
        cnpj = self.table.item(selected_row, 0).data(Qt.ItemDataRole.UserRole)
        ok, message = self.database.delete_empresa(cnpj)
        if ok:
            self.table.removeRow(selected_row)
        else:
            QMessageBox.critical(self, 'Erro ao excluir', message)


    def update_row(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            return
        cnpj_original = self.table.item(selected_row, 0).data(Qt.ItemDataRole.UserRole)
        data_changed = {}
        for column, campo in enumerate(FIELDS):
            if column == 0:
                continue
            item = self.table.item(selected_row, column)
            if item is None or item.text() == item.data(Qt.ItemDataRole.UserRole):
                continue
            data_changed[campo] = item.text()
        if data_changed:
            ok, message = self.database.update_empresa(data_changed, cnpj_original)
            if ok:
                for column in range(self.table.columnCount()):
                    item = self.table.item(selected_row, column)
                    if item is not None:
                        item.setData(Qt.ItemDataRole.UserRole, item.text())
            else:
                QMessageBox.critical(self, 'Erro ao alterar', message)


    def generate_excel(self):
        path = self.search_directory()
        if not path:
            return
        row_count = self.table.rowCount()
        column_count = self.table.columnCount()
        row_data = []
        row_data.append(FIELDS)
        for row in range(row_count):
            register = []
            for column in range(column_count):
                item = self.table.item(row, column)
                
                if item is not None:
                    register.append(item.text())
                else:
                    register.append("") 
            row_data.append(register)  
        ok, message = export_to_excel(row_data, path)
        if not ok: 
            QMessageBox.warning(self, 'Erro na geração excel',message)
            return
        QMessageBox.information(self, 'Sucesso', message)
        
    def search_directory(self):
        arquive_path = QFileDialog.getSaveFileName(
            parent=None,
            caption="Selecionar Pasta",
            dir="",
            filter='.xlsl' # Caminho inicial (vazio usa o diretório atual ou o último usado)
    )
        return arquive_path[0]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())