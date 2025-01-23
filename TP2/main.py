# Path: TP2/main.py

import json
from operator_class import Operator
from mentalist import Mentalist
from spaceship import Spaceship
from fleet import Fleet

with open("default.json", "r") as f:
    data = json.load(f)

fleet_data = data["Flotte"]
ships_data = data["Vaisseaux"]

fleet = Fleet(fleet_data["Nom"])

for ship_data in ships_data:
    ship = Spaceship(ship_data["Nom"], ship_data["Type"], ship_data["Etat"])
    fleet.append_spaceship(ship)
    
    for crew_member in ship_data["Equipage"]:
        name_parts = crew_member["Nom"].split()
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else "" # AU CAS OU TA PAS DE NOM :X  

        if crew_member["Type"] == "operator":
            operator = Operator(
                first_name=first_name,
                last_name=last_name,
                gender=crew_member["Sexe"],
                age=crew_member["Age"],
                role=crew_member["Metier"]
            )
            ship.append_member(operator)
        elif crew_member["Type"] == "mentalist":
            mentalist = Mentalist(
                first_name=first_name,
                last_name=last_name,
                gender=crew_member["Sexe"],
                age=crew_member["Age"]
            )
            mentalist.set_mana(crew_member["Mana"])
            ship.append_member(mentalist)


print(f"Flotte: {fleet.get_name()}")
print("Statistiques:", fleet.statistics())
