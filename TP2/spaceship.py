# Path: TP2/spaceship.py

from operator_class import Operator

class Spaceship:
    def __init__(self, name, ship_type, condition="Opérationnel"):
        self._name = name
        self._ship_type = ship_type
        self._crew = []
        self._condition = condition

    # Getters
    def get_name(self):
        return self._name

    def get_ship_type(self):
        return self._ship_type

    def get_crew(self):
        return self._crew

    def get_condition(self):
        return self._condition

    # Setters
    def set_condition(self, condition):
        self._condition = condition

    def append_member(self, member):
        if len(self._crew) < 10:
            self._crew.append(member)
        else:
            raise ValueError("La capacité maximale de l'équipage est atteinte.")

    def remove_member(self, member_name):
        for member in self._crew:
            if f"{member.get_first_name()} {member.get_last_name()}" == member_name:
                self._crew.remove(member)
                return
        raise ValueError(f"Le membre {member_name} n'existe pas.")

    def display_crew(self):
        for member in self._crew:
            print(member.introduce_yourself())

    def check_preparation(self):
        has_pilot = any(isinstance(member, Operator) and member.get_role() == "Pilote" for member in self._crew)
        has_technician = any(isinstance(member, Operator) and member.get_role() == "Technicien" for member in self._crew)
        return has_pilot and has_technician