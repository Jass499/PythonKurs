"""
    Autor:      Jasmin Schmitt
    Datum:      26.08.2025
    Version:    1.0

    Funktionen

    In Python sind auch Funktionen Objekte (Callable objects) und haben daher:
        - eine ID (Nummer)
        - einen Value (Rückgabewert)
        - eventuell eine Reference (Funktionsname)
        - einen Typ (Datentyp) (ergibt sich aus Rückgabewert)

"""

from operator import truediv, floordiv, sub, mul, add, mod, eq, gt  # le, ge, ne, lt
# truediv Flieskommadivision, floordiv Ganzzahldivision
# from math import fabs, ceil, floor, trunc, fmod, frexp, nan, isnan, sqrt, isqrt, pow, pi
import math
from random import randrange, randint, random, seed, shuffle, choice, sample
from datetime import date, time, datetime, timedelta
from time import asctime  #strftime, sleep
import sys  # Python System
import os  # Operation System

# from subprocess import Popen

print("******************* Funktionen sind Objekte *******************")
print("id(print):", id(print))
print("type(print):", type(print))

print("******************* Funktionen sind Objekte *******************")
help(print)

print("******************* Mathematik *******************")
print("abs(-3.5):", abs(-3.5))
print("min([20, 10, -5, 70, -15]):", min([20, 10, -5, 70, -15]))
print("max([20, 10, -5, 70, -15]):", max([20, 10, -5, 70, -15]))
print("min(20, 10, -5, 70, -15):", min(20, 10, -5, 70, -15))
print("max(20, 10, -5, 70, -15):", max(20, 10, -5, 70, -15))
print("sum([20, 10, -5, 70, -15]):", sum([20, 10, -5, 70, -15]))
print("round(-3.344, 2):", round(-3.344, 2))
print("round(-3.345, 2):", round(-3.345, 2))

# Zufall (passiert ohne Ursache)
# Hier chaotisch
seed()  # Initialisieren
for i in range(5):  # wird 5 mal ausgeführt
    print("random():", random())  # Zahl zwischen 0 und 100
for i in range(5):  # wird 5 mal ausgeführt
    print("randrange(0, 101, 2):", randrange(0, 101, 2))  # Zufallsgenerator zwischen 1 und 100
for i in range(5):  # wird 5 mal ausgeführt
    print("choice(0, 101, 2):", choice(range(0, 101, 2)))  # Zufallsgenerator zwischen 1 und 100
for i in range(5):  # wird 5 mal ausgeführt
    print("randint(1, 100):", randint(1, 100))  # Zufallsgenerator zwischen 1 und 100

meinesequenze = ["b", 3, (6, "c"), 5.6]
for i in range(5):  # wird 5 mal ausgeführt
    print("choice([\"b\", 3,(6, \"c\"), 5.6]):", choice(meinesequenze))  # Zufallsgenerator zwischen 1 und 100

# mischen
print("Original Meinesequenze;", meinesequenze)
shuffle(meinesequenze)
print("Meinesequenze gemischt:", meinesequenze)

# Zufällige Liste erzeugen
for i in range(5):
    print("sample([\"abc\", 100, (10, \"def\")], counts=[2, 4, 3], k=4):",
          sample(["abc", 100, (10, "def")], counts=[2, 4, 3], k=4))
    # sample funktion wählt zufällig k Elemente aus der Beispielliste (1. Argument) aus
    # k <= der länge von dieser Beispielliste
    # counts vervielfältigt die Werte aus der Liste/ identisch mit
    # print(":", sample(["abc", "abc", 100, 100, 100, 100, (10, "def"), (10, "def"), (10, "def")], k=4))

