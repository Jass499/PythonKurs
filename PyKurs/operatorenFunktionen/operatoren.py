"""
    Autor:      Jasmin Schmitt
    Datum:      26.08.2025
    Version:    1.0

    Operatoren und Rangordnung


"""

# Zuweisung
#  =
# Abkürzung
# a = a + b verkürzt a += b

a = 11
print("a = 11:", a)
a += 2
print("a += 2:", a)
a -= 2
print("a -= 2:", a)
a /= 2
print("a /= 2:", a)
a *= 2
print("a *= 2:", a)
a //= 2  # Ganzzahldivision
print("a //= 2:", a)
a %= 2  # Modulo = Rest der Ganzzahldivision
print("a %= 2:", a)
a = 3
print("a = 3:", a)
a **= 2
print("a **2:", a)

# Arithmetische Operatoren
print("(2*(3+4)-4)/5)", ((2 * (3 + 4) - 4) / 5))
# Objekte, auf die der + Operator angewendet werden kann, besitzen einen __add__() Methode
a = 2
print("a = 2, (a + 1)", (a + 1))
a = 2
print("a = 2, a.__add__(1)", (a.__add__(1)))
# + Operator ist überladen (Polymorphismus)
a = "abc"
print("a = \"abc\", (a +\"def\"):", (a + "def"))
a = "abc"
print("a = \"abc\", ((a.__add__(\"def\")):", (a.__add__("def")))

print("7/2", (7 / 2))
print("7//2", (7 // 2))
print("7%2", (7 % 2))

print("2 ** 8:", (2 ** 8))  # Potenz
print("9 ** 0.5:", (9 ** 0.5))  #Quadratwurzel

# Datentypen mischen scheitert
#print("\"etc\" + 3:", ("etc" + 3))

# Verlgeichende Operatoren
# == ist gleich
# < kleiner
# > größer
# <= kleiner oder gleich
# >= größer oder gleich
# != ungleich
# is, is not
# in, not in

# Logik
# False == (0 oder "")
# True != (0 oder "") / True == 1 == 5 == -3 == "abc"

print("(3 == 3):", (3 == 3))
print("(4>5):", (4 > 5))
print("\"A\" < \"a\"):", ("A" < "a"))
print("\"a\" < \"b\"):", ("a" < "b"))
print("\"abba\" < \"zeppelin\"):", ("abba" < "zeppelin"))

print("True and False:", (True and False))
print("True and not False:", (True and not False))
print("True or False:", (True or False))
print("True or not False:", (True or not False))


# Exklusives oder
# Anzahl der True ungerade -> True
def xor(str1, str2):
    return (str1 and not str2) or (not str1 and str2)


print("True or True:", (True or True))
print("xor(True, True):", xor(True, True))

# Objektvergleich
b = 3
c = 3
d = 4
print("b is c:", (b is c))
print("c is d:", (c is not d))

# Kollektionenvergleich
print("(\"all\" in \"Hallo Welt\"):", ("all" in "Hallo Welt"))
print("(\"Birne\" not in [\"Apfel\", \"Kirschen\", \"Banane\":", ("Birne" not in ["Apfel", "Kirschen", "Banane"]))
