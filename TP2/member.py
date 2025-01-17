# Path: TP2/member.py

class Member:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def introduce_yourself(self):
        return f"Je m'appelle {self.first_name} {self.last_name}, je suis un {self.gender} de {self.age} ans."