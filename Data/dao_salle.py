import json
import mysql.connector
from models.salle import Salle


class DataSalle:
    def get_connection(self):
        with open("Data/config.json", "r", encoding="utf-8") as f:
            config = json.load(f)

        connexion = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return connexion

    def insert_salle(self, salle):
        connexion = self.get_connection()
        curseur = connexion.cursor()

        requete = "INSERT INTO salle (code, description, categorie, capacite) VALUES (%s, %s, %s, %s)"
        valeurs = (salle.code, salle.description, salle.categorie, salle.capacite)

        curseur.execute(requete, valeurs)
        connexion.commit()

        curseur.close()
        connexion.close()

    def update_salle(self, salle):
        connexion = self.get_connection()
        curseur = connexion.cursor()

        requete = """
        UPDATE salle
        SET description = %s, categorie = %s, capacite = %s
        WHERE code = %s
        """
        valeurs = (salle.description, salle.categorie, salle.capacite, salle.code)

        curseur.execute(requete, valeurs)
        connexion.commit()

        curseur.close()
        connexion.close()

    def delete_salle(self, code):
        connexion = self.get_connection()
        curseur = connexion.cursor()

        requete = "DELETE FROM salle WHERE code = %s"
        curseur.execute(requete, (code,))
        connexion.commit()

        curseur.close()
        connexion.close()

    def get_salle(self, code):
        connexion = self.get_connection()
        curseur = connexion.cursor()

        requete = "SELECT * FROM salle WHERE code = %s"
        curseur.execute(requete, (code,))
        resultat = curseur.fetchone()

        curseur.close()
        connexion.close()

        if resultat:
            return Salle(resultat[0], resultat[1], resultat[2], resultat[3])
        return None

    def get_salles(self):
        connexion = self.get_connection()
        curseur = connexion.cursor()

        requete = "SELECT * FROM salle"
        curseur.execute(requete)
        resultats = curseur.fetchall()

        curseur.close()
        connexion.close()

        liste_salles = []
        for ligne in resultats:
            salle = Salle(ligne[0], ligne[1], ligne[2], ligne[3])
            liste_salles.append(salle)

        return liste_salles