# Path: TP2/fleet.py

from spaceship import Spaceship
from operator_class import Operator

class Fleet:
    def __init__(self, name):
        self._name = name
        self._spaceships = []

    # Getters
    def get_name(self):
        return self._name

    def get_spaceships(self):
        return self._spaceships

    def append_spaceship(self, spaceship):
        if len(self._spaceships) < 15:
            self._spaceships.append(spaceship)
        else:
            raise ValueError("La capacité maximale de la flotte est atteinte.")

    def statistics(self):
        total_members = sum(len(spaceship.get_crew()) for spaceship in self._spaceships)
        roles = {}
        for spaceship in self._spaceships:
            for member in spaceship.get_crew():
                if isinstance(member, Operator):
                    roles[member.get_role()] = roles.get(member.get_role(), 0) + 1
        return {
            "Total membres": total_members,
            "Répartition des rôles": roles,
        }
