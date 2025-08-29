"""
    Autor:      Jasmin Schmitt
    Datum:      25.08.2025
    Version:    1.0

    Datentypen in Python

    Daten werden durch Objekte dargestellt.
    Jedes Objekt hat
        - eine ID (Nummer)
        - einen Value (Wert)
        - eventuell eine Reference (Name)
        - einen Typ (Datentyp) (ergibt sich aus Wert -> dynamische Typisierung)

    Die Trivialdatentypen werden alle durch Literale (Buchstaben) dargestellt.

"""

print("***************** Zahlen *****************")
print("Ganzzahl (Integer, int):", 5, "Datentyp:", type(5), "ID:", id(5))
print("Ganzzahl dezimal(10 Ziffern, 0-9):", 10, "Datentyp:", type(10), "ID:", id(10))
print("Ganzzahl binär (2 Ziffern, 0-1):", 0b10, "Datentyp:", type(0b10), "ID:", id(0b10))
print("Ganzzahl hexadezimal (16 Ziffern, 0-9, A-F):", 0x10, "Datentyp:", type(0x10), "ID:", id(0x10))

print("Dezimalzahl (float):", 5.3, "Datentyp:", type(5.3), "ID:", id(5.3))  # Dezimaltrennzeichen ist ein Punkt
print("Dezimalzahl Exponentialschreibweise (float):", 7.8E3, "Datentyp:", type(7.8E3), "ID:", id(7.8E3))
print("Dezimalzahl Exponentialschreibweise (float):", 7.8E-3, "Datentyp:", type(7.8E-3), "ID:", id(7.8E-3))

print("***************** Kollektionen *****************")
# iterierbare Objekte (aus einzelnen Elemente)
print("************ Sequenzen ************")
print("****** unveränderliche Sequenzen ******")
print("** Strings **")
print("Zeichenkette (String, str ):", "ETC", "Datentyp:", type("ETC"), "ID:", id("ETC"))
print("Zeichenkette (String, str ):", 'ETC', "Datentyp:", type('ETC'), "ID:", id('ETC'))
print("Wir sind bei 'etc' Python lernen.")
print('Wir sind bei "etc" Python lernen.')
print("Wir sind bei \"etc\" Python lernen.")
print('Wir sind bei \'etc\' Python lernen.')
# Escape Sequenze
#   \n          Zeilenumbruch
#   \t          Tabulator
#   \"          auszugebendes Anführungszeichen
#   \'          auszugebendes einfaches Anführungszeichen
#   \\          auszugebender Backslash Bsp. Pfad
#   \u03A9      16Bit = 2 Byte=4Hexbuchstaben Unicode Zeichen (Omega)
print("Zeichenkette mit Escape Sequenz:", "Wir sind \n\tbei etc\nPython lernen.")
print("Zeichenkette mit Escape Sequenz:", "Pfad zu Pakete: C:\\Python313\\Lib\\site-packages")
print("Zeichenkette mit Escape Sequenz:", "Unicode: \u03A9")

print("** Tuple **")
#unveränderliche Sammlung auch unterschiedlicher Informationen/Duplikate sind erlaubt
print("Tupel (tuple ):", ("abc", 7, 5.3), "Datentyp:", type(("abc", 7, 5.3)), "ID:", id(("abc", 7, 5.3)))

print("****** veränderliche Sequenzen ******")
print("** Liste **")
#veränderliche Sammlung auch unterschiedlicher Informationen/Duplikate sind erlaubt
meineliste = ["abc", 7, 5.3]
pass
meineliste.append(100)
print("Liste (list):", meineliste, "Datentyp:", type(meineliste), "ID:", id(meineliste))

# Operationen mit Sequenzen
# Auswahl eines Elementes erfolgt immer mit eckiger Klammer (Indexing, auch bei tuple und string)
# Nummerierung beginnt immer bei 0
print("2. Element (hat die Nummer 1) der Liste:", meineliste[1])

meintupel = tuple(meineliste)
print("4. Element (hat die Nummer 3) der Liste:", meintupel[3])

# Python
# 012345
#-654321
print("Vorletzer Buchstabe des Strings 'Python':", "Python"[4], "Python"[-2])

# Merge
meineliste = meineliste + ["def", 50]
meineliste += [20]
print("Liste " + "(list):", meineliste, "Datentyp:", type(meineliste), "ID:", id(meineliste))

# Vervielfältigen einer Sequence
print(3 * "Hoch! ")

