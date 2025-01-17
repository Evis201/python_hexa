# Path: TP2/main.py

import json
from operator_class import Operator
from mentalist import Mentalist
from classes.spaceship import Spaceship
from fleet import Fleet

with open('default.json', 'r') as file:
    data = json.load(file)

fleet_data = data["Fondation"]["Flotte"]
fleet = Fleet(fleet_data["Nom"])

for ship_data in fleet_data["Vaisseaux"]:
    spaceship = Spaceship(ship_data["Nom"], ship_data["Type"])
    spaceship.set_condition(ship_data["Etat"])
    fleet.append_spaceship(spaceship)

spaceship_name = "Cosmo Explorer"
spaceship_type = "exploration"
spaceship = Spaceship(name=spaceship_name, type=spaceship_type)

fleet.add_spaceship(spaceship)

crew_data = data["Fondation"]["MembresEquipage"]
if "Opérateurs" in crew_data:
    for operator_data in crew_data["Opérateurs"]:
        operator = Operator(operator_data["Nom"], operator_data["Métier"].lower())
        for spaceship in fleet.get_spaceships():
            if len(spaceship.crew) < 10:
                spaceship.append_member(operator)
                break

if "Mentalistes" in crew_data:
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
            if spaceship.crew:
                member.act(spaceship.crew[0])  # Pass the first crew member as the operator
            member.recharge_mana()

for spaceship in fleet.get_spaceships():
    print(f"Vaisseau: {spaceship.name}, Type: {spaceship.type}, État: {spaceship.condition}")

# Verif les attributs
for spaceship in fleet.get_spaceships():
    print(f"Vaisseau: {spaceship.name}, Type: {spaceship.type}, État: {spaceship.condition}")
    for member in spaceship.crew:
        if isinstance(member, Operator):
            print(f"  Opérateur: {member.name}, Rôle: {member.role}, Expérience: {member.experience}")
        elif isinstance(member, Mentalist):
            print(f"  Mentaliste: {member.name}, Mana: {member.mana}")

# Verif la prep
for spaceship in fleet.get_spaceships():
    print(f"{spaceship.name} est prêt: {spaceship.check_preparation()}")

fleet.statistics()