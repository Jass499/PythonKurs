"""
    Autor:      Jasmin Schmitt
    Datum:      26.08.2025
    Version:    1.0

    Ausgabe: zufälliges, eine gewisse Anzahl Stellen langes Passwort

    Alternativ: Silbe bauen: Mitlaut-Selbstlaut-Mitlaut

"""

from random import randint, seed

untergrenze = 65  # Das ist ASCII Code Buchstabe A
obergrenze = 90  # Das ist ASCII Code Buchstabe Z
laenge = 14


def zufallsbuchstabe():
    """Liefert einen zufälligen Buchstaben."""
    seed()
    return chr(randint(untergrenze, obergrenze))  # Zahl wird mit chr in Buchstaben umgewandelt.


def zufallspasswort():
    """Liefert ein zufälliges, eine gewisse Anzahl an Stellen, langes Passwort."""
    passwort = ""
    for i in range(laenge):
        passwort = passwort + zufallsbuchstabe()
    return passwort


print("Zufälliges ", laenge, "Zeichen langes Passwort:", zufallspasswort())