# Vergleich mit Operatoren
print("truediv(sub(mul(2, add(3,4)),4), 5):", truediv(sub(mul(2, add(3, 4)), 4), 5))
# Unterschied
print("truediv (7, 2):", truediv(7, 2))
print("floordiv (7, 2:", floordiv(7, 2))
print("mod (7, 2:", mod(7, 2))
print("divmod (7, 2:", divmod(7, 2))
print("pow(2, 8):", pow(2, 8))
print("math.pow(2, 8):", math.pow(2, 8))
print("math.fabs(-23.34):", math.fabs(-23.34))  #Absolutbetrag einer Zahl (in float)
print("math.ceil(-23.45):", math.ceil(-23.45))  # liefert die kleinste integer größergleich der Angabe
print("math.floor(-23.45):", math.floor(-23.45))  # liefert die größte integer kleinergleich der Angabe
print("math.trunc(-23.45):", math.trunc(-23.45))  # Zahl ohne Dezimalstellen
print("math.fmod(7, 2):", math.fmod(7, 2))  # Modulo in float (Rest der Ganzzahldivision)
print("math.frexp(-23.45):", math.frexp(-23.45))
# liefert Mantisse und Exponent als Tupel
# das ist die interne Repräsentation einer float (Dezimal) Zahl
# (-0.7328125 ist die Mantisse, 5 ist die Exponente)
print("identisch mit:", (-0.7328125 * 2 ** 5))
print("also:", math.frexp(-23.45)[0] * 2 ** math.frexp(-23.45)[1])
# not a number = NaN = float value
print("math.nan:", math.nan)
print("identisch mit flot(\"nan\"):", float("nan"))
#Eigenheiten
print("math.nan == math.nan:", math.nan == math.nan)
print("math.nan != math.nan:", math.nan != math.nan)
print("math.nan == math.nan:", math.nan == 7)
print("math.nan != math.nan:", math.nan != 7)
# Ist eine Zahl Nan?
print("math.isnan(7):", math.isnan(7))
print("math.isnan(math.nan):", math.isnan(math.nan))
# Quadratwurzel
print("math.sqrt(9):", math.sqrt(9))  #Quadratwurzel aus 9/Ergebnis liefert float
print("math.sqrt(10):", math.sqrt(10))  #Quadratwurzel aus 10/Ergebnis liefert float
print("math.isqrt(10):", math.isqrt(10))  #Quadratwurzel aus 10/Ergebnis liefert integer
print("math.pi:", math.pi)  # Pi

print("******************* Vergleichende Funktionen *******************")
print("eq(3, 3):", eq(3, 3))
print("gt(4, 5):", gt(4, 5))  # größer als

print("******************* Information *******************")
# Bei str kontrolle ob Text eine Zahl ist bzw ob Zahl auch wirklich Zahl ist
print("\"123\".isnumeric():", "123".isnumeric())
print("\"abc\".isnumeric():", "abc".isnumeric())
print("\"abc\".isalpha():", "abc".isalpha())
print("\"abc123\".isalpha():", "abc123".isalpha())
print("\"abc123\".isalnum():", "abc123".isalnum())
print("\"abc123\\n\".isalnum():", "abc123\n".isalnum())  # Steuerzeichen dabei

print("******************* Ein/Ausgabe *******************")

#  Eingaben
#eingabe = input("Bitte eine Zahl eingeben: ")  # Leerzeichen am Ende um die Eingabe zu vereinfachen
eingabe = "1234567"
print("Sie haben die Zahl " + eingabe + " eingegeben.")

# eine Datei zum schreiben öffnen!!

# r zum lesen und wird standardmässig ausgeführt
# w ist das schreiben bzw. überschreiben
# a ist Anhängen
# + (w+, r+, a+) um Datei lesen zu können und schreiben
# x erzeugen der Datei
# b Binär - Modus lesen und schreiben
# t text - Modus lesen und schreiben = Standard

# Datei wird geöffnet/Dateierweiterung anfügen
datei = open("test.txt", "w")  # Datei wird erstellt wenn noch nicht existiert, ansonsten überschrieben.
# In Datei schreiben
print("Sie haben die Zahl " + eingabe + " eingegeben.", file=datei)
# Datei schliessen
datei.close()

