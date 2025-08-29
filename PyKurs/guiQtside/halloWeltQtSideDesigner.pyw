"""
    Autor:      Robert Panzirsch
    Datum:      x.x.20xx
    Version:    1.0

    Laden einer *.ui Datei (XML) des Qt / Side Designers zur Laufzeit (PyQt)
    bzw Konvertierung in ein Python Modul (PySide)

    PyQt kann ui Dateien direkt laden

    PySide benötigt eine Konvertierung in ein Python Modul:
    c:\\Python313\\Scripts\\pyside6-uic.exe halloWeltQtSideDesigner.ui -o halloWeltQtSideDesignerUI.py

"""

import sys

# Variante PyQt
#from PyQt6 import QtWidgets, uic


# Variante PySide
from PySide6 import QtWidgets
from halloWeltQtSideDesignerUI import Ui_Dialog


class HalloWelt(QtWidgets.QDialog):
    def __init__(self, parent=None):
        # Eigener Konstruktor
        super().__init__(parent)
        # Aufruf Konstruktor QDialog
        # Variante PyQt
        #self.ui = uic.loadUi("halloWeltQtSideDesigner.ui", self)
        # Variante PySide
        self.ui = Ui_Dialog()  # Instanzieren
        self.ui.setupUi(self)  # Steuerelemente erzeugen und platzieren
        self.ui.schaltflaecheok.clicked.connect(self.onok)
        # Slot zum Empfang des Klick Ereignisses einrichten

    def onok(self):
        self.close()


anwendung = QtWidgets.QApplication(sys.argv)
# Anwendung mit Hauptschleife erzeugen
dialog = HalloWelt()
# Fenster erzeugen
dialog.show()
# und anzeigen
sys.exit(anwendung.exec())
# Hauptschleife starten
