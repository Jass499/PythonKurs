"""
    Autor:      Jasmin Schmitt
    Datum:      28.08.2025
    Version:    1.0

    Klasse mit Methoden, sowie eine Funktion (def) für den Import

    für
        - unittest
        - pydoc

    Wir schreiben hier in einem anynomen mehrzeiligen Text, das ist eigentlich kein Kommentar,
    sondern der docstring, der auch über die Systemvariable __doc__ zugänglich ist.
    Dies würde nicht mit einzeiligen Kommentar funktionieren.

    pydoc
    Utility, ein Modul von Python zur Dokumentation.
    Ähnlich help()

    Syntax: python -m pydoc [keyword|function|modul|paket|..] -> Eingabe im Terminal
    python -m pydoc os  # -m steht für Modul exekutieren pydoc als Script, mit Argument os
    python -m pydoc -b  # startet Browser, mit q im Terminal wird der Vorgang gestoppt
    python -m pydoc meineBerechnungen
    python -m pydoc -w meine Berechnungen

    Vergleiche:
    python
    helo()
    os

    oder:
    python
    help("os")

"""


class Berechnungen:
    def __init__(self, x, y):
        """Initialisierung, Argumente in Eigenschaften der Klasse ablegen"""
        self.x = x
        self.y = y

    def meinesumme(self):
        """Liefert die arithmetische Summe: x + y"""
        return self.x + self.y

    def meinprodukt(self):
        """Liefert das arithmetische Produkt: x * y"""
        return self.x * self.y

    def meinwahr(self):
        """Liefert True wenn gleich: x == y"""
        return self.x == self.y


def meinesubtraktion(x, y):
    """Liefert die arithmetische Differenz: x - y"""
    return x - y

