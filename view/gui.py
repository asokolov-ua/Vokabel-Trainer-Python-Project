

import tkinter as tk
class Vokabelview:
    def __init__(self,root):
        self.root = root
        #Titel
        self.root.title("")#Es gibt zunächst am Anfang kein Titel, weil es dann sich nach dem Anzeigen des deutschen Wortes ändern wird

        #Leinwand
        self.canvas = tk.Canvas(root, width = 350, height = 350, bg = "lightblue")#bg ist ein Attribut für background von unserer Leinwand
        self.canvas.pack(pady=10)

        #Hintergrund(Rahmen für das deutsche Wort), hier habe ich mir einer alternativen Polygon Funktion von Tkinter versucht
        form = [
            85, 20,  # Oben links Start
            265, 20,  # Oben rechts Start
            275, 30,  # Oben rechts Ende
            275, 210,  # Unten rechts Start
            265, 220,  # Unten rechts Ende
            85, 220,  # Unten links Start
            75, 210,  # Unten links Ende
            75, 30  # Oben links Ende
        ]

        self.canvas.create_polygon(form,fill="beige",outline="black",width=2, smooth=True)#Kanten runden mit smooth


        #Erstellt ein Textfeld für deutsches Wort
        self.wort_anzeige = self.canvas.create_text(175,120, text ="",font=("Arial",24))#Man erstellt quasi ein Feld für zukünftige deutsche Wörter, zuerst steht da nichts

        #Erstellt ein Eingabefeld für die englische Übersetzung
        self.eingabe = tk.Entry(root,width=25,font=("Arial",20), bg="whitesmoke",bd=2) # tk.Entry erstellt ein interaktives Eingabefeld, bd ist ein attribut für borderwidth
        self.eingabe.pack(pady=20)

        #Buttons im Rahmen
        self.button_rahmen = tk.Frame(root)
        self.button_rahmen.pack(pady=10)

        self.button_skip =tk.Button(self.button_rahmen, text = "Weiter")#Erstellt ein Button mit Text Weiter im Rahmen
        self.button_skip.pack(side=tk.LEFT,padx=10)#Packt diesen Button quasi in ein Fenster und positioniert ihn Links des Rahmens

        self.button_check = tk.Button(self.button_rahmen, text = "Prüfen")#Gleiche vorgehensweise wie mit erstem Button
        self.button_check.pack(side=tk.RIGHT,padx=10)


        #Counter Anzeige
        self.counter_anzeige = self.canvas.create_text(175,260,text="Richtig beantwortet: 0",font=("Arial",12))



#Methoden:


    # Anzeige deutsches Wort
    def zeige_wort(self,wort):#hier muss statt Wort etwas aus dem Model stehen
        self.canvas.itemconfig(self.wort_anzeige, text=wort)
        self.root.title(wort)

    #Methode, die Counter aktualisiert
    def counter_aktualisieren(self,stand): #Statt stand muss etwas sein, damit es sich immer erneut, im Controller vielleicht
        self.canvas.itemconfig(self.counter_anzeige, text=f"Richtig beantwortet: {stand}")

    #Die nächsten beiden Methoden sind für den Austausch mit Controller wichtig. Die werden im Controller benutzt
    def get_eingabe(self):
        return self.eingabe.get()

    def loesche_eingabe(self):
        self.eingabe.delete(0, tk.END)


   #Als nächstes ändere ich die Abtrennung des Eingabefeldes von dem da unten





        # Test
if __name__ == "__main__":
    root = tk.Tk()# Erstellt das hauptfenster unserer app, darauf wird alles aufgebaut
    view = Vokabelview(root)
    view.zeige_wort("Apfel")


    root.mainloop()


