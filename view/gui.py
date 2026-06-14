import tkinter as tk

class VokabelView:
    def __init__(self, root):
        self.root = root
        # Titel wird initial leer gelassen, wie im aktuellen Code
        self.root.title("Vokabeltrainer")

        # Leinwand (Canvas) - wie bisher in lightblue
        self.canvas = tk.Canvas(root, width=350, height=350, bg="lightblue")
        self.canvas.pack(pady=10)

        # Hintergrund (Karteikarte mit Polygon-Funktion und abgerundeten Kanten)
        form = [
            85, 20,   # Oben links Start
            265, 20,  # Oben rechts Start
            275, 30,  # Oben rechts Ende
            275, 210, # Unten rechts Start
            265, 220, # Unten rechts Ende
            85, 220,  # Unten links Start
            75, 210,  # Unten links Ende
            75, 30    # Oben links Ende
        ]
        # Erstellt die Karteikarte auf der Leinwand [1]
        self.canvas.create_polygon(form, fill="beige", outline="black", width=2, smooth=True)

        # Anzeige für das deutsche Wort
        self.wort_anzeige = self.canvas.create_text(175, 120, text="", font=("Arial", 24))

        # Counter Anzeige
        self.counter_anzeige = self.canvas.create_text(175, 260, text="Richtig beantwortet: 0", font=("Arial", 12))

        self.nachricht = self.canvas.create_text(
            175,
            290,
            text="",
            font=("Arial", 12)
        )

        # --- ÄNDERUNG 1: Präziser Hinweistext oben vom Eingabefeld ---
        # Dieser Text liegt auf dem Canvas direkt über der Stelle, an der das Entry gepackt wird
        self.hinweis = self.canvas.create_text(175, 320, text="Englische Übersetzung :", font=("Arial", 12, "bold"))

        # --- ÄNDERUNG 2: Kleineres Texteingabefeld ---
        # Die Breite (width) wurde von 25 auf 15 reduziert, um es kompakter zu machen
        self.eingabe = tk.Entry(root, width=15, font=("Arial", 18), bg="whitesmoke", bd=2)
        self.eingabe.pack(pady=10)

        # Buttons im Rahmen - bleiben gleich zur Vorversion
        self.button_rahmen = tk.Frame(root)
        self.button_rahmen.pack(pady=10)

        self.button_skip = tk.Button(self.button_rahmen, text="Weiter")
        self.button_skip.pack(side=tk.LEFT, padx=10)

        self.button_check = tk.Button(self.button_rahmen, text="Prüfen")
        self.button_check.pack(side=tk.RIGHT, padx=10)

    # --- Methoden (gleichbleibend für die Kommunikation mit dem Controller) ---

    def zeige_wort(self, wort):
        self.canvas.itemconfig(self.wort_anzeige, text=wort)

    def counter_aktualisieren(self, stand):
        self.canvas.itemconfig(self.counter_anzeige, text=f"Richtig beantwortet: {stand}")

    def get_eingabe(self):
        # Der Controller nutzt dies, um die Antwort zu prüfen [2]
        return self.eingabe.get()

    def loesche_eingabe(self):
        self.eingabe.delete(0, tk.END)

    def zeige_nachricht(self, text):
        self.canvas.itemconfig(self.nachricht, text=text)

    # Verbindet Buttons mit Controller
    def set_check_command(self, command):
        self.button_check.config(command=command)

    def set_next_command(self, command):
        self.button_skip.config(command=command)

# Test-Block
if __name__ == "__main__":
    root = tk.Tk()
    view = VokabelView(root)
    view.zeige_wort("Apfel")
    root.mainloop()

