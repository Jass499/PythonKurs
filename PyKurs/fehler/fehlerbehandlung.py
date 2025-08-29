"""
    Autor:      Jasmin Schmitt
    Datum:      28.08.2025
    Version:    1.0

    Fehlerbehandlung (Exceptions)

    try erfordert immer auch ein except und oder finally

"""

try:  # Versuche Anweisungsblock im Fehlerfall in den except Block springen und weiter arbeiten
    wert = 2 / 0
    # Wenn in try Block kein fehler auftritt, dann wird unter den except Block weiter gearbeitet
except:  # Nur in Fehlerfall wird dieser Anweisungsblock exekutiert und dann darunter weiter gearbeitet
    # ohne der konkretten exception Klasse kritisitert die IDE
    print("(1) Bei der Anweisung \"wert = 2 /0 \" ist ein Laufzeitfehler aufgetreten")

try:
    # pass  #                       kein Fehler
    wert = 2 / 0  #                 ein Bsp für Laufzeitfehler/ da Division durch 0
    # wert = eval("(4/2")  #        Das ist ein Syntaxfehler
    # wert = int("abc")  #          Datentypkonflikt
    # xyz()  #                      Name unbekannt
except SyntaxError:
    print("(2) Die Anweisung ist syntaktisch falsch!")
except ValueError:
    print("(2) Die Anweisung liefert einen Datentypkonflikt!")
except NameError:
    print("(2) Die Anweisung benützt einen unbekannten Namen!")
except:
    print("(2) Die Anweisung liefert einen anderen Fehler!")
else:  # Wird nur im NICHT Fehlerfall exekutiert und weiter gearbeitet
    print("(2) Die Anweisung liefert keinen Fehler!")
finally:  # Wird immer ausgeführt (auch wenn kein except und daher nach finally abgebrochen wird)
    print("(2) Ende des Try!")

# Diese Anweisungen stehen oft nach eigener Fehlerbehandlung am Ende des except
# Fehler selbst auslösen
#raise SyntaxError("Syntaxerror selbst ausgelöst!")
# Warnung selbst auslösen
#raise Warning("Warnung selbst ausgelöst!")

try:
    pass
    #wert = 2 / 0
finally:
    print("(3) kein except, daher wird beim Auftreten eines Fehlers im Try abgebrochen!")

print("Fertig!")
