"""
    Autor:      Jasmin Schmitt
    Datum:      29.08.2025
    Version:    1.0

    sqlite Datenbank Operationen

"""

from sqlite3 import connect

verbindung = connect("firma.db")

# DML Bereich
artikeltabelle = verbindung.execute("SELECT * FROM tblArtikel")

for datensatz in artikeltabelle:
    print(str(datensatz[0]) + "; " + datensatz[1] + "; " + str(datensatz[2]))

#verbindung.execute("INSERT INTO tblArtikel (ArtikelNr, ArtikelName, ArtikelLagerbestand)"
#                   "VALUES (900, \"Apfel\", 180)")

verbindung.execute("UPDATE tblArtikel SET ArtikelLagerbestand = 20 WHERE ArtikelNr = 900")

verbindung.execute("DELETE FROM tblArtikel WHERE ArtikelNr = 100")

verbindung.commit()

verbindung.close()  # Ende
