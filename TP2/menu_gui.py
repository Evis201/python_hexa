# Path: TP2/menu_gui.py

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog
import json
from fleet import Fleet
from spaceship import Spaceship
from operator_class import Operator
from mentalist import Mentalist

class FleetApp:
    def __init__(self, root):
        self.root = root  # Pas toucher sinon tkinder va pas être content
        self.root.title("Gestion de la Flotte")
        self.fleet = None
        self.spaceships = {}

        self.load_data()

        # MAIN INTERFACE :)
        self.create_widgets()

    def load_data(self):
        try:
            with open("default.json", "r") as f:
                self.data = json.load(f)

            fleet_data = self.data["Flotte"]
            ships_data = self.data["Vaisseaux"]

            self.fleet = Fleet(fleet_data["Nom"])

            for ship_data in ships_data:
                ship = Spaceship(ship_data["Nom"], ship_data["Type"], ship_data["Etat"])
                self.fleet.append_spaceship(ship)
                self.spaceships[ship_data["Nom"]] = ship

                for crew_member in ship_data["Equipage"]:
                    name_parts = crew_member["Nom"].split()
                    first_name = name_parts[0]
                    last_name = name_parts[1] if len(name_parts) > 1 else ""

                    if crew_member["Type"] == "operator":
                        operator = Operator(
                            first_name=first_name,
                            last_name=last_name,
                            gender=crew_member["Sexe"],
                            age=crew_member["Age"],
                            role=crew_member["Metier"]
                        )
                        ship.append_member(operator)
                    elif crew_member["Type"] == "mentalist":
                        mentalist = Mentalist(
                            first_name=first_name,
                            last_name=last_name,
                            gender=crew_member["Sexe"],
                            age=crew_member["Age"]
                        )
                        mentalist.set_mana(crew_member["Mana"])
                        ship.append_member(mentalist)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de charger les données : {e}")

    def assign_member(self, member):
        for ship in self.spaceships.values():
            if len(ship.get_crew()) < 10:
                ship.append_member(member)
                break

    def create_widgets(self):
        # LABEL Pour liste déroulantes
        lbl_ships = tk.Label(self.root, text="Vaisseaux disponibles:")
        lbl_ships.grid(row=0, column=0, padx=10, pady=5)

        self.ship_list = ttk.Combobox(self.root, values=list(self.spaceships.keys()))
        self.ship_list.grid(row=0, column=1, padx=10, pady=5)
        self.ship_list.bind("<<ComboboxSelected>>", self.display_ship_details)

        # ZONE DE TEXTE ( vaisseaux )
        self.ship_details = tk.Text(self.root, width=70, height=10, state="disabled")
        self.ship_details.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        # BOUTONS ( actions )
        btn_rename_fleet = tk.Button(self.root, text="Renommer la flotte", command=self.rename_fleet)
        btn_rename_fleet.grid(row=2, column=0, pady=5)

        btn_add_ship = tk.Button(self.root, text="Ajouter un vaisseau", command=self.add_ship)
        btn_add_ship.grid(row=2, column=1, pady=5)

        btn_add_member = tk.Button(self.root, text="Ajouter un membre", command=self.add_member)
        btn_add_member.grid(row=3, column=0, pady=5)

        btn_remove_member = tk.Button(self.root, text="Supprimer un membre", command=self.remove_member)
        btn_remove_member.grid(row=3, column=1, pady=5)

        btn_ship_prep = tk.Button(self.root, text="Vérifier la préparation", command=self.check_ship_prep)
        btn_ship_prep.grid(row=4, column=0, pady=5)

        # ZONE DE TEXTE ( statistiques )
        self.stats_display = tk.Text(self.root, width=50, height=10, state="disabled")
        self.stats_display.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def display_ship_details(self, event):
        ship_name = self.ship_list.get()
        ship = self.spaceships.get(ship_name)

        if ship:
            details = f"Nom: {ship.get_name()}\nType: {ship.get_ship_type()}\nÉtat: {ship.get_condition()}\n\nÉquipage:\n"
            crew = ship.get_crew()

            if crew:
                for member in crew:
                    details += f"- {member.introduce_yourself()}\n"
            else:
                details += "Aucun membre d'équipage."

            self.ship_details.config(state="normal")
            self.ship_details.delete(1.0, tk.END)
            self.ship_details.insert(tk.END, details)
            self.ship_details.config(state="disabled")

    def rename_fleet(self):
        new_name = tk.simpledialog.askstring("Renommer la flotte", "Entrez le nouveau nom de la flotte:")
        if new_name:
            self.fleet.rename(new_name)
            messagebox.showinfo("Succès", f"La flotte a été renommée en {new_name}.")

    def add_ship(self):
        name = tk.simpledialog.askstring("Ajouter un vaisseau", "Nom du vaisseau:")
        type_ship = tk.simpledialog.askstring("Ajouter un vaisseau", "Type du vaisseau:")
        state = tk.simpledialog.askstring("Ajouter un vaisseau", "État du vaisseau:")

        if name and type_ship and state:
            new_ship = Spaceship(name, type_ship, state)
            self.fleet.append_spaceship(new_ship)
            self.spaceships[name] = new_ship
            self.ship_list.config(values=list(self.spaceships.keys()))
            messagebox.showinfo("Succès", f"Le vaisseau {name} a été ajouté à la flotte.")

    def add_member(self):
        ship_name = self.ship_list.get()
        ship = self.spaceships.get(ship_name)

        if ship:
            full_name = tk.simpledialog.askstring("Ajouter un membre", "Nom complet du membre:")
            gender = tk.simpledialog.askstring("Ajouter un membre", "Sexe:")
            age = tk.simpledialog.askinteger("Ajouter un membre", "Âge:")
            role = tk.simpledialog.askstring("Ajouter un membre", "Rôle (operator/mentalist):")

            if full_name and gender and age and role:
                first_name, last_name = (full_name.split()[0], full_name.split()[1]) if " " in full_name else (full_name, "")
                if role.lower() == "operator":
                    new_member = Operator(first_name, last_name, gender, age, role)
                elif role.lower() == "mentalist":
                    mana = tk.simpledialog.askinteger("Ajouter un mentalist", "Mana:")
                    new_member = Mentalist(first_name, last_name, gender, age)
                    new_member.set_mana(mana)
                else:
                    messagebox.showerror("Erreur", "Type de membre inconnu.")
                    return

                ship.append_member(new_member)
                messagebox.showinfo("Succès", f"{full_name} a été ajouté à l'équipage du vaisseau {ship_name}.")
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un vaisseau.")

    def remove_member(self):
        ship_name = self.ship_list.get()
        ship = self.spaceships.get(ship_name)

        if ship:
            full_name = tk.simpledialog.askstring("Supprimer un membre", "Nom complet du membre à supprimer:")
            if full_name:
                member = ship.get_member_by_name(full_name)
                if member:
                    ship.remove_member(member)
                    messagebox.showinfo("Succès", f"{full_name} a été supprimé de l'équipage du vaisseau {ship_name}.")
                else:
                    messagebox.showerror("Erreur", "Membre non trouvé")
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un vaisseau.")

    def check_ship_prep(self):
        ship_name = self.ship_list.get()
        ship = self.spaceships.get(ship_name)

        if ship:
            if ship.is_ready():
                messagebox.showinfo("Préparation", f"Le vaisseau {ship_name} est prêt.")
            else:
                messagebox.showinfo("Préparation", f"Le vaisseau {ship_name} n'est pas prêt.")
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un vaisseau.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FleetApp(root)
    root.mainloop()
