from Data.dao_salle import DataSalle
class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie or salle.capacite is None:
            return False, "Tous les champs sont obligatoires"
        if salle.capacite < 1:
            return False, "La capacité doit être supérieure ou égale à 1"
        self.dao_salle.insert_salle(salle)
        return True, "Salle ajoutée avec succès"

    def modifier_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie or salle.capacite is None:
            return False, "Tous les champs sont obligatoires"
        if salle.capacite < 1:
            return False, "La capacité doit être supérieure ou égale à 1"
        self.dao_salle.update_salle(salle)
        return True, "Salle modifiée avec succès"

    def supprimer_salle(self, code):
        self.dao_salle.delete_salle(code)

    def rechercher_salle(self, code):
        return self.dao_salle.get_salle(code)

    def recuperer_salles(self):
        return self.dao_salle.get_salles()