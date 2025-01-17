# Path: TP2/spaceship.py

from operator_class import Operator

class Spaceship:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.crew = []
        self.condition = "Opérationnel"

    def append_member(self, member):
        if len(self.crew) < 10:
            self.crew.append(member)
            print(f"{member.name} a été ajouté à l'équipage.")
        else:
            print("Capacité maximale de l'équipage atteinte.")

    def check_preparation(self):
        has_pilot = any(member.role == "pilote" for member in self.crew if isinstance(member, Operator))
        has_technician = any(member.role == "technicien" for member in self.crew if isinstance(member, Operator))
        return has_pilot and has_technician and self.condition == "ready"

    def set_condition(self, condition):
        valid_conditions = ["Opérationnel", "Endommagé", "Détruit"]
        if condition in valid_conditions:
            self.condition = condition
            print(f"L'état du vaisseau est maintenant: {condition}.")
        else:
            print(f"Condition invalide: {condition}. Les conditions valides sont: {', '.join(valid_conditions)}.")