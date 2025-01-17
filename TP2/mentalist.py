# Path: TP2/mentalist.py

class Member:
    def __init__(self, name):
        self.name = name

class Operator(Member):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role
        self.experience = 0

    def act(self):
        print(f"{self.name} {self.role} le vaisseau.")

class Mentalist(Member):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 100

    def get_mana(self):
        return self.mana

    def set_mana(self, mana):
        self.mana = mana

    def act(self, operator):
        pass

    def recharge_mana(self):
        self.mana += 10