#Länge einer Sequence
print("Länge des Worte Python:", len("Python"))
print("Anzahl der Elemente der Liste:", len(meineliste))
print("Anzahl der Elemente des Tupel:", len(meintupel))

# slice notation
# [start:ende]              von Element Nummer start bis Element Nummer ende -1 (="MITTE)
# [start:]                  alles ab Element Nummer start
# [:ende]                   alles bis Element Nummer ende -1 = ende Elemente von vorne oder links (="LINKS)
# [-start:]                 start Element von hinten oder rechts (="RECHTS)
# [:-ende]                  alles bis auf die letzten ende Elemente
# [:]                       alles

print("Liste:", meineliste)
print("Von Elemente Nr 2 bis Element Nr 5-1:", meineliste[2:5])
print("Alles ab Elemente Nr 3:", meineliste[3:])
print("4 Elemente von links:", meineliste[:4])
print("3 Elemente von rechts:", meineliste[-3:])
print("Alles bis auf die letzten 2 Elemente:", meineliste[:-2])
print("Alles:", meineliste[:])

#  Operationen mit Listen
# An bestimmer Position einfügen (position, element was eingefügt wird)
meineliste.insert(1, 200)
print("Liste:", meineliste)

# Minimum und Maximum
print("Minuimum der Liste:", min([7, -3, 50]))
print("Maximum der Liste:", max([7, -3, 50]))

# Element suchen und duplikate
# Position des ersten Vorkommnisses eines Elements finden
# Mit Index kann ein Wert gefunden werden
meineliste.append(100)
print("Liste:", meineliste)
print("Position des ersten Elements mit den Wert 100 in Liste finden:", meineliste.index(100))
# Anzahl der Vorkommnise
print("Anzahl der Elemente mit den Wert 100 in Liste ausgeben:", meineliste.count(100))
print("Anzahl der Elemente mit den Wert 500 in Liste ausgeben:", meineliste.count(500))

# Erstes Vorkommnis eines Elementes löschen (scheitert falls nicht vorhanden)
meineliste.remove(100)
print("Liste:", meineliste)

# Löschen eines bestimmten Elements, löschen des Elements mit Nummer 2
del meineliste[2]
print("Liste:", meineliste)

# Sortieren von Zahlen
meineliste = [-5, 100, 7, -10, 20, 30, 5.3]
print("Liste unsortiert:", meineliste)
meineliste.sort()
print("Liste sortiert:", meineliste)

meineliste.reverse()
print("Liste umgekehrt sortiert:", meineliste)

print("************ Mengen ************")
# Eine Menge hat keine Ordnung, d.h. ich kann nicht sagen gib mir das zweite Element
print("****** veränderliche Menge ******")
#veränderliche Sammlung auch unterschiedlicher Informationen/es gibt keine Duplikate
meinemenge = {"abc", 5, 6, 7, 5}
print("Menge (set):", meinemenge, "Datentyp:", type(meinemenge), "ID:", id(meinemenge))
meinemenge.add(2)
print("Menge (set):", meinemenge, "Datentyp:", type(meinemenge), "ID:", id(meinemenge))
print("****** unveränderliche Menge ******")
#unveränderliche Sammlung auch unterschiedlicher Informationen/es gibt keine Duplikate
meinefixemenge = frozenset(meinemenge)
print("Unveränderliche Menge (frozenset):", meinefixemenge, "Datentyp:", type(meinefixemenge),
      "ID:", id(meinefixemenge))

print("************ Abbildungen, Wörterbücher ************")
# Paare der Form Schlüssel:wert
woertbuch = {"sun": "Sonne", "moon": "Mond", "star": "Stern"}
print("Übersetzung von \"moon\" aus Wörterbuch, dictonary (dict):", woertbuch["moon"],
      "Datentyp:", type(woertbuch), "ID:", id(woertbuch))

print("***************** Wahrheitswert oder boolean *****************")
print("Wahrheitswert WAHR (bool):", True, "Datentyp:", type(True), "ID:", id(True))
print("Wahrheitswert FALSCH (bool):", False, "Datentyp:", type(False), "ID:", id(False))

print("***************** NoneType Kein Wert *****************")
# None ~ Nichts ~ Leer ~ Nicht ausgefüllt ~ Unbekannt <> 0 <> ""(Text der Länge 0) <> NULL
print("Kein Wert (NoneType):", None, "Datentyp:", type(None), "ID:", id(None))
