"""
    Autor:      Jasmin Schmitt
    Datum:      25.08.2025
    Version:    1.0

    Integer Caching
    (String Interning)

    Implementierung CPython 3.10 (-5 .. 256, Objekte sind immer schon angelegt (Ganzzahlen))

    Cache ist ein Universalausdruck für schnellen Zwischenspeicher zur Performancesteigerung

"""
a = 256
b = 256
print(a is b)
# 1.) Test mit Script starten -> True
# 2.) Test mit interaktiver Eingaben in Python Shell -> True

a = 257
b = 257
print(a is b)
# 1.) Test mit Script starten -> True (Interpreter sieht das gesamte Script und optimiert)
# 2.) Test mit interaktiver Eingaben in Python Shell -> False (!)
