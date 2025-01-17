# Path: TP2/fleet.py

class Fleet:
    def __init__(self, name):
        self.name = name
        self.spaceships = []

    def append_spaceship(self, spaceship):
        if len(self.spaceships) < 15:
            self.spaceships.append(spaceship)
        else:
            raise ValueError("Limite de 15 vaisseaux atteinte.")

    def statistics(self):
        total_members = sum(len(spaceship.crew) for spaceship in self.spaceships)
        print(f"Nombre total de membres: {total_members}")
        roles_count = {}
        for spaceship in self.spaceships:
            for member in spaceship.crew:
                if isinstance(member, Operator):
                    roles_count[member.role] = roles_count.get(member.role, 0) + 1
        print("Répartition des rôles:", roles_count)
