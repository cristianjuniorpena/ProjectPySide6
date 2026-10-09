# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)
import myrecursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(769, 600)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(200, 16777215))
        self.left_container.setStyleSheet(u"")
        self.left_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 156, 434))
        self.page.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(11)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

        self.btn_contatos = QPushButton(self.page)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setMinimumSize(QSize(0, 30))
        self.btn_contatos.setFont(font)
        self.btn_contatos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_contatos)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 96, 26))
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 111, 391))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frmHeader = QFrame(self.main_container)
        self.frmHeader.setObjectName(u"frmHeader")
        self.frmHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmHeader.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frmHeader)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frmHeader)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frmHeader)

        self.frmMain = QFrame(self.main_container)
        self.frmMain.setObjectName(u"frmMain")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmMain.sizePolicy().hasHeightForWidth())
        self.frmMain.setSizePolicy(sizePolicy)
        self.frmMain.setStyleSheet(u"")
        self.frmMain.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmMain.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frmMain)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Pages = QStackedWidget(self.frmMain)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Pages.setStyleSheet(u"")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_6 = QVBoxLayout(self.pg_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.pg_home)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_7)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_7 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_10 = QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_logradouro = QLineEdit(self.frame_4)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_logradouro, 4, 0, 1, 3)

        self.txt_bairro = QLineEdit(self.frame_4)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_bairro, 5, 2, 1, 1)

        self.nomeEmpresa = QLabel(self.frame_4)
        self.nomeEmpresa.setObjectName(u"nomeEmpresa")

        self.gridLayout.addWidget(self.nomeEmpresa, 0, 0, 1, 3)

        self.txt_numero = QLineEdit(self.frame_4)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_numero, 5, 0, 1, 1)

        self.txt_telefone = QLineEdit(self.frame_4)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone, 7, 0, 1, 1)

        self.txt_complemento = QLineEdit(self.frame_4)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_complemento, 5, 1, 1, 1)

        self.txt_cep = QLineEdit(self.frame_4)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_cep, 6, 2, 1, 1)

        self.txt_nome_empresa = QLineEdit(self.frame_4)
        self.txt_nome_empresa.setObjectName(u"txt_nome_empresa")
        self.txt_nome_empresa.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome_empresa, 3, 1, 1, 2)

        self.txt_uf = QLineEdit(self.frame_4)
        self.txt_uf.setObjectName(u"txt_uf")
        self.txt_uf.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_uf, 6, 1, 1, 1)

        self.txt_email = QLineEdit(self.frame_4)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_email, 7, 1, 1, 2)

        self.txt_cnpj = QLineEdit(self.frame_4)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        self.txt_cnpj.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_cnpj, 3, 0, 1, 1)

        self.txt_municipio = QLineEdit(self.frame_4)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_municipio, 6, 0, 1, 1)

        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.label_12.setWordWrap(True)

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 3)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.btnAdicionar = QPushButton(self.tab)
        self.btnAdicionar.setObjectName(u"btnAdicionar")

        self.verticalLayout_10.addWidget(self.btnAdicionar, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.Empresas = QWidget()
        self.Empresas.setObjectName(u"Empresas")
        self.verticalLayout_9 = QVBoxLayout(self.Empresas)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.Empresas)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Table = QTableWidget(self.Empresas)
        if (self.Table.columnCount() < 11):
            self.Table.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.Table.setObjectName(u"Table")

        self.horizontalLayout_5.addWidget(self.Table)

        self.frame_3 = QFrame(self.Empresas)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btnAlterar = QPushButton(self.frame_3)
        self.btnAlterar.setObjectName(u"btnAlterar")

        self.verticalLayout_8.addWidget(self.btnAlterar)

        self.btnExcluir = QPushButton(self.frame_3)
        self.btnExcluir.setObjectName(u"btnExcluir")

        self.verticalLayout_8.addWidget(self.btnExcluir)

        self.btnExcel = QPushButton(self.frame_3)
        self.btnExcel.setObjectName(u"btnExcel")

        self.verticalLayout_8.addWidget(self.btnExcel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.Empresas, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_cadastrar)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.splitter = QSplitter(self.pg_contatos)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(150, 190, 161, 32))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.label_10 = QLabel(self.splitter)
        self.label_10.setObjectName(u"label_10")
        self.splitter.addWidget(self.label_10)
        self.label_11 = QLabel(self.splitter)
        self.label_11.setObjectName(u"label_11")
        self.splitter.addWidget(self.label_11)
        self.Pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_11 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.pg_sobre)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_11.addWidget(self.label_8)

        self.label_9 = QLabel(self.pg_sobre)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_9)

        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.frmMain)

        self.frmfooter = QFrame(self.main_container)
        self.frmfooter.setObjectName(u"frmfooter")
        self.frmfooter.setFrameShape(QFrame.Shape.StyledPanel)
        self.frmfooter.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frmfooter)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frmfooter)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frmfooter)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sys Dev Fernando", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Usu\u00e1rio: Padoka</p><p>Sistema: Cadastro</p><p>Status: Ativo</p><p>Venc: 31/12/2026</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema de Cadastro", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/myrecursos/logo_sysdev_240px.png\"/></p></body></html>", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.nomeEmpresa.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Empresa</span></p></body></html>", None))
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_nome_empresa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Empresarial", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email", None))
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Insira primeiramente o CNPJ para realizar o Auto-preenchimento</span></p></body></html>", None))
        self.btnAdicionar.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"EMPRESAS", None))
        ___qtablewidgetitem = self.Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        ___qtablewidgetitem1 = self.Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None))
        ___qtablewidgetitem2 = self.Table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None))
        ___qtablewidgetitem3 = self.Table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None))
        ___qtablewidgetitem4 = self.Table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        ___qtablewidgetitem5 = self.Table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        ___qtablewidgetitem6 = self.Table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None))
        ___qtablewidgetitem7 = self.Table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None))
        ___qtablewidgetitem8 = self.Table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        ___qtablewidgetitem9 = self.Table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        ___qtablewidgetitem10 = self.Table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"E-MAIL", None))
        self.btnAlterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btnExcluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btnExcel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Empresas), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/myrecursos/whatsApp.png\"/></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>+55 43 98382-9134</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">SOBRE</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#000000;\">Este sistema faz consulta do CNPJ utilizando API da Receita Federal e faz o cadastro em um banco de dados. O objetivo deste sistema \u00e9 ensinar como utilizar Python e o QT para desenvolver aplica\u00e7\u00f5es modernas e funcionais.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sys dev Cristian Jr", None))
    # retranslateUi

