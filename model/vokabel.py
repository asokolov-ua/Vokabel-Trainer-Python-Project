class Vokabel:
    def __init__(self, deutsch, english):
        self.deutsch = deutsch
        self.english = english

    def pruefe(self, antwort):
        antwort = antwort.strip.lower() #löscht alle Abstände und macht alle Buchstaben klein

        return antwort == self.english.lower()

    # Defines how the vocabulary is displayed as text
    def __str__(self):
        return f"{self.deutsch} -> {self.english}"


# wort = Vokabel("Apfel", "Apple")
# print(wort)