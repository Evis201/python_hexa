# Path: TP2/fleet.py

from operator_class import Operator

class Fleet:
    def __init__(self, name):
        self.name = name
        self.spaceships = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_spaceships(self):
        return self.spaceships

    def set_spaceships(self, spaceships):
        self.spaceships = spaceships

    def append_spaceship(self, spaceship):
        self.spaceships.append(spaceship)

    def statistics(self):
        for spaceship in self.spaceships:
            print(f"Vaisseau: {spaceship.name}, Type: {spaceship.type}, État: {spaceship.condition}")
            for member in spaceship.crew:
                role = member.role if isinstance(member, Operator) else "autre"
                print(f"  Membre: {member.name}, Rôle: {role}")
