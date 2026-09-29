from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_main import Ui_MainWindow
from excel import exportar_excel
from requisicoes import requestCNPJ
from database import Database
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()   #atributo relacionado as alterações internas do sistema
        self.ui.setupUi(self)
        self.setWindowTitle("SysDev - Sistema de cadastro de empresas")
        appIcon = QIcon(u"logo_sysdev_240px.png")
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
        self.ui.btnAlterar.clicked.connect(self.alter_database)

        self.ui.tabWidget.currentChanged.connect(self.show_registers_from_database)

        self.ui.txt_cnpj.textChanged.connect(self.auto_insert)
        self.ui.txt_nome_empresa.textChanged.connect(self.alterar_nome_empresa)


    def alterar_nome_empresa(self):
        texto_rico = f'<html><head/><body><p align="center"><span style=" font-size:16pt; font-weight:700;">{self.ui.txt_nome_empresa.text()}</span></p></body></html>'
        self.ui.nomeEmpresa.setText(texto_rico)

    def auto_insert(self):
        cnpj = self.ui.txt_cnpj.text()
        new_cnpj = cnpj.replace(' ', '').replace('-', '').replace('.', '').replace('/', '')
        if len(new_cnpj) == 14:
            request = requestCNPJ(new_cnpj)
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


    def show_rows(self, cnpj, nome_empresa, logradouro, numero, complemento, bairro, municipio, uf, cep, telefone, email):
        row_index = self.table.rowCount()  
        self.table.insertRow(row_index)       

        self.table.setItem(row_index, 0, QTableWidgetItem(cnpj))
        self.table.setItem(row_index, 1, QTableWidgetItem(nome_empresa))
        self.table.setItem(row_index, 2, QTableWidgetItem(logradouro))
        self.table.setItem(row_index, 3, QTableWidgetItem(numero))
        self.table.setItem(row_index, 4, QTableWidgetItem(complemento))
        self.table.setItem(row_index, 5, QTableWidgetItem(bairro))
        self.table.setItem(row_index, 6, QTableWidgetItem(municipio))
        self.table.setItem(row_index, 7, QTableWidgetItem(uf))
        self.table.setItem(row_index, 8, QTableWidgetItem(cep))
        self.table.setItem(row_index, 9, QTableWidgetItem(telefone))
        self.table.setItem(row_index, 10, QTableWidgetItem(email))

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
        self.show_rows(*entries)

    def show_registers_from_database(self):
        registers = self.database.select_empresa()
        for i in registers:
            self.show_rows(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10])
    
    def delete_row(self):
        selected_row = self.table.currentRow()
        cnpj = self.table.item(selected_row, 0).text()
        self.database.delete_empresa(cnpj)
        self.table.removeRow(selected_row)

    def alter_database(self):
        registers = self.database.select_empresa()
        for i in registers:
            self.insert_row()
        
    

    def gerar_excel(self):
        row_count = self.table.rowCount()
        column_count = self.table.columnCount()
        row_data = []

        cabecalho = []
        for column in range(column_count):
            item = self.table.horizontalHeaderItem(column)
            if item is not None:
                cabecalho.append(item.text())
            else:
                cabecalho.append(f"Coluna {column}")
        
        row_data.append(cabecalho)

        for row in range(row_count):
            register = []
            for column in range(column_count):
                item = self.table.item(row, column)
                
                if item is not None:
                    register.append(item.text())
                else:
                    register.append("") 
            row_data.append(register)  
        print(row_data)
        # exportar_excel(row_data)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

    # if self.ui.tabWidget.indexOf(self.ui.tabWidget.currentWidget) == 1 else None