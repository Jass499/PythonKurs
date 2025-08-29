"""
    Autor:      Jasmin Schmitt
    Datum:      28.08.2025
    Version:    1.0

    Dateien/Ordner mit Infos auflisten.


"""

from os import *  # listdir
from os.path import *  # isfile, isdir, getsize, exists

# Alles aus dem aktuellen Verzeichnis listen
print("****************** Dateien und Ordner im aktuellen Ordner ******************")
for dateiOrdner in listdir("."):  # listdir spricht mit "." den aktuellen Ordner an
    print(dateiOrdner, ("(Datei, " + str(getsize(dateiOrdner)) + " Bytes)") if isfile(dateiOrdner) else "(Ordner)")

# Alles aus dem übergeordneten Verzeichnis listen
print("****************** Alle Dateien und Ordner im übergeordneten Ordner ******************")
for dateiOrdner in listdir(".."):  # listdir spricht mit "." den aktuellen Ordner an
    print(dateiOrdner,
          ("(Datei, " + str(getsize("..\\" + dateiOrdner)) + " Bytes)") if isfile("..\\" + dateiOrdner) else "(Ordner)")

# Alles aus bestimmten Verzeichnis listen
print("****************** Datein und Ordner im Ordner c:\\windows ******************")
for dateiOrdner in listdir("c:\\windows"):  # listdir spricht mit "." den aktuellen Ordner an
    print(dateiOrdner,
          ("(Datei, " + str(getsize("c:\\windows\\" + dateiOrdner)) + " Bytes)")
          if isfile("c:\\windows\\" + dateiOrdner) else "(Ordner)")

# Alles aus bestimmten Verzeichnis listen
print("****************** Datein und Ordner im Ordner c:\\ ******************")
for dateiOrdner in listdir("c:\\"):  # listdir spricht mit "." den aktuellen Ordner an
    print(dateiOrdner,
          ("(Datei, " + str(getsize("c:\\" + dateiOrdner)) + " Bytes)")
          if isfile("c:\\" + dateiOrdner) else "(Ordner)")
