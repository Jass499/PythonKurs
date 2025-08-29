"""
    Autor:      Jasmin Schmitt
    Datum:      26.08.2025
    Version:    1.0

    Eine Variable ist ein Speicherplatz in Hauptspeicher/Arbeitsspeicher oder auch RAM
    mit reference (Name, Zeiger, Pointer) und einem zur Laufzeit veränderlichem value (Wert).

    In Python ist auche eine Variable ein Objekt, hat
        - eine ID (Nummer)
        - einen Value (Wert)
        - eventuell eine Reference (Name)
        - einen Typ (Datentyp) (ergibt sich aus Wert -> dynamische Typisierung)

    Python hat keine Konstante.
    Eine Konstante ist ein Speicherplatz in Hauptspeicher/Arbeitsspeicher oder auch RAM
    mit reference (Name, Zeiger, Pointer) und einem zur Laufzeit unveränderlichem value (Wert).

"""

import ctypes

a = "Hallo Welt"

print("ID der Variable:", id(a))
print("Datentyp der Variable:", type(a))
print("Wert der Variable über Name:", a)
print("Wert der Variable über Name:", ctypes.cast(id(a), ctypes.py_object).value)  #Über ID Wert auslesen
