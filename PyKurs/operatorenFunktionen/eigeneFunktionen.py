"""
    Autor:      Jasmin Schmitt
    Datum:      27.08.2025
    Version:    1.0

    Eigene Funktionen definieren

"""

from datetime import date, timedelta
from inspect import signature


# Funktion ohne Rückgabewert (Subroutine = Unterprogramm, Prozedur)
def meineausgabefunktion(zeichenkette):
    print(zeichenkette)


# Verwendung meiner Funktion meineausgabefunktion
#eingabe = input("Bitte Text eingeben: ")
#meineausgabefunktion(eingabe)  # ist wie ein Echo


# Funktion mit einen Rückgabewert
def wochentag1(datum):
    return ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[datum.weekday()]


# Verwendung meiner Funktion wochentag1
print("Wir haben heute " + wochentag1(date.today()) + "!")


# Funktion mit einen Rückgabewert und optionalen Argument
def wochentag2(datum=date.today()):
    return ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[datum.weekday()]


# Verwendung meiner Funktion wochentag2
print("Wir haben heute " + wochentag2() + "!")
print("Wir hatten gestern " + wochentag2(date.today() - timedelta(days=1)) + "!")


# Funktion mit einen Rückgabewert und einem und belieig vielen weiteren Argumenten
# **weitere Argumente für beliebige viele weiter Schlüsselwort Argumente
def wochentag3(datum1, *weitere_datum):
    ergebnis = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[datum1.weekday()]
    for datum in weitere_datum:
        ergebnis = (ergebnis + ", " +
                    ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[datum.weekday()])
    return ergebnis


# Verwendung meiner Funktion wochentag1
print("Wir haben heute, morgen und übermorgen " +
      wochentag3(date.today(), date.today() + timedelta(days=1), date.today() + timedelta(days=2)) + "!")
print("Argumentliste: ", signature(wochentag3))
