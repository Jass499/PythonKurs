"""
    Autor:      Jasmin Schmitt
    Datum:      28.08.2025
    Version:    1.0

    Modul für den Import
    Enthält (üblicherweise) nur Definitionen

"""

from datetime import date


# Funktion mit einen Rückgabewert
def wochentagheute():
    """ Liefert den heutigen Wochentag. """
    return ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[date.today().weekday()]


if __name__ != "__main__":
    print("Modul importiert, Code exekutiert!")
