"""
    Autor:      Jasmin Schmitt
    Datum:      28.08.2025
    Version:    1.0

    Textdatei schreiben (csv)

    Bsp: Fixe Zeichenanzahl anstatt Trennzeichen

"""

#import io
import os
import sys

# Pfadangaben (c: oder ..) normal möglich, aber statt einen slash diesen verdoppeln
#quelldatei = "..\\dateisystem" # Nur für Fehlerprüfung notwendig.
quelldatei = "datenbank.csv"
zieldatei = "datenbank.txt"
dbcsv = None
dbtxt = None

# Existiert Quelldatei (oder Verzeichnis)?
if not os.path.exists(quelldatei):
    print("Datei (Verzeichnis) existiert nicht")
    sys.exit(0)  # Wenn Datei nicht existert wird Modul beendet!

# Ist Quelldatei eine Datei?
if not os.path.isfile(quelldatei):  # isdir kann für Verzeichnis angewendet werden
    print("Keine Datei!")
    sys.exit(0)  # Wenn Datei nicht existert wird Modul beendet!

# Zielatei löschen
if os.path.exists(zieldatei):
    try:
        os.remove(zieldatei)
        print("Alte Zieldatei wurde gelöscht.")
    except OSError:
        print("Löschen der alten Zieldatei fehlgeschlagen!")
        sys.exit(0)

# r zum lesen und wird standardmässig ausgeführt
# w ist das schreiben bzw. überschreiben
# a ist Anhängen
# + (w+, r+, a+) um Datei lesen zu können und schreiben
# x erzeugen der Datei
# b Binär - Modus lesen und schreiben
# t text - Modus lesen und schreiben = Standard

# Quelldatei öffnen
# eine Datei zum schreiben öffnen!!
# with open(quelldatei, "r") as dbcsv:
#     with (zieldatei, "w") as dbtxt:

with open(quelldatei, "r") as dbcsv, open(zieldatei, "w") as dbtxt:
    # Alles einlesen
    inhaltcsv = dbcsv.read()
    inhalttxt = ""

    # Inhalt wird gesplitet nach Zeilen
    zeilen = inhaltcsv.split(sep="\n")  # Inhalt wird in einer neuen Variable gespeichert

    # Für alle Zeilen aus
    for zeilennr in range(len(zeilen) - 1):
        # Zellen (Spalten einer Zeile) inListe einlesen
        zellen = zeilen[zeilennr].split(sep=";")
        # Für alle Zellen (Spalten einer Zeile)
        for spaltennr in range(len(zellen)):  # Spalten anzahl wird über len bestimmt
            # Hier die Anweisung für jede Zelle realisieren
            inhalttxt = inhalttxt + (zellen[spaltennr] + "               ")[:15]
        # Nächste Zeile in Zieldatei
        inhalttxt = inhalttxt + "\n"

    #Inhalt in Datei schreiben
    dbtxt.write(inhalttxt)

# Datei schliessen
dbcsv.close()
dbtxt.close()
