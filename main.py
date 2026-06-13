import tkinter as tk
from model.trainer import Trainer
from view.gui import VokabelView
from controller.app_controller import AppController


# Startet die Anwendung
def main():
    # Erstellt Hauptfenster
    root = tk.Tk()

    # Erstellt Trainer
    trainer = Trainer()
    # Lädt Vokabeln aus Datei
    trainer.lade_vokabeln("data/vokabeln.txt")

    # Erstellt Benutzeroberfläche
    view = VokabelView(root)

    # Verbindet Logik und GUI
    controller = AppController(trainer, view)
    controller.start()

    # Startet GUI-Schleife
    root.mainloop()

# Führt Programm direkt aus
if __name__ == "__main__":
    main()





