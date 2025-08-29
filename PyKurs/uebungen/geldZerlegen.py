"""
    Autor:      Jasmin Schmitt
    Datum:      26.08.2025
    Version:    1.0

    Eingabe: Einen Geldbetrag in Euro (mit Cent) (float)
            Bsp: 768(.76)
    Ausgabe: Stückelung in Scheinen und Münzen
    Bsp: 1*500+1*200+0*100+1*50+0*20+1*10+1*5+1*2+1*1+1*0.50+1*0.20+0*0.10+1*0.05+0*0.002+1*0.01

"""

eingabe = input("Geben Sie einen Geldbetrag in Euro ein: ")
geld = float(eingabe)
euro = int(geld)  # Ganze Euro
# cent = int((geld - euro) * 100)  # Rundungsfehler
cent = int(geld * 100 - euro * 100)  # Besser

for i in [500, 200, 100, 50, 20, 10, 5, 2, 1]:
    print(euro // i, "mal", i, "Euro")
    euro = euro % i

for i in [50, 20, 10, 5, 2, 1]:
    print(cent // i, "mal", i, "Cent")
    cent = cent % i
