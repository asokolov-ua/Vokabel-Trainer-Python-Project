from model.vokabel import Vokabel

class Trainer:

    # Initialisiert Trainingsdaten
    def __init__(self):
        self.vokabeln = []
        self.index = 0
        self.richtig = 0
        self.falsch = 0

    # Lädt Vokabeln aus einer Textdatei
    def lade_vokabeln(self, dateipfad):
        with open(dateipfad, "r", encoding="utf-8") as file:
            for zeile in file:

                # Entfernt Leerzeichen
                zeile = zeile.strip()

                # Überspringt leere Zeilen
                if zeile == "":
                    continue

                # Trennt Wort und Übersetzung
                deutsch, english = zeile.split(";")
                # Erstellt Vokabelobjekt
                vokabel = Vokabel(deutsch, english)
                # Fügt Objekt zur Liste hinzu
                self.vokabeln.append(vokabel)

    # Gibt die aktuelle Vokabel zurück
    def aktuelle_vokabel(self):
        if self.ist_fertig():
            return None

        return self.vokabeln[self.index]

    # Prüft die Antwort
    def pruefe_antwort(self, antwort):
        vokabel = self.aktuelle_vokabel()

        if vokabel is None:
            return False

        if vokabel.pruefe(antwort):
            self.richtig += 1
            return True

        self.falsch += 1
        return False

    # Geht zur nächsten Vokabel
    def naechste_vokabel(self):
        self.index += 1

    # Prüft ob Training beendet ist
    def ist_fertig(self):
        return self.index >= len(self.vokabeln)

