"""

    Dies ist ein mehrzeiliges , unbenanntes Textobjekt, verwendet ganz oben im Script verwendt als docstring

    Grundlagen im Code

    Syntax = Schreibweise

    Metasymole
        <..>        inklusive Klammern durch sinnvolles ersetzen
        [..]        optionale Angabe
        {..|..}     verpflichtende Auswahl


    - Je Textzeile eine Anweisung
    (- Sonst einen ; zwischen mehreren Anweisungen einer Textzeile setzen)
    - Anweisung über mehrere Textzeilen: Am Ende ein Backslash anhängen
        oder geklammerte Ausdrücke (..) [..] {..}

    Benennungen:
        - muss mit Alphabuchstabe beginnen [a-z][A-Z][_] (keine Umlaute und kein ß verwenden!)
        - danach sind auch Ziffern möglich [0-9] Bsp "Zahl1" (1Zahl ist nicht erlaubt)
        - keine Schlüsselwörter verwenden
    Case Sensitiv! (Groß und Kleinschreibung ist entscheidend!)

    Namenskonventionen:
        - Variablen, Funktionen, Methoden, Datei, Ordner: sollen mit kleinbuchstaben beginnen
            -> lower (lowerCamelCase)
        - Klassen: sollen mit Großbuchstaben beginnen
            -> UpperCamelCase (UPPER)

    - ein : leitet im Python einen Block ein, danach muss mindestens eine Zeile eingerückt sein

    Text in einfache oder doppetet Anfürhungszeichen einschließen.
    Mehrzeiligen Text in 3 in einfache oder doppetet Anfürhungszeichen einschließen.
    Bitte einfache oder doppetet Anfürhungszeichen nicht wild oder ohne Grund mischen.

    Es gibt keinen mehrzeiligen Kommentar.
    Es gibt nur den einzeiligen Kommentar ab dem Doppelkreuz bis Zeilenende.
    ****************************

    Dateierweiterungen:
    py      Standard Python Script
    pyw     GUI Python Script
    pyi     Interface (Schnittstellen) Definitionsdatei
    pyc     Python Byte Code
                py -Compiler-> pyc - Interpreter-> binär Information konventiert
"""

name = input("Name: ")  #               Eingabe(Input)
gruss = "Hallo " + name + "!"  #        Verarbeitung
print(gruss)  #                         Ausgabe (Output)
