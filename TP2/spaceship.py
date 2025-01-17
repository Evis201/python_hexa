# Path: TP2/spaceship.py

class Spaceship:
    def __init__(self, name, shipType):
        self.name = name
        self.shipType = shipType
        self.crew = []
        self.condition = "opérationnel"

    def append_member(self, member):
        if len(self.crew) < 10:
            self.crew.append(member)
            print(f"{member.name} a été ajouté à l'équipage.")
        else:
            print("Capacité maximale de l'équipage atteinte.")

    def check_preparation(self):
        has_pilot = any(member.role == "pilote" for member in self.crew if isinstance(member, Operator))
        has_technician = any(member.role == "technicien" for member in self.crew if isinstance(member, Operator))
        return has_pilot and has_technician