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
        if self.mana >= 20:
            self.mana -= 20
            operator.act()
            print(f"{self.name} manipule le membre {operator.name}")
        else:
            print(f"{self.name} n'a pas assez de mana pour le manipuler {operator.name}")

    def recharge_mana(self):
        self.mana = min(self.mana + 50, 100)
        print(f"{self.name} a rechargé son mana. Mana actuel: {self.mana}.")