# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'halloWeltQtSideDesigner.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(256, 197)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 161, 61))
        font = QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.schaltflaecheok = QPushButton(Dialog)
        self.schaltflaecheok.setObjectName(u"schaltflaecheok")
        self.schaltflaecheok.setGeometry(QRect(70, 120, 111, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.schaltflaecheok.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Mein Hallo Welt", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Hallo Welt!", None))
        self.schaltflaecheok.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

