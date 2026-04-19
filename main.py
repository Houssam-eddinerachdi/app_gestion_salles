from services.services_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

service.supprimer_salle("B201")

s1 = Salle("B201", "Salle Réseau", "Laboratoire", 24)
succes, message = service.ajouter_salle(s1)
print(message)

s2 = Salle("B201", "Salle Réseau Cisco", "Laboratoire", 28)
succes, message = service.modifier_salle(s2)
print(message)

salle = service.rechercher_salle("B201")
if salle:
    salle.afficher_infos()

liste = service.recuperer_salles()
for s in liste:
    print("-------------")
    s.afficher_infos()

service.supprimer_salle("B201")
print("Salle supprimée")

from views.view_salle import ViewSalle

app = ViewSalle()
app.mainloop()