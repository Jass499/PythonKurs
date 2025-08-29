"""
    Autor:      Jasmin Schmitt
    Datum:      28.08.2025
    Version:    1.0

    Funktion aus (eigenem) Modul (*.py Datei mit Definitionen und deren Anweisungen)
    bzw. (eigenem) Paket ( ein Ordner, mit einer Initialisierungsdatei (__init__.py)) importieren

    from . import *

    . = das aktuelle Verzeichnis -> Trennzeichen zwischen Verzeichnissen beim import
    .. = darüberliegendes Verzeichnis
    \\ = Backslash muss doppelt angegeben werden

    (keinerlei Schrägstriche, kein Slash, kein Backslash)
"""
#  import sys

# Import gehören an den Anfang - in der Lerndatei nicht gemacht :D
# nur die Funktion asctime aus dem Modul time importieren
#from time import asctime as at  # mit as wird der Name der Funktion auf "at" geändert

#print(asctime())
#print(at())

# alle Funktionen aus dem Modul time importieren -> Version 1
#from time import *

#print(asctime())

# alle Funktionen aus dem Modul time importieren -> Version 2
# import time

# print(time.asctime())  # beim aufrufen von Funktionen muss der Modulname auch angegeben werden.

# alle Funktionen aus dem Modul time importieren -> Version 2
#import time as t # mit as wird der Name des Moduls auf "t" geändert

#print(t.asctime())  # beim aufrufen von Funktionen muss der Modulname auch angegeben werden.

# Aus eigenem Script = Modul
# Muss am Suchpfad PATH des Betriebssystem oder im aktuellen Ordner liegen!
#import sys

#print(sys.path)
#sys.path.append("c:\\etc\\meineModule")  # Suchpfad ergänzen

from operatorenFunktionen.meineTextfunktionen import *  # Importiert alle Funktionen

# Pythonkurs
# 0123456789
print("4 Zeichen ab dem 3 Zeichen:", mitte("Pythonkurs", 3, 4))
print("6 Zeichen von Links:", links("Pythonkurs", 6))
print("4 Zeichen von Rechts:", rechts("Pythonkurs", 4))

# Aus eigenem Paket importieren
# Muss am Suchpfad PATH des Betriebssystem oder im aktuellen Ordner liegen!
# nur ein Modul eines Pakets importieren
# from meinPaket.meineZufallsfunktionen import *

from meinPaket import *

print("Heutiger Wochentag: ", wochentagheute())
print("Zufallszahl:", meinezufallszahl())
