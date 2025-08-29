"""
    Autor:      Robert Panzirsch
    Datum:      x.x.20xx
    Version:    1.0

    GUI mit Klasse Tk aus Modul tkinter (Interface zum Toolkit)

"""

from tkinter import Tk, Menu, Label, Entry, Radiobutton, StringVar, Checkbutton, IntVar, Button
from tkinter import Listbox, END, ACTIVE, messagebox

fenster = Tk()
# Fenster Objekt aus Klasse Tk instanzieren

fenster.geometry("510x200+100+100")
# Größe und Position von der linken oberen Ecke aller Bildschirme einstellen in px: BREITExHÖHE+X+Y

fenster.title("Programmfenster")  # Titel einstellen


# Menü
def menueeintragarbeit():
    """ Funktion für Menüeintrag Arbeit """
    messagebox.showinfo(title="Arbeit", message="Arbeit ...")


def menueeintraginfo():
    """ Funktion für Menüeintrag Info """
    messagebox.showinfo(title="Info", message="Copyright Wifi Wien")


menue = Menu(fenster)
# Menü Objekt aus Klasse Menu instanzieren
dateimenue = Menu(menue, tearoff=0)
# Dateimenü Objekt aus Klasse Menu instanzieren
# keine strichlierte Trennlinie
hilfemenue = Menu(menue, tearoff=0)
# Hilfemenü Objekt aus Klasse Menu instanzieren
# keine strichlierte Trennlinie
dateimenue.add_command(label="Arbeit", command=menueeintragarbeit)
# Befehl in Menü Datei
dateimenue.add_separator()
# Trennlinie
dateimenue.add_command(label="Exit", command=fenster.quit)
# Befehl in Menü Datei
hilfemenue.add_command(label="Info", command=menueeintraginfo)
# Befehl in Menü Hilfe
menue.add_cascade(label="Datei", menu=dateimenue)
# Dropdown Menü Datei einrichten
menue.add_cascade(label="Hilfe", menu=hilfemenue)
# Dropdown Menü Hilfe einrichten
fenster.config(menu=menue)
# Menü in Fenster einrichten

# Beschriftungen
beschriftungname = Label(fenster, text="Name:")
#beschriftungname.grid(row=0, column=0, padx=10, pady=10)
# Gridmanager, Tabellenraster
beschriftungname.place(x=10, y=10, width=50, height=20)
# Placemanager
beschriftungpasswort = Label(fenster, text="Passwort:")
beschriftungpasswort.place(x=10, y=50, width=50, height=20)

# Textfeld
textfeldname = Entry(fenster)
textfeldname.place(x=80, y=10, width=100, height=20)
textfeldpasswort = Entry(fenster, show="*")
textfeldpasswort.place(x=80, y=50, width=100, height=20)

# Optionsfeld
anrede = StringVar()
# hält die Wahl der Optionsfelder
optionsfeldfrau = Radiobutton(fenster, text="Frau", value="Frau", variable=anrede, tristatevalue=0)
optionsfeldfrau.place(x=200, y=10, width=100, height=20)
optionsfeldherr = Radiobutton(fenster, text="Herr", value="Herr", variable=anrede, tristatevalue=0)
optionsfeldherr.place(x=200, y=50, width=100, height=20)

# Kontrollkästchen
wichtig = IntVar()
# Hält die Wahl des Kontrollkästchens
kontrollkaestchenwichtig = Checkbutton(fenster, text="Wichtig", variable=wichtig)
kontrollkaestchenwichtig.place(x=300, y=10, width=100, height=20)

# Listenfeld
listenfeldobst = Listbox(fenster, selectmode="browse")
listenfeldobst.insert(END, "Apfel", "Birne", "Kirsche", "Banane")
listenfeldobst.activate(0)
# erstes Element auswählen, damit beim Zugriff ohne Benutzerwahl kein Fehler auftritt
listenfeldobst.select_set(0)
# und dieses blau markieren
listenfeldobst.place(x=400, y=10, width=100, height=100)


# Schaltflächen
def befehlok():
    messagebox.showinfo(message="Tschüss ...")
    fenster.quit()


schaltflaecheok = Button(fenster, text="OK", command=befehlok)
schaltflaecheok.place(x=400, y=140, width=100, height=50)


def befehlauswertung():
    auswertung = (
            "Name: " + textfeldname.get() +
            "\nPasswort: " + textfeldpasswort.get() +
            "\nAnrede: " + anrede.get() +
            "\nWichtig: " + str(wichtig.get()) +
            "\nListe: " + str(listenfeldobst.get(first=ACTIVE))
    )
    messagebox.showinfo(title="Auswertung", message=auswertung)


schaltflaecheauswertung = Button(fenster, text="Auswertung", command=befehlauswertung)
schaltflaecheauswertung.place(x=250, y=140, width=100, height=50)

fenster.mainloop()
# anzeigen und Hauptroutine starten
