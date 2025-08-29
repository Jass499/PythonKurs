"""
    Autor:      Jasmin Schmitt
    Datum:      26.08.2025
    Version:    1.0

    Selbstlaut: aeiuo

    Einggabe: Satz
    Ausgabe: Anzahl der Selbstlaute im Satz

"""

text = "Hallo Welt!"
vokale = "aeiuo"
counts = {v:0 for v in vokale}

for char in text.lower():
    if char in counts:
        counts[char] += 1

print("Vokal-Zählung:", counts)


