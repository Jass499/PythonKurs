# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'anwendungQtSideDesigner.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QGroupBox, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTabWidget, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionEnde = QAction(MainWindow)
        self.actionEnde.setObjectName(u"actionEnde")
        self.actionInfo = QAction(MainWindow)
        self.actionInfo.setObjectName(u"actionInfo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 771, 481))
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.label = QLabel(self.tab1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 49, 16))
        self.label_2 = QLabel(self.tab1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 49, 16))
        self.txtName = QLineEdit(self.tab1)
        self.txtName.setObjectName(u"txtName")
        self.txtName.setGeometry(QRect(110, 40, 113, 22))
        self.txtPasswort = QLineEdit(self.tab1)
        self.txtPasswort.setObjectName(u"txtPasswort")
        self.txtPasswort.setGeometry(QRect(110, 80, 113, 22))
        self.txtPasswort.setEchoMode(QLineEdit.EchoMode.Password)
        self.txtVielText = QTextEdit(self.tab1)
        self.txtVielText.setObjectName(u"txtVielText")
        self.txtVielText.setGeometry(QRect(30, 130, 301, 301))
        self.lstObst = QListWidget(self.tab1)
        self.lstObst.setObjectName(u"lstObst")
        self.lstObst.setGeometry(QRect(370, 20, 371, 192))
        self.cboProgramm = QComboBox(self.tab1)
        self.cboProgramm.setObjectName(u"cboProgramm")
        self.cboProgramm.setGeometry(QRect(380, 270, 351, 24))
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.chkWichtig = QCheckBox(self.tab2)
        self.chkWichtig.setObjectName(u"chkWichtig")
        self.chkWichtig.setGeometry(QRect(40, 70, 79, 20))
        self.grpAnrede = QGroupBox(self.tab2)
        self.grpAnrede.setObjectName(u"grpAnrede")
        self.grpAnrede.setGeometry(QRect(160, 50, 161, 141))
        self.optFrau = QRadioButton(self.grpAnrede)
        self.optFrau.setObjectName(u"optFrau")
        self.optFrau.setGeometry(QRect(30, 30, 92, 20))
        self.optHerr = QRadioButton(self.grpAnrede)
        self.optHerr.setObjectName(u"optHerr")
        self.optHerr.setGeometry(QRect(30, 80, 92, 20))
        self.calTermin = QCalendarWidget(self.tab2)
        self.calTermin.setObjectName(u"calTermin")
        self.calTermin.setGeometry(QRect(410, 60, 256, 190))
        self.tabWidget.addTab(self.tab2, "")
        self.cmdEnde = QPushButton(self.centralwidget)
        self.cmdEnde.setObjectName(u"cmdEnde")
        self.cmdEnde.setGeometry(QRect(700, 510, 75, 24))
        self.cmdAuswertung = QPushButton(self.centralwidget)
        self.cmdAuswertung.setObjectName(u"cmdAuswertung")
        self.cmdAuswertung.setGeometry(QRect(560, 510, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        self.menuHilfe = QMenu(self.menubar)
        self.menuHilfe.setObjectName(u"menuHilfe")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuHilfe.menuAction())
        self.menuDatei.addAction(self.actionEnde)
        self.menuHilfe.addAction(self.actionInfo)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Anwendung", None))
        self.actionEnde.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Passwort:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Seite 1", None))
        self.chkWichtig.setText(QCoreApplication.translate("MainWindow", u"Wichtig", None))
        self.grpAnrede.setTitle(QCoreApplication.translate("MainWindow", u"Anrede", None))
        self.optFrau.setText(QCoreApplication.translate("MainWindow", u"Frau", None))
        self.optHerr.setText(QCoreApplication.translate("MainWindow", u"Herr", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Seite 2", None))
        self.cmdEnde.setText(QCoreApplication.translate("MainWindow", u"Ende", None))
        self.cmdAuswertung.setText(QCoreApplication.translate("MainWindow", u"Auswertung", None))
        self.menuDatei.setTitle(QCoreApplication.translate("MainWindow", u"Datei", None))
        self.menuHilfe.setTitle(QCoreApplication.translate("MainWindow", u"Hilfe", None))
    # retranslateUi

