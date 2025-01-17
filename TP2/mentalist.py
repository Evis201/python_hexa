# Path: TP2/mentalist.py

class Mentalist(Member):
    def __init__(self, first_name, last_name, gender, age, mana=100):
        super().__init__(first_name, last_name, gender, age)
        self.mana = mana

    def act(self, operator):
        if self.mana >= 20:
            self.mana -= 20
            return f"{self.first_name} {self.last_name} influence {operator.first_name} {operator.last_name}."
        else:
            return f"{self.first_name} {self.last_name} n'a pas assez de mana pour agir."

    def recharge_mana(self):
        self.mana = min(self.mana + 50, 100)

    # Getters and Setters
    def get_mana(self):
        return self.mana

    def set_mana(self, mana):
        self.mana = mana