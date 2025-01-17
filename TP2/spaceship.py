# Path: TP2/spaceship.py

class Spaceship:
    def __init__(self, name, ship_type, condition="opérationnel"):
        self.name = name
        self.ship_type = ship_type
        self.crew = []
        self.condition = condition

    def append_member(self, member):
        if len(self.crew) < 10 and isinstance(member, (Operator, Mentalist)):
            self.crew.append(member)
        else:
            raise ValueError("Le membre ne peut pas être ajouté (limite atteinte ou type incorrect).")

    def remove_member(self, first_name, last_name):
        for member in self.crew:
            if member.first_name == first_name and member.last_name == last_name:
                self.crew.remove(member)
                return
        print("Membre non trouvé.")

    def display_crew(self):
        for member in self.crew:
            print(member.introduce_yourself())

    def check_preparation(self):
        has_pilot = any(isinstance(member, Operator) and member.role == "pilote" for member in self.crew)
        has_technician = any(isinstance(member, Operator) and member.role == "technicien" for member in self.crew)
        return has_pilot and has_technician
