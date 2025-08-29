"""
    Autor:      Jasmin Schmitt
    Datum:      28.08.2025
    Version:    1.0

    Was ist ein Paket? = Ist eine Sammlung (Ordner) von (mit) Modulen und dieser Initialisierungsdatei.
    Beim Import des Pakets wird diese Initialsierungsdatei exekutiert.
    Hier steht also was importiert werden soll, wenn das Paket importiert wird.

"""

from meinPaket.meineDatumsfunktionen import *  # Pfad Angabe ist notwendig also Paket/dann Modul
from meinPaket.meineZufallsfunktionen import *  # Pfad Angabe ist notwendig also Paket/dann Modul

if __name__ != "__main__":
    print("Paket importiert, Initialisierungsdatei exekutiert!")
