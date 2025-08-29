"""
    Autor:      Jasmin Schmitt
    Datum:      27.08.2025
    Version:    1.0

    Verzweigungen

"""

#eingabe = int(input("Bitte geben Sie eine ganze Zahl zwischen 0 -100 ein: "))
eingabe = 20

print("******************* Einseitige, einfache Verzweigung  *******************")
if eingabe >= 50:
    print("Die Eingabe", eingabe, "war in der oberene Hälfte.")

print("******************* Zweiseitig, einfache Verzweigung  *******************")
if eingabe < 50:
    print("Die Eingabe", eingabe, "war in der unteren Hälfte.")
else:
    print("Die Eingabe", eingabe, "war in der oberene Hälfte.")

print("******************* Mehfrache, geschachtelt zweiseitige Verzweigung  *******************")
if eingabe < 33:
    print("Die Eingabe", eingabe, "war im ersten Drittel.")
else:
    if eingabe < 66:
        print("Die Eingabe", eingabe, "war im zweiten Drittel.")
    else:
        print("Die Eingabe", eingabe, "war im dritten Drittel.")

if eingabe < 25:
    print("Die Eingabe", eingabe, "war im ersten Viertel.")
else:
    if eingabe < 50:
        print("Die Eingabe", eingabe, "war im zweiten Viertel.")
    else:
        if eingabe < 75:
            print("Die Eingabe", eingabe, "war im dritten Viertel.")
        else:
            print("Die Eingabe", eingabe, "war im viertel Viertel.")

print("******************* Mehfrach Verzweigung  *******************")
if eingabe < 33:
    print("Die Eingabe", eingabe, "war im ersten Drittel.")
elif eingabe < 66:
    print("Die Eingabe", eingabe, "war im zweiten Drittel.")
else:
    print("Die Eingabe", eingabe, "war im dritten Drittel.")

if eingabe < 25:
    print("Die Eingabe", eingabe, "war im ersten Viertel.")
elif eingabe < 50:
    print("Die Eingabe", eingabe, "war im zweiten Viertel.")
elif eingabe < 75:
    print("Die Eingabe", eingabe, "war im dritten Viertel.")
else:
    print("Die Eingabe", eingabe, "war im viertel Viertel.")

print("******************* Bedingter Ausdruck  *******************")
# dannwert if bedingung else sonstwert
# else ist nicht optional
print("Die Eingabe war in der ersten Hälfte." if eingabe < 50 else "Die Eingabe war in der zweiten Hälfte.")

print("******************* ab Python 3.1 gibt es ein match/case *******************")
match eingabe:
    case 0:
        print("Die Eingabe war 0.")
    case 40 | 60:
        print("Die Eingabe war 40 oder 60.")
    case eingabe if eingabe > 80:
        print("Die Eingabe war größer 80.")
    case _:  # else
        print("Die Eingabe", eingabe, "war nicht 0,40, 60 oder größer 80.")
