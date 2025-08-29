"""
    Autor:      Jasmin Schmitt
    Datum:      28.08.2025
    Version:    1.0

    Modul für den Import
    Enthält (üblicherweise) nur Definitionen

"""

from random import randint

untergrenze = 0
obergrenze = 100


def meinezufallszahl():
    """ Liefert eine zufällige ganze Zahl """
    return randint(untergrenze, obergrenze)


if __name__ != "__main__":
    print("Modul importiert, Code exekutiert!")
