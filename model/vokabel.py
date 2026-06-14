class Vokabel:

    # Erstellt eine Vokabelkarte
    def __init__(self, deutsch, english):
        self.deutsch = deutsch
        self.english = english

    # Prüft die Antwort des Benutzers
    def pruefe(self, antwort):
        # Entfernt Leerzeichen und wandelt in Kleinbuchstaben um
        antwort = antwort.strip().lower() #löscht alle Abstände und macht alle Buchstaben klein
        # Vergleicht die Antwort mit der Übersetzung
        return antwort == self.english.lower()

    # Bestimmt die Textdarstellung des Objekts
    def __str__(self):
        return f"{self.deutsch} -> {self.english}"


# wort = Vokabel("Apfel", "Apple")
# print(wort)