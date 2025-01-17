# Path: TP2/main.py

import json
from operator_class import Operator
from mentalist import Mentalist
from spaceship import Spaceship
from fleet import Fleet

with open('default.json', 'r') as file:
    data = json.load(file)

fleet_data = data["Fondation"]["Flotte"]
fleet = Fleet(fleet_data["Nom"])

for ship_data in fleet_data["Vaisseaux"]:
    spaceship = Spaceship(ship_data["Nom"], ship_data["Type"])
    spaceship.set_condition(ship_data["Etat"])
    fleet.append_spaceship(spaceship)

crew_data = data["Fondation"]["MembresEquipage"]
for operator_data in crew_data["Opérateurs"]:
    operator = Operator(operator_data["Nom"], operator_data["Métier"].lower())
    for spaceship in fleet.get_spaceships():
        if len(spaceship.crew) < 10:
            spaceship.append_member(operator)
            break

for mentalist_data in crew_data["Mentalistes"]:
    mentalist = Mentalist(mentalist_data["Nom"])
    for spaceship in fleet.get_spaceships():
        if len(spaceship.crew) < 10:
            spaceship.append_member(mentalist)
            break

for spaceship in fleet.get_spaceships():
    for member in spaceship.crew:
        if isinstance(member, Operator):
            member.act()
            member.gain_experience()
        elif isinstance(member, Mentalist):
            member.act(spaceship.crew[0])  # Influence le premier membre de l'équipage
            member.recharge_mana()

# Vérification des attributs
for spaceship in fleet.get_spaceships():
    print(f"Vaisseau: {spaceship.name}, Type: {spaceship.shipType}, État: {spaceship.condition}")
    for member in spaceship.crew:
        if isinstance(member, Operator):
            print(f"  Opérateur: {member.name}, Rôle: {member.role}, Expérience: {member.experience}")
        elif isinstance(member, Mentalist):
            print(f"  Mentaliste: {member.name}, Mana: {member.mana}")

# Vérification de la préparation des vaisseaux
for spaceship in fleet.get_spaceships():
    print(f"{spaceship.name} est prêt: {spaceship.check_preparation()}")

# Affichage des statistiques de la flotte
fleet.statistics()