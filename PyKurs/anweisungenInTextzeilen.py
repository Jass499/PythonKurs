"""
    Autor:      Jasmin Schmitt
    Datum:      25.08.2025
    Version:    1.0

    Verhältnis von Anweisung zu Textzeile

"""

# Eine Anweisung pro Textzeile
x = 10
print("x:", x)

# Zwei Anweisung in einer Textzeile (bitte nicht!)
#y = 20; print("y:", y)

# Explizit verbinden
a = 1 + \
    2  #            Kommentar nur hier möglich!
print("a:", a)

# Impliziert verbinden
b = (3 +  # Kommentar auch hier möglich
     4)
print("b:", b)
