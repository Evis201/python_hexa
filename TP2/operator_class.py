# Path: TP2/operator.py

from member import Member

class Operator(Member):
    def __init__(self, first_name, last_name, gender, age, role):
        super().__init__(first_name, last_name, gender, age)
        self._role = role
        self._experience = 0

    # Getters
    def get_role(self):
        return self._role

    def get_experience(self):
        return self._experience

    # Setters
    def set_role(self, role):
        self._role = role

    def set_experience(self, experience):
        self._experience = experience

    def act(self):
        return f"{self.get_first_name()} {self.get_last_name()} exécute une action en tant que {self._role}."

    def gain_experience(self):
        self._experience += 1