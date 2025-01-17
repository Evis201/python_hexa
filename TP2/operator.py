# Path: TP2/operator.py

class Operator(Member):
    def __init__(self, first_name, last_name, gender, age, role, experience=0):
        super().__init__(first_name, last_name, gender, age)
        self.role = role
        self.experience = experience

    def act(self):
        return f"{self.first_name} {self.last_name} réalise une action en tant que {self.role}."

    def gain_experience(self):
        self.experience += 1

    # Getters and Setters
    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def get_experience(self):
        return self.experience

    def set_experience(self, experience):
        self.experience = experience