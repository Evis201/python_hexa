# Path: TP2/member.py

class Member:
    def __init__(self, first_name, last_name, gender, age):
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._age = age

    # Getters
    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_gender(self):
        return self._gender

    def get_age(self):
        return self._age

    # Set
    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_gender(self, gender):
        self._gender = gender

    def set_age(self, age):
        self._age = age

    def introduce_yourself(self):
        return f"Je m'appelle {self._first_name} {self._last_name}, je suis un(e) {self._gender} de {self._age} ans."
