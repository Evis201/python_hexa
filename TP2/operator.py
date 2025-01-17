# Path: TP2/operator.py

class Member:
    def __init__(self, name):
        self.name = name

class Operator(Member):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role
        self.experience = 0 # 0 par défaut pour un nouvel opérateur

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def get_experience(self):
        return self.experience

    def set_experience(self, experience):
        self.experience = experience

    def act(self):
        print(f"{self.name} {self.role} le vaisseau.")

    def gain_experience(self):
        self.experience += 1
        
    def act(self):
        if self.role == "pilote":
            print(f"{self.name} pilote le vaisseau.")
        elif self.role == "technicien":
            print(f"{self.name} répare une partie du vaisseau.")
        elif self.role == "concierge":
            print(f"{self.name} nettoie les toilettes du vaisseau.")
        else:
            print(f"{self.name} {self.role} le vaisseau.")