# Trennzeichen bei print ändern
print("etc", "Wien", sep="-")
# Endzeichen bei print ausschalten
print("Hallo ", end="")
print("Welt")

print("******************* Text *******************")
print("len(\"Python\"):", len("Python"))  # Länge eines Textes
print("ord(\"A\"):", ord("A"))  # - Unicode
print("chr(65):", chr(65))  # Gibt Buchstaben A zurück - Unicode
print("chr(65):", chr(8364))  # Gibt € zurück - Unicode
print("str.lower(\"Hallo Welt\"):", str.lower("Hallo Welt"))
print("\"Hallo Welt\".lower()):", "Hallo Welt!".lower())
print("str.upper(\"Hallo Welt\"):", str.upper("Hallo Welt"))
print("\"Hallo Welt\".upper()):", "Hallo Welt!".upper())
print("str.join(" ", [\"Hallo\", \"Welt\"]):", str.join(" ", ["Hallo", "Welt"]))
print("\" \".join([\"Hallo\", \"Welt\"]:", " ".join(["Hallo", "Welt"]))  #Verkettung mit Leerzeichen
print("\"Wir lernen heute Python\".split():", "Wir lerenen heute Python".split())  # Teilen von Text
print("\"Hallo\".replace(\"a\", \"e\":", "Hallo".replace("a", "e"))  # Ersetzen von Text
# Entfernen von Leerzeichen vor oder hinter Text
print("\"|\" + str.strip(\" Leerzeichen vorne und hinten entfernen \"):",
      "|" + str.strip(" Leerzeichen vorne und hinten entfernen ") + "|")

# Finden von Text
print("str.find(\"Peter Wolf\", " "):", str.find("Peter Wolf", " "))  # Suchen von leerzeichen als Bsp.
print("str.find(\"Peter Wolf\", \"e\"):", str.find("Peter Wolf", "e"))  # Suchen von e als Bsp.
print("str.count(\"Peter Wolf\", \"e\"):", str.count("Peter Wolf", "e"))  # Wie oft kommt e im Text vor

# slice notation
# [start:ende]              von Element Nummer start bis Element Nummer ende -1 (="MITTE)
# [start:start+anzahl]      Anzahl Zeichen ab dem Zeichen Nr start. Um thon aus Pythonkurs zu bekommen.
#                           Pythonkurs"[2:2 + 4] verwenden (Teil)
# [start:]                  alles ab Element Nummer start
# [:ende]                   alles bis Element Nummer ende -1 = ende Elemente von vorne oder links (="LINKS)
# [-start:]                 start Element von hinten oder rechts (="RECHTS)
# [:-ende]                  alles bis auf die letzten ende Elemente
# [:]                       alles

# Pythonkurs
# 0123456789
print("4 Zeichen ab dem Zeichen Nr 2. \"Pythonkurs\"[2:2 + 4]:", "Pythonkurs"[2:2 + 4])
print("Alles ab dem Zeichen Nr 6. \"Pythonkurs\"[6:]:", "Pythonkurs"[6:])
print("6 Zeichen von Links. \"Pythonkurs\"[:6]:", "Pythonkurs"[:6])
print("4 Zeichen von Rechts. \"Pythonkurs\"[-4:]:", "Pythonkurs"[-4:])
print("Alles bis auf dei letzen 4 Zeichen. \"Pythonkurs\"[:-4]:", "Pythonkurs"[:-4])
print("Alles! \"Pythonkurs\"[:]:", "Pythonkurs"[:])

print("******************* Datum und Uhrzeit *******************")
print("Heutiger Tag:", date.today())
print("Aktueller Tag und Uhrzeit:", datetime.now())
# Formatiert
print("Aktueller Tag und Uhrzeit mit Format Funktion, datetime.now():",
      format(datetime.now(), "%A %d.%m.%Y %H.%M:%S"))
