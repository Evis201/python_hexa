# Path: TP2/mentalist.py

from member import Member

class Mentalist(Member):
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self._mana = 100

    # Getters
    def get_mana(self):
        return self._mana

    # Setters
    def set_mana(self, mana):
        self._mana = mana

    def act(self, operator):
        if self._mana >= 20:
            self._mana -= 20
            return operator.act()
        return f"{self.get_first_name()} n'a pas assez de mana pour influencer l'opérateur."

    def recharge_mana(self):
        self._mana = min(self._mana + 50, 100)