"""
    Autor:      Jasmin Schmitt
    Datum:      26.08.2025
    Version:    1.0

    Datentypen umwandeln

"""

print("Ganzzahl 23 nach Dezimalzahl:", float(23))
print("Dezimalzahl 4.5 nach Ganzzahl:", int(4.5))

print("Ganzzahl 56 nach Zeichenketten und verketett mit \"78\":", str(56) + "78")
print("Zeichenketten \"78\" nach Ganzzahl und addiert mit 56:", int("78") + 56)

print("None nach Wahrheitswert:", bool(None))
print("() nach Wahrheitswert:", bool())
print("0 nach Wahrheitswert:", bool(0))
print("(1) nach Wahrheitswert:", bool(1))
print("(5) nach Wahrheitswert:", bool(5))
print("(-3) nach Wahrheitswert:", bool(-3))
print("(4.5) nach Wahrheitswert:", bool(4.5))
print("\"abc\" nach Wahrheitswert:", bool("abc"))
print("\"\" nach Wahrheitswert:", bool(""))

print("Wahrheitswert True nach Ganzzahl:", int(True))
print("Wahrheitswert False nach Ganzzahl:", int(False))

print("Sequenz nach Tupel:", tuple("Python"))
print("Sequenz nach Liste:", list("Python"))
print("Sequenz nach Menge:", set("Python"))
print("Liste von Paaren als Tupel nach Wörterbuch:", dict([(1, "a"), (2, "b"), (3, "c")]))

# Datenkonflikt
#print(int("abc"))
