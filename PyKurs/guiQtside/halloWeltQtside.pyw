"""
    Autor:      Robert Panzirsch
    Datum:      x.x.20xx
    Version:    1.0

    GUI mit Modul QtWidgets von Paket PyQt6 (oder PySide6)

    PyQt und PySide sind ziemlich identisch, haben aber unterschiedliche Hersteller und Lizenzbedingungen

    Beim Paket PySide ist auch der Designer dabei:
    c:\\Python313\\Lib\\site-packages\\PySide6\\designer.exe

"""

import sys
#from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

anwendung = QApplication(sys.argv)
# Aus QApplication Klasse Anwendung mit Argumenten instanzieren

fenster = QWidget()
# Fenster instanzieren, QWidget ist Basisklasse für Steuerelemente

fenster.resize(300, 100)
# Größe einstellen

fenster.setWindowTitle("Fenster mit Qt/Side")
# Titel einstellen

fenster.beschriftung = QLabel("Hallo Welt!")
# Beschriftung erzeugen

fenster.schaltflaeche = QPushButton("OK")
# Schaltfläche erzeugen

fenster.schaltflaeche.clicked.connect(fenster.close)
# Klick Ereignisbehandlung für Schaltfläche einrichten
# Slot zum Empfang des Klick Signals einrichten

box = QVBoxLayout()
# Box Layout erzeugen

box.addWidget(fenster.beschriftung)
# Beschriftung montieren
box.addWidget(fenster.schaltflaeche)
# Schaltfläche montieren

fenster.setLayout(box)
# Fenster auf Box Layout setzen

fenster.show()
# Fenster anzeigen
sys.exit(anwendung.exec())
# Anwendung (Hauptroutine) starten
