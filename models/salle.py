class Salle:
    def __init__(self, code, description, categorie, capacite):
        self.code = code
        self.description = description
        self.categorie = categorie
        self.capacite = capacite

    def afficher_infos(self):
        print("Code :", self.code)
        print("Description :", self.description)
        print("Categorie :", self.categorie)
        print("Capacite :", self.capacite)
