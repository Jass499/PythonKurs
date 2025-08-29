"""
    Autor:      Jasmin Schmitt
    Datum:      29.08.2025
    Version:    1.0

    Windowsvorlage verwendet
    GUI mit Klasse TK aus Modul tkinter
"""

from tkinter import *

fenster = Tk()

fenster.geometry("300x100+700+300")  # gibt größe und Position an

fenster.title("Mein erstes Fenster")  #Titel

beschriftung = Label(fenster, text="Hallo Welt!")

beschriftung.pack()  # hier wird unser Label am Fenster in die Mitte platziert


def befehl():  # Befel um Fenster mit Schaltfläche zu schließen
    fenster.quit()


schaltflaeche = Button(fenster, text="OK", command=befehl)  # Schaltfläche wird erstellt und Befehl wird hinzugefügt
schaltflaeche.pack()

fenster.mainloop()  # Fenster wird gestartet
