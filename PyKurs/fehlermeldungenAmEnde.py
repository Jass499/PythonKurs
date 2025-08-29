"""
    Autor:      Ihr Name
    Datum:      x.y.z
    Version:    1.0

    Workaround, damit Fehlermeldungen am Ende der Ausgabe stehen

"""

import time

# Originale print Funktion gegen eine eigene print Funktion tauschen, die nach dem print kurz wartet
add_sleep = lambda p: lambda *args, **kwargs: (p(*args, **kwargs), time.sleep(.01))[0]
# lange Variante
"""
def add_sleep(p):
    def new_p(*args, **kwargs):
        ret = p(*args, **kwargs)
        time.sleep(.01)
        return ret
    return new_p
"""

# Test mit und ohne dieser Zeile
print = add_sleep(print)

# Triviallösung, aber rote Farbe fehlt
#import sys
#sys.stderr = sys.stdout

print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
print("************************************************")
fehler = 2 / 0
