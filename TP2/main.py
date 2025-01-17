# Path: TP2/main.py

import json
from member import Member
from operator import Operator
from mentalist import Mentalist
from spaceship import Spaceship
from fleet import Fleet

with open('default.json', 'r') as file:
    data = json.load(file)

if __name__ == "__main__":
    # Créer une flotte
    fleet = Fleet("Galactica")

    # Créer des vaisseaux
    spaceship1 = Spaceship("Bayta", "Marchand")
    spaceship2 = Spaceship("Dark Nebula", "Guerre", "Endommagé")

    # Ajouter des membres d'équipage
    op1 = Operator("Gaal", "Dornick", "Femme", 34, "technicien")
    ment1 = Mentalist("Joie", "", "Femme", 25)

    spaceship1.append_member(op1)
    spaceship2.append_member(ment1)

    # Ajouter des vaisseaux à la flotte
    fleet.append_spaceship(spaceship1)
    fleet.append_spaceship(spaceship2)

    # Afficher les statistiques
    fleet.statistics()
