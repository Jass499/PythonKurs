"""
    Autor:      Jasmin Schmitt
    Datum:      26.08.2025
    Version:    1.0

    Selbstlaut: aeiuo

    Einggabe: Satz
    Ausgabe: Anzahl der Selbstlaute im Satz

    Plan:
    1.) Eingabe des Benutzers entgegen nehmen (Input) und in der Variable "satz" speichern -> liefert str
    2.) Zähler Variable "anzahl(int)" auf 0 initialisieren
    3.) Für jedes "zeichen(str)" im "satz(str)" (for Schleife)
        schaue ich, ob das "zeichen(str)" im String der "Selbstlaute(str)" aeiuoAEIOU vorkommt (if):
            -> Nein -> Gehe zum nächsten Schleifendurchgang mit continue
            -> Ja -> Inkrementieren (hochzählen) des Zählers Variable anzahl(int)
    4.) Ausgabe des Werts der Anzahl(int) in einem schönen Satz (print)


"""

satz = input("Bitte geben Sie einen Satz ein: ")
anzahl = 0

for zeichen in satz:
    if zeichen not in "aeiuoAEIOU":
        continue
    anzahl += 1

print("Der Satz", satz, " enthält ", anzahl, "Selbstlaute.")