print("Aktueller Tag und Uhrzeit mit Format Ersetzungsangabe, \"{:%A %d.%m.%Y %H.%M:%S}\".format(datetime.now():",
      "{:%A %d.%m.%Y %H.%M:%S}".format(datetime.now()))
print("Aktueller Tag und Uhrzeit formatiert mit f-string , \"{:%A %d.%m.%Y %H.%M:%S}\".format(datetime.now():",
      f"{datetime.now():%A %d.%m.%Y %H.%M:%S}")
print("Aktueller Tag und Uhrzeit formatiert mit strtime, datetime.now().strftime(\"%A %d.%m.%Y %H.%M:%S\") :",
      datetime.now().strftime("%A %d.%m.%Y %H.%M:%S"))

# Heutiger Wochentag
# Montag = 0
print("Heutiger Wochentag:", datetime.weekday(datetime.now()))
# Grenzen
print("Kleinstes Jahr:", date.min)
print("Größtes Jahr:", date.max)
#Heutiger Tag
print("Tag:, date.today().day", date.today().day)  # vom 27.08.2025 den 27ten Tag
print("Monat:, date.today().month", date.today().month)  # vom 27.08.2025 den 08 Monat
print("Year:, date.today().year", date.today().year)  # vom 27.08.2025 den 2025 Yahr
print("Stunde:, datetime.now().hour", datetime.now().hour)  # Stunde aus der Uhrzeit
print("Minute:, datetime.now().minute", datetime.now().minute)  # Minute aus der Uhrzeit
print("Sekunde:, datetime.now().second", datetime.now().second)  # Sekunde aus der Uhrzeit
print("Mikrosekunde:,datetime.now().microsecond", datetime.now().microsecond)  # Mikrosekunde aus der Uhrzeit
# Erstellen von Datum/Uhrzeit/Datum & Uhrzeit aus einzelnen Teilen:
print("Erstellen von Datum aus einzelnen Teilen:, date(day=1, month=1, year=2026)", date(day=1, month=1, year=2026))
print("time(hour=12, minute=20):", time(hour=12, minute=20))
print("datetime(day=1, month=1, year=2026, hour=12, minute=20:",
      datetime(day=1, month=1, year=2026, hour=12, minute=20))
print("Gestern:", date.today() - timedelta(days=1))  # Hier wird das gestrige Datum ermittelt
print("ASC Time:", asctime())

# Warten funktion
#sleep(10)  # Warten mit sleep 10 Sekunden

print("******************* range, reversed, sorted *******************")
# range erzeugt ein interierbares objekt
# range ([start, ] ende[, schrittweite])
# beginnt bei start (Standard ist 0/Wenn Start ausgelassen wird)
# endet vor (!) ende, in Schritten von schrittweite(Standard = 1)

for i in range(0, 11, 2):  #Start ist 0/Ende ist 11 und Schrittweite ist 2
    print("i:", i)

# kann umgekehrt und in Liste konvertiert werden.
print("list(reversed(range(0, 11, 2)):", list(reversed(range(0, 11, 2))))

# sortieren
print("sorted([7, 1, 4, 100, -3, 50]:", sorted([7, 1, 4, 100, -3, 50]))  # Aufsteigend sortiert
print("sorted([7, 1, 4, 100, -3, 50]:", list(reversed(sorted([7, 1, 4, 100, -3, 50]))))  #Absteigend sortiert

print("******************* Formatieren *******************")
# format(wert, formatspezifikation) eine Formatfunktion
# formatersetzungangabe.format(wert)

# Formatiert
print("Aktueller Tag und Uhrzeit mit Format Funktion, datetime.now():",
      format(datetime.now(), "%A %d.%m.%Y %H.%M:%S"))
print("Aktueller Tag und Uhrzeit mit Format Ersetzungsangabe, \"{:%A %d.%m.%Y %H.%M:%S}\".format(datetime.now():",
      "{:%A %d.%m.%Y %H.%M:%S}".format(datetime.now()))
