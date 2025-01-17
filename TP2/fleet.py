# Path: TP2/fleet.py

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
        if len(self.spaceships) < 15:
            self.spaceships.append(spaceship)
            print(f"{spaceship.name} a été ajouté à la flotte.")
        else:
            print("Capacité maximale de la flotte atteinte.")

    def statistics(self):
        total_members = sum(len(ship.crew) for ship in self.spaceships)
        role_distribution = {}
        total_experience = 0
        operator_count = 0

        for ship in self.spaceships:
            for member in ship.crew:
                role = member.role if isinstance(member, Operator) else "autre"
                role_distribution[role] = role_distribution.get(role, 0) + 1
                if isinstance(member, Operator):
                    total_experience += member.experience
                    operator_count += 1

        average_experience = total_experience / operator_count if operator_count > 0 else 0

        print(f"Nombre total de membres: {total_members}")
        print("Répartition des rôles:")
        for role, count in role_distribution.items():
            print(f"  {role}: {count}")
        print(f"Niveau moyen d'expérience des opérateurs: {average_experience:.2f}")
