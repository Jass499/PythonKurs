"""
    Autor:      Jasmin Schmitt
    Datum:      26.08.2025
    Version:    1.0

    Selbstlaut: aeiuo

    Einggabe: Satz
    Ausgabe: Anzahl der Selbstlaute im Satz

"""

text = "Hallo Welt!"
a_count = e_count = i_count = u_count = o_count = 0

for char in text.lower():
    if char == "a":
        a_count += 1
    elif char == "e":
        e_count += 1
    elif char == "i":
        i_count += 1
    elif char == "u":
        u_count += 1
    elif char == "o":
        o_count += 1

print("A:", a_count, "E:", e_count, "I:", i_count, "U:", u_count, "O:", o_count)

