"""
    Autor:      Jasmin Schmitt
    Datum:      27.08.2025
    Version:    1.0

    Funktion Fakultät = Faktorielle (0!=1!=1)

    Bsp: 5! = 1*2*3*4*5

"""

zahl = int(input("Bitte eine ganze Zahl (0-999) eingeben: "))


# Iterative Lösung der Falkutät
def fak_it(n):  #Funktion durch def
    ergebnis = 1
    while n > 1:
        ergebnis = ergebnis * n
        n = n - 1
    return ergebnis


print("Die iterative Lösung der Fakultät von", zahl, "ist:", fak_it(zahl))


# Rekursive Lösung der Falkutät
# Rekrusion = sich selbst aufrufen
# Grosses Problem, wird in Teillösung gesplitet + Restproblem
# Restproblem genauso lösen wie großes Problem
# immer wieder
# Restproblem trivila lösbar

def fak_rek(n):  #Funktion durch def
    if n == 0 or n == 1:
        # Trivallösung
        return 1
    else:
        # Grosses Problem, wird in Teillösung gesplitet + Restproblem
        # Rekursion
        return n * fak_rek(n - 1)


print("Die rekursive Lösung der Fakultät von", zahl, "ist:", fak_rek(zahl))
