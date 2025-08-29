"""
    Autor:      Jasmin Schmitt
    Datum:      26.08.2025
    Version:    1.0

    Primzahl: Positive Ganzzahl, die nur duch 1 und sich selbst ganzzahlig teilbar ist

    Einggabe: Positive Ganzzahl
    Ausggabe: Ja ist Primzahl oder Nein keine Primzahl weil....(durch 2 Teilbar)

    Bsp.:
    Eingabe: 7
    7%2 != 0 -> könnte Primzahl sein
    7%3 != 0 -> könnte Primzahl sein
    nur bis 7//2 = 3, daher Primzahl

    Eingabe: 9
    9%2 != 0 -> könnte Primzahl sein
    9%3 == 0 -> JA -> keine Primzahl, weil 9=3*(9//3), Aufhören

    Plan:
    1.) Eingabe des Benutzers entgegen nehmen (Input), nach int konvertieren und in der Variable "zahl" speichern
        (Eine Kontrolle auf positive Ganze Zahl, findet nicht statt, wird aber den Benutzer mitgeteilt.)
    2.) Für jedes i(variable) Von 2 bis zahl//2 (for)
            probiere ich, ob zahl modulo i == 0 (if)
                -> Ja -> !keine Primzahl!, weil zahl=i*(zahl//i) ausgeben mit print, Aufhören (break)
            else:
                ohne Break wird eine Ausgabe mit Print erstellt ist eine Primzahl

"""

zahl = int(input("Bitte eine ganze, positive Zahl eingeben: "))

for i in range(2, zahl // 2):
    if zahl % i == 0:
        print(zahl, "==", i, "*", zahl // i, "und daher keine Primzahl.")
        break
else:
    print(zahl, " ist eine Primzahl.")
