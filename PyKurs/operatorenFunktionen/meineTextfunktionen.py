"""
    Autor:      Jasmin Schmitt
    Datum:      28.08.2025
    Version:    1.0

    Modul für den Import
    Enthält (üblicherweise) nur Definitionen

"""


# slice notation
# [start:ende]              von Element Nummer start bis Element Nummer ende -1 (="MITTE)
# [start:start+anzahl]      Anzahl Zeichen ab dem Zeichen Nr start. Um thon aus Pythonkurs zu bekommen.
#                           Pythonkurs"[2:2 + 4] verwenden (Teil)
# [:ende]                   alles bis Element Nummer ende -1 = ende Elemente von vorne oder links (="LINKS)
# [-start:]                 start Element von hinten oder rechts (="RECHTS)


def links(zeichenkette, anzahl):
    """ Liefert anzahl Zeichen der Zeichenkette von Links """
    return zeichenkette[:anzahl]


def rechts(zeichenkette, anzahl):
    """ Liefert anzahl Zeichen der Zeichenkette von Rechts """
    return zeichenkette[-anzahl:]


def mitte(zeichenkette, anfang, anzahl):
    """ Liefert anzahl Zeichen ab dem Zeichen anfang (erstes Zeichen ist Nr1) der Zeichenkette """
    return zeichenkette[anfang - 1:anfang - 1 + anzahl]
    # Hier muss -1 verwendet werden, da Python mit 0 rechnet aber der Benutzer mit 1 Starten wird.


# Wenn die Datei als Script exekutiert wird, steht in der Systemvariable __name__ der Wert __main__
# Wenn die Datei als Modul importiert wird, steht in der Systemvariable __name__ der Wert meineTextfunktionen
# Also der Namenteil ohne Dateierweiterung der *.py Datei

if __name__ == "__main__":
    # Pythonkurs
    # 0123456789
    print("4 Zeichen ab dem 3 Zeichen:", mitte("Pythonkurs", 3, 4))
    print("6 Zeichen von Links:", links("Pythonkurs", 6))
    print("4 Zeichen von Rechts:", rechts("Pythonkurs", 4))
else:
    print("Modul importiert, Code exekutiert!")
