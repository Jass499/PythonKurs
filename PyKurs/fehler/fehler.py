"""
    Autor:      Jasmin Schmitt
    Datum:      25.08.2025
    Version:    1.0

    Typen von Fehler

"""

# Syntaxfehler (Schreibweise)
#a = 2 * (3 + 4))       zu viele Klammern

# Laufzeitfehler
# b = 5/0               / durch 0 nicht möglich

# Semantikfehler (Bedeutung)
c = 6
C = 7
print("Das kleine c hat den Wert: ", C)  # hier wird die falsche Variable verwendet, deswegen ohne Fehlermeldung

# Einrückungsfehler (Indent)
d = 8
if d == 8:
    #pass  # Kann verwendet werden um in den Fall den If Block zu umgehen. Kann während der Entwickelt verwendet werden.
    print("Falscher Indent?!")  # Wenn Einrückung zu klein oder zu groß ist.
    #print("Falscher Indent?!")  # Wenn Einrückung zu klein oder zu groß ist.
