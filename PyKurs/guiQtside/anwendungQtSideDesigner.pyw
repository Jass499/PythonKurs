"""
    Autor:      Robert Panzirsch
    Datum:      x.x.20xx
    Version:    1.0

    Laden einer *.ui Datei (XML) des Qt / Side Designers zur Laufzeit (PyQt)
    bzw Konvertierung in ein Python Modul (PySide)

    PyQt kann ui Dateien direkt laden

    PySide benötigt eine Konvertierung in ein Python Modul:
    c:\\Python313\\Scripts\\pyside6-uic.exe anwendungQtSideDesigner.ui -o anwendungQtSideDesignerUI.py

"""

import sys

# Variante PyQt
#from PyQt6 import QtWidgets, uic


# Variante PySide
from PySide6 import QtWidgets
from anwendungQtSideDesignerUI import Ui_MainWindow


class Anwendung(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        # Eigener Konstruktor
        super().__init__(parent)
        # Aufruf Konstruktor QMainWindow
        # Variante PyQt
        #self.ui = uic.loadUi("anwendungQtSideDesigner.ui", self)
        # Variante PySide
        self.ui = Ui_MainWindow()  # Instanzieren
        self.ui.setupUi(self)  # Steuerelemente erzeugen und platzieren
        self.ui.cmdAuswertung.clicked.connect(self.onauswertung)
        self.ui.cmdEnde.clicked.connect(self.onende)
        # Slot zum Empfang des Klick Ereignisses der Schaltfläche einrichten
        self.ui.actionEnde.triggered.connect(self.onende)
        self.ui.actionInfo.triggered.connect(self.oninfo)
        # Slot zum Empfang des Klick Ereignisses im Menü einrichten
        self.ui.lstObst.addItem("Apfel")
        self.ui.lstObst.addItem("Birne")
        self.ui.lstObst.addItem("Kirsche")
        self.ui.lstObst.addItem("Banane")
        self.ui.lstObst.setCurrentRow(0)
        # Liste füllen und erstes auswählen
        self.ui.cboProgramm.addItem("Word")
        self.ui.cboProgramm.addItem("Excel")
        self.ui.cboProgramm.addItem("Access")
        # Kombinationsfeld füllen
        self.ui.statusbar.showMessage("Anwendung gestartet!", 5000)
        # 5 Sekunden lang in die Statusleiste schreiben

    def onauswertung(self):
        msgboxauswertung = QtWidgets.QMessageBox()
        # Variante für PyQt: self.ui.calTermin.selectedDate().toPyDate()
        # Variante für PySide: self.ui.calTermin.selectedDate().toPython()
        auswertung = (
                "Name: " + self.ui.txtName.text() +
                "\nPasswort: " + self.ui.txtPasswort.text() +
                ("\nAnrede: Frau" if self.ui.optFrau.isChecked() else
                 ("\nAnrede: Herr" if self.ui.optHerr.isChecked() else "\nAnrede: ")) +
                ("\nWichtig: Ja" if self.ui.chkWichtig.isChecked() else "\nWichtig: Nein") +
                # "\nDatum: " + str(self.ui.calTermin.selectedDate().toPyDate()) +
                "\nDatum: " + str(self.ui.calTermin.selectedDate().toPython()) +
                "\nObst: " + self.ui.lstObst.currentItem().text() +
                "\nProgramm: " + self.ui.cboProgramm.currentText() +
                "\nText: " + self.ui.txtVielText.toPlainText()
        )
        msgboxauswertung.setText(auswertung)
        msgboxauswertung.exec()

    def onende(self):
        self.close()

    def oninfo(self):
        msgboxinfo = QtWidgets.QMessageBox()
        msgboxinfo.setText("Copyright Wifi Wien")
        msgboxinfo.exec()
        self.ui.statusbar.showMessage("Info angezeigt!", 5000)


anwendung = QtWidgets.QApplication(sys.argv)
# Anwendung mit Hauptschleife erzeugen
app = Anwendung()
# Fenster erzeugen
app.show()
# und anzeigen
sys.exit(anwendung.exec())
# Hauptschleife starten
