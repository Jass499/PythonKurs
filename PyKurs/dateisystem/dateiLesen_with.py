"""
    Autor:      Jasmin Schmitt
    Datum:      28.08.2025
    Version:    1.0

    Textdatei lesen (csv)

"""

#import io
import os
import sys

# Pfadangaben (c: oder ..) normal möglich, aber statt einen slash diesen verdoppeln
#quelldatei = "..\\dateisystem" # Nur für Fehlerprüfung notwendig.
quelldatei = "datenbank.csv"
dbcsv = None

# Existiert Datei (oder Verzeichnis)?
if not os.path.exists(quelldatei):
    print("Datei (Verzeichnis) existiert nicht")
    sys.exit(0)  # Wenn Datei nicht existert wird Modul beendet!

# Ist das eine Datei?
if not os.path.isfile(quelldatei):  # isdir kann für Verzeichnis angewendet werden
    print("Keine Datei!")
    sys.exit(0)  # Wenn Datei nicht existert wird Modul beendet!

# r zum lesen und wird standardmässig ausgeführt
# w ist das schreiben bzw. überschreiben
# a ist Anhängen
# + (w+, r+, a+) um Datei lesen zu können und schreiben
# x erzeugen der Datei
# b Binär - Modus lesen und schreiben
# t text - Modus lesen und schreiben = Standard

# Datei öffnen
# eine Datei zum schreiben öffnen!!
with open(quelldatei, "r") as dbcsv:
    # Alles einlesen
    inhaltcsv = dbcsv.read()

    # Inhalt wird gesplitet nach Zeilen
    zeilen = inhaltcsv.split(sep="\n")  # Inhalt wird in einer neuen Variable gespeichert

    # Zeilenanzahl?
    print("Zeilenanzahl:", len(zeilen))

    # Für alle Zeilen aus
    for zeilennr in range(len(zeilen) - 1):
        # Zellen (Spalten einer Zeile) inListe einlesen
        zellen = zeilen[zeilennr].split(sep=";")
        # Für alle Zellen (Spalten einer Zeile)
        for spaltennr in range(len(zellen)):  # Spalten anzahl wird über len bestimmt
            # Hier die Anweisung für jede Zelle realisieren
            print((zellen[spaltennr] + "               ")[:15], end="")
        # Nächste Zeile in Ausgabe
        print()

# Datei wird automatisch geschlossen, das with ein ersatz für diesen Code ist
# try:
#     dbcsv = open(quelldatei, "r")
#     # operationen
# finally:
#     dbcsv.close()
