"""
    Autor:      Jasmin Schmitt
    Datum:      28.08.2025
    Version:    1.0

    unittest

"""

import unittest
#import codeTestenDokumentieren.codeBeispiel.meineBerechnungen
# Hier wird aus dem Modul Klasse & def meinesubtraktion (da außerhalb der Klasse)
from codeTestenDokumentieren.codeBeispiel.meineBerechnungen import Berechnungen, meinesubtraktion


# Zugriff auf docstring
#print("docstring __doc__ aus meineBerechnungen Modul:", codeTestenDokumentieren.codeBeispiel.meineBerechnungen.__doc__)

# assert Statement (Behauptung)
# Wenn Bedingung True passiert nichts, wenn False wird ein Fehler erzeugt und eine Meldung ausgegeben.
#assert 1 > 0
#assert 1 < 0
#assert 1 < 0, "Die Behauptung ist falsch!"

# unittest Modul (Framework für Code testen
# TestCase Klasse mit folgenden assert Methoden:
# assertEqual(a, b) prüft ob a == b
# assertTrue (x) prüft ob bool(x) is True
# assertIs(a, b) prüft ob a is b
# assertIn(a, b) prüft ob a in b
# assertIsInstance(a, b) prüft ob isinstance(a, b) = Fragt ab ob Objekt der gewünschten Klasse entspricht


class TestBerechnungen(unittest.TestCase):
    def test_meinesumme1(self):
        """Name muss mit test (Unterstrich muss nicht sein) beginnen! (Sonst wird nicht getestet)
            Testet meine Methode meinesumme aus meiner Klasse Berechnungen"""
        ergebnis = Berechnungen(2, 4)
        # Objekt Instanz aus Klasse Berechnungen erzeugen.
        # Test mit 7 statt 6 muss Fehler liefern
        self.assertEqual(ergebnis.meinesumme(), 6, "Die Summe wird nicht richtig berechnet!")

    def test_meinprodukt(self):
        """ Testet meine Methode meinprodukt aus mein Klasse Berechnungen """
        ergebnis = Berechnungen(2, 4)
        # Objekt Instanz aus Klasse Berechnungen erzeugen.
        # Test mit 9 statt 8 muss Fehler liefern
        self.assertEqual(ergebnis.meinprodukt(), 8, "Das Produkt wird nicht richtig berechnet!")

    def test_meinwahr(self):
        """ Testet meine Methode meinprodukt aus mein Klasse Berechnungen """
        ergebnis = Berechnungen(True, True)  # Test mit True, False muss fehler liefern
        # Objekt Instanz aus Klasse Berechnungen erzeugen.
        self.assertTrue(ergebnis.meinwahr(), "Der Vergleich ist logisch nicht wahr!")

    def test_meinesumme2(self):
        """Name muss mit test (Unterstrich muss nicht sein) beginnen! (Sonst wird nicht getestet)
            Testet meine Methode meinesumme aus meiner Klasse Berechnungen"""
        ergebnis = Berechnungen(2, 4)  # Test mit 200, 400 muss Fehler liefern
        # Objekt Instanz aus Klasse Berechnungen erzeugen.
        self.assertIs(ergebnis.meinesumme(), 6, "Die Objekte sind nicht identisch!")

    def test_meinesumme3(self):
        """Testet meine Methode meinesumme aus meiner Klasse Berechnungen"""
        ergebnis = Berechnungen(2, 4)
        # Objekt Instanz aus Klasse Berechnungen erzeugen.
        # Test mit [3, 7, 14]  muss Fehler liefern
        self.assertIn(ergebnis.meinesumme(), [3, 6, 14], "Das Ergebnis ist nicht in der Liste enthalten")

    def test_meinesumme4(self):
        """Testet meine Methode meinesumme aus meiner Klasse Berechnungen"""
        ergebnis = Berechnungen(2, 4)  # Test mit 2.0,4 muss Fehler liefern
        # Objekt Instanz aus Klasse Berechnungen erzeugen.
        self.assertIsInstance(ergebnis.meinesumme(), int, "Das Ergebnis ist nicht Integer!")

    def test_meinesubtraktion(self):
        """Testet meine Methode test_meinesubtraktion aus meine Modul meineBerechnungen"""
        # Test mit -3 muss Fehler liefern
        self.assertEqual(meinesubtraktion(2, 4) - 4, "Die Subtraktion wird nicht richtig berechnet!")


if __name__ == "__main__":
    unittest.main()
