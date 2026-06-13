from model.vokabel import Vokabel

class Trainer:
    def __init__(self):
        self.vokabeln = []
        self.index = 0
        self.richtig = 0
        self.falsch = 0


    def lade_vokabeln(self, dateipfad):
        with open(dateipfad, "r", encoding="utf-8") as file:
            for zeile in file:
                zeile = zeile.strip()

                if zeile == "":
                    continue

                deutsch, english = zeile.split(";")
                vokabel = Vokabel(deutsch, english)
                self.vokabeln.append(vokabel)


    def aktuelle_vokabel(self):
        if self.ist_fertig():
            return None

        return self.vokabeln[self.index]


    def naechste_vokabel(self):
        self.index += 1


    def pruefe_antwort(self, antwort):
        vokabel = self.aktuelle_vokabel()

        if vokabel is None:
            return False

        if vokabel.pruefe(antwort):
            self.richtig += 1
            return True

        self.falsch += 1
        return False
    

    def ist_fertig(self):
        return self.index >= len(self.vokabeln)