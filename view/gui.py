import tkinter as tk
class Vokabelview:
    def __init__(self,root):
        self.root = root
        #Titel
        self.root.title("")#Es gibt zunächst am Anfang kein Titel, weil es dann sich nach dem Anzeigen des deutschen Wortes ändern wird

        #Leinwand
        self.canvas = tk.Canvas(root, width = 200, height = 200)
        self.canvas.pack(pady=10)

        #Hintergrund
        self.canvas.create_rectangle(40,20,140,260,fill="beige")

        #Erstellt ein Textfeld für deutsches Wort
        self.wort_anzeige = self.canvas.create_text(90,100, text ="",font=("Arial",20))#Man erstellt quasin ein Feld für zukünftige deutsche Wörter, zuerst steht da nichts

        #Erstellt ein Eingabefeld für die englische Übersetzung
        self.eingabe = tk.Entry(root,width=50,font=("Arial",20)) # tk.Entry erstellt ein interaktives Eingabefeld
        self.eingabe.pack(pady=10)

        #Buttons
        self.button.skip =tk.Button(root, text = "Weiter")#Erstellt ein Button mit Text Weiter
        self.button.skip.pack(side=tk.LEFT,padx=20,pady=10)#Packt diesen Button quasi in ein Fenster und positioniert ihn Links der Leinwand

        self.button.check = tk.Button(root, text = "Prüfen")#Gleiche vorgehensweise wie mit erstem Button
        self.button.check.pack(side=tk.LEFT,padx=20,pady=10)


        #Counter Anzeige



#Methoden:


    # Anzeige deutsches Wort
    def zeige_wort(self,wort):#hier muss statt Wort etwas aus dem Model stehen
        self.canvas.itemconfig(self.wort_anzeige, text=wort)
        self.root.title(wort)

    #Hier werden noch weitere Methoden sein 



