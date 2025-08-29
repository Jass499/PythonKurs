"""
    Autor:      Jasmin Schmitt
    Datum:      27.08.2025
    Version:    1.0

    Schleifen

"""

print("******************* Bedingungsgesteurte Schleife MIN=0 *******************")
#eingabe = input("(1) Bitte geben Sie eine ganze Zahl zwischen 0 und 100 ein: ")
eingabe = "50"
#while not (eingabe.isnumeric() and int(eingabe) >= 0 and int(eingabe) <= 100):

while not eingabe.isnumeric() or int(eingabe) < 0 or int(eingabe) > 100:
    eingabe = input("(1) Bitte geben Sie eine ganze Zahl zwischen 0 und 100 ein: ")
else:
    print("(1) Es wurde die Zahl", int(eingabe), "eingegeben.")

print("******************* Endlos Schleife mit break und countinue *******************")
while True:  # True .. Endlosschleife, False .. Block 0 mal
    # eingabe = input("(2) Bitte geben Sie eine ganze Zahl zwischen 0 und 100 ein: ")
    if eingabe.isnumeric() and 0 <= int(eingabe) <= 100:
        break  # break springt aus der Schleife, unter else von while
    else:
        continue  # continue springt zum nächsten Schleifendurchlauf ohne den aktuellen fertigzustellen
    # print("Toter Code....")
# else:  # wird nur ausgeführt wenn kein break
#   print("Toter Code....?")

print("(2) Es wurde die Zahl", int(eingabe), "eingegeben.")

print("******************* Zählergesteuerte Schleife *******************")
print("Kollektion ist str:")
for i in "Python":
    print(i, end=" ")

print("\nKollektion ist tuple:")
for i in ("rot", "gelb", "grün"):
    print(i, end=" ")

print("\nKollektion ist list:")
for i in [4, 1, 5, 3, 1]:
    print(i, end=" ")

print("\nKollektion ist ein set:")
for i in {4, 1, 5, 3, 1}:
    print(i, end=" ")

print("\nKollektion ist ein set:")
for i in {4, 1, 5, 3, 1}:
    print(i, end=" ")

print("******************* range, reversed, sorted *******************")
# range erzeugt ein interierbares objekt
# range ([start, ] ende[, schrittweite])
# beginnt bei start (Standard ist 0/Wenn Start ausgelassen wird)
# endet vor (!) ende, in Schritten von schrittweite(Standard = 1)

print("\nKollektion über range Funktion:")
for i in range(0, 11, 2):  #Start ist 0/Ende ist 11 und Schrittweite ist 2
    print(i, end=" ")

print("\nKollektion über range Funktion, hochzählen ohne Ausgabe:")
for i in range(1000000):
    pass
    #print(i, end=" ")
print("\nKollektion über range Funktion, hochzählen ohne Ausgabe:")
for i in range(1000000):
    print(i, end=chr(13))  # CR
