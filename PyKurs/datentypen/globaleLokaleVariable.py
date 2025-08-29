"""
    Autor:      Jasmin Schmitt
    Datum:      26.08.2025
    Version:    1.0

    Gültigkeitsbereich = Scope = Namensraum = namespace

    Globale und Lokale Variable
    Globaler und Lokaler Namensraum

    Übergabe von Variablen ("Hauptprogramm" übergibt eine Variable an ein "Unterprogramm")

    Call by reference oder Call by value gibt es in Python nicht.
    Es werden Objekte übergeben (Call by object).
    Ob ein Unterprogramm im Hauptprogramm ein Objekt verändern kann, hängt vom Datentypen ab. (im/mutable)!

"""


# Unterprogramm
def unterprogramm(dd, ee):
    # auch dd und ee sind lokale Variable!
    # Schreibzugriff im globalen Namensraum scheitert
    # b += 20  # Ändern geht nicht
    # Setzen: Es wir eine neue lokael Variable b erzeugt = eine Namensgleichheit mit globalen Namensraum, bis ist hier
    # ein eigener Speicherplatz.
    b = 20  # Das ändert nicht den Wert der globalen Variable b!
    # Schreibzugriff auf globale Variable c schaffen
    global c
    c = 30  # Setzen: Das ändert den Wert der globalen Variable c!

    # eine Lokale int -> immutable Variable dd (Setzen/Ändern/Löschen einzeln testen)
    #dd = 40  # Setzen: Das ändern nicht den Wert der globalen Variable d
    dd += 40  # Ändern: Das ändern nicht den Wert der globalen Variable d
    #del dd  # Löschen: Das ändern nicht den Wert der globalen Variable d

    # eine Lokale list -> mutable Variable ee (Setzen/Ändern/Löschen einzeln testen)
    #ee = [50]  # Setzen: Das ändern nicht den Wert der globalen Variable e
    ee[0] = 100  # Ändern: Das ändert den Wert der globalen Variable e (!!!!) SEITENEFFEKT
    #del ee  # Löschen: Das ändern nicht den Wert der globalen Variable e

    print("*********** Unterprogramm ***********")
    print("Globale Variable a im Unterprogramm:", a)
    print("Lokale Variable b im Unterprogramm:", b)
    print("Globale Variable c im Unterprogramm:", c)
    print("Globale Variable d im Unterprogramm:", d)
    print("Globale Variable e im Unterprogramm:", e)
    print("Lokale Variable dd im Unterprogramm:", dd)
    print("Lokale Variable ee im Unterprogramm:", ee)

    print("*********** locals ***********")
    # Dictonary mit allen lokalen Referenzen des aktuellen Namenraums
    print("Lokaler Namensraum:\n", locals())  # auch mit vars() möglich
    print("*********** globals ***********")
    # Dictonary mit allen lokalen Referenzen des aktuellen Namenraums
    print("Globaler Namensraum:\n", globals())


# Hauptprogramm
# Hier ist der globale und lokale Namensraum identisch
# Globale Variable
a = 1
b = 2
c = 3
d = 4  #        int Datentyp = immutable
e = [5]  #      list Datenyp = mutable

print("*********** Hauptprogramm ***********")
print("Globale Variable a im Hauptprogramm:", a)
print("Globale Variable b im Hauptprogramm:", b)
print("Globale Variable c im Hauptprogramm:", c)
print("Globale Variable d im Hauptprogramm:", d)
print("Globale Variable e im Hauptprogramm:", e)
# dd, ee ist hier nicht verfügbar/sichtbar

unterprogramm(d, e)

print("*********** Hauptprogramm ***********")
print("Globale Variable a im Hauptprogramm:", a)
print("Globale Variable b im Hauptprogramm:", b)
print("Globale Variable c im Hauptprogramm:", c)
print("Globale Variable d im Hauptprogramm:", d)
print("Globale Variable e im Hauptprogramm:", e)
# dd, ee ist hier nicht verfügbar/sichtbar