print("Aktueller Tag und Uhrzeit formatiert mit f-string , \"{:%A %d.%m.%Y %H.%M:%S}\".format(datetime.now():",
      f"{datetime.now():%A %d.%m.%Y %H.%M:%S}")
print("Aktueller Tag und Uhrzeit formatiert mit strtime, datetime.now().strftime(\"%A %d.%m.%Y %H.%M:%S\") :",
      datetime.now().strftime("%A %d.%m.%Y %H.%M:%S"))

print("format(1234567, \"E\":", format(1234567, "E"))
# Nachkommastellen auf 2 reduzieren/Formatmethode:
print("format(12.34567, \".2f\") + \" €\":", format(12.34567, ".2f") + " €")
# Nachkommastellen auf 2 reduzieren/Formatersetzungangabe
print("format(12.34567, \".2f\") + \" €\":", "{:.2f}".format(12.34567) + " €")

print("format(12.34567, \"10.2f\") + \" €\":", format(12.34567, "10.2f") + " €")
print("Zifferngruppierung, \"{:,}\".format(12345670):", "{:,}".format(12345670))  # Zifferngruppierung
# Formatierung Dezimal/Binär/Hex

print("\"dec:{0:#d}, bin: {0:#b}, hex: {0:#x}\".format(182)):", "dec: {0:#d}", "bin: {0:#b}", "hex: {0:#x}".format(182))

# f - String
# Präfix f
print("f\"{12,34567:{5}.{4}} €\":", f"{12.34567:{5}.{4}} €")

person = "Hugo"
print("f\"Die Person hat den Namen {person!r}.\":", f"Die Person hat den Namen {person!r}.")
print("f\"Die Person hat den Namen {repr(person)}.\":", f"Die Person hat den Namen {repr(person)}.")

print("******************* Konvertierung Zahlensystem *******************")
print("bin(182):", bin(182))
print("hex(182):", hex(182))
print("str(0xb6):", str(0xb6))

print("******************* Datentyp, Objektnummer *******************")
print("type(\"etc\":", type("etc"))
print("id(\"etc\":", id("etc"))

print("******************* Python System *******************")
print("sys.version:", sys.version)
print("Alle Benennungen des Moduls sys:", dir(sys))

print("******************* Bestriebssystem *******************")
print("Umgebungsvariabel Path des OS:", os.environ["PATH"])

print("******************* pass *******************")
pass  # NULL operation, macht gar nix, wird benutzt als Platzhalter für zukünftigen Code, um Syntay zu erfüllen

print("******************* Evaluieren von Ausdrücken *******************")
# einen Ausdruck als str auswerten/ausrechnen

ausdruck = "2+3*4"
print("Ausrechnen der Variable ausdruck:", eval(ausdruck))

print("******************* exec *******************")
# Pythoncode als str ausführen

pythoncode = """
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("Das ist gefährlich wenn man keine Kontrolle über den str hat!")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
"""
exec(pythoncode)

# Anderes Script ausführen
exec(open("..\\anweisungenInTextzeilen.py").read())  # Script wird geöffnet und gestartet

# Anderes Programm starten, auf Terminierung warten (Administrator Recht?)
# Terminierung funktion nur für herkömmliche Desktop Anwendungen, keine neuen Windows Apps
# os.system("regedit.exe")  # Beispiel für herkömmliche Desktop Anwendung, hier wird der Code nicht beendet
# os.system("calc.exe")  # Beispiel für Windows App, bei Apps wird der Code beendet

# Anderes Programm starten, NICHT auf Terminierung warten (Administrator Recht?)
#Popen("regedit.exe")  # Beispiel für herkömmliche Desktop Anwendung, hier wird der Code nicht beendet
#Popen("calc.exe")  # Beispiel für Windows App, bei Apps wird der Code beendet

# Script beenden
sys.exit(0)

#print("Wird nicht mehr exekutiert....")
