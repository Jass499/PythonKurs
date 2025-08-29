"""
    Autor:      Jasmin Schmitt
    Datum:      28.08.2025
    Version:    1.0

    Context Manager: with

    Das with erzeugt eine Block von Statments.

    Vor der Ausführung des Blocks erfolgt eine Initialisierung durch einen Aufruf von __enter__()
    Nachder Beendigung des Blocks erfolgt eine Bereinigung durch Aufruf __exit__()

    Das with Statment kann statt einen try/finally Block verwendet werden.

    Es dient zu:
        - Lock/Unlock von Ressourcen
        - Open/Close von Ressourcen
        - Commit/Rollback von Transaktionen
        - Zeitmessung

"""


# Muster
class MeinManager:
    def __init__(self, dateiname, modus):
        self.dateiname = dateiname
        self.modus = modus
        self.datei = None

    def __enter__(self):
        self.datei = open(self.dateiname, self.modus)
        return self.datei

    def __exit__(self):
        self.datei.close()


# ohne with
datei = open("musterdatei.txt", "w")
try:
    datei.write("Hallo!\n")
finally:
    datei.close()

# mit with
with open("musterdatei.txt", "a") as datei:
    datei.write("Hallo mit With!\n")

# Will man Exceptions abfangen
try:
    datei = open("musterdatei.txt", "a")
except FileNotFoundError:
    print("Datei nicht gefunden!")
else:
    with datei:
        datei.write("Hallo!\n")
