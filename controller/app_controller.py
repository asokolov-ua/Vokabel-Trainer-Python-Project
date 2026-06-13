class AppController:

    # Verbindet Trainer und Benutzeroberfläche
    def __init__(self, trainer, view):
        self.trainer = trainer
        self.view = view

        # Verknüpft Buttons mit Methoden
        self.view.set_check_command(self.pruefen)
        self.view.set_next_command(self.naechste)

    # Startet die Anwendung
    def start(self):

        # Aktuelles Wort holen
        vokabel = self.trainer.aktuelle_vokabel()

        # Wort anzeigen
        self.view.zeige_wort(vokabel.deutsch)

    # Prüft die Antwort des Benutzers
    def pruefen(self):

        # Eingabe aus dem GUI lesen
        antwort = self.view.get_eingabe()

        # Antwort überprüfen
        richtig = self.trainer.pruefe_antwort(antwort)

        # Ergebnis anzeigen
        if richtig:
            self.view.zeige_nachricht("Richtig!")
        else:
            self.view.zeige_nachricht("Falsch!")

        # Punktestand aktualisieren
        self.view.counter_aktualisieren(
            self.trainer.richtig
        )

    # Geht zum nächsten Wort
    def naechste(self):

        # Zum nächsten Index wechseln
        self.trainer.naechste_vokabel()

        # Eingabefeld leeren
        self.view.loesche_eingabe()

        # Alte Nachricht löschen
        self.view.zeige_nachricht("")

        # Prüfen ob Training beendet ist
        if self.trainer.ist_fertig():

            self.view.zeige_wort("Fertig!")

        else:

            # Nächstes Wort anzeigen
            vokabel = self.trainer.aktuelle_vokabel()

            self.view.zeige_wort(
                vokabel.deutsch
            )