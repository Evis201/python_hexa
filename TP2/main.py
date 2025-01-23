# Path: TP2/main.py

import json
from operator_class import Operator
from mentalist import Mentalist
from spaceship import Spaceship
from fleet import Fleet

# Charger les données JSON
with open("default.json", "r") as f:
    data = json.load(f)

# Initialisation de la flotte
fleet_data = data["Fondation"]["Flotte"]
members_data = data["Fondation"]["MembresEquipage"]

fleet = Fleet(fleet_data["Nom"])

# Création des vaisseaux
for ship_data in fleet_data["Vaisseaux"]:
    ship = Spaceship(ship_data["Nom"], ship_data["Type"], ship_data["Etat"])
    fleet.append_spaceship(ship)

# Affichage des statistiques de la flotte
print(f"Flotte: {fleet.get_name()}")
print("Statistiques:", fleet.statistics())