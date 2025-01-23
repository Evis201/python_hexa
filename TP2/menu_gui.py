import tkinter as tk
from tkinter import messagebox
from operator_class import Operator
from mentalist import Mentalist
from spaceship import Spaceship
from fleet import Fleet
import json

with open("default.json", "r") as f:
    data = json.load(f)

fleet_data = data["Fondation"]["Flotte"]
members_data = data["Fondation"]["MembresEquipage"]

fleet = Fleet(fleet_data["Nom"])

spaceships = {}
for ship_data in fleet_data["Vaisseaux"]:
    ship = Spaceship(ship_data["Nom"], ship_data["Type"], ship_data["Etat"])
    fleet.append_spaceship(ship)
    spaceships[ship_data["Nom"]] = ship

operators_data = members_data.get("Opérateurs", [])
mentalists_data = members_data.get("Mentalistes", [])

if not operators_data:
    print("Aucun opérateur trouvé dans les données JSON.")

if not mentalists_data:
    print("Aucun mentaliste trouvé dans les données JSON.")

for operator_data in operators_data:
    operator = Operator(
        first_name=operator_data["Nom"].split()[0],
        last_name=operator_data["Nom"].split()[1],
        gender=operator_data["Sexe"],
        age=operator_data["Age"],
        role=operator_data["Métier"]
    )
    for ship in spaceships.values():
        if len(ship.get_crew()) < 10:
            ship.append_member(operator)
            break

for mentalist_data in mentalists_data:
    mentalist = Mentalist(
        first_name=mentalist_data["Nom"].split()[0],
        last_name=mentalist_data["Nom"].split()[1],
        gender=mentalist_data["Sexe"],
        age=mentalist_data["Age"]
    )
    for ship in spaceships.values():
        if len(ship.get_crew()) < 10:
            ship.append_member(mentalist)
            break



# GUI
def rename_fleet():
    new_name = name_entry.get()
    if new_name:
        fleet._name = new_name
        messagebox.showinfo("Succès", f"La flotte a été renommée en {new_name} !")
    else:
        messagebox.showwarning("Erreur", "Veuillez entrer un nom valide.")


def show_statistics():
    stats = fleet.statistics()
    stats_text = f"Nom de la flotte: {fleet.get_name()}\n\n"
    stats_text += f"Total membres: {stats['Total membres']}\n\nRépartition des rôles:\n"
    for role, count in stats["Répartition des rôles"].items():
        stats_text += f"- {role}: {count}\n"
    messagebox.showinfo("Statistiques de la flotte", stats_text)


def add_spaceship():
    new_ship_name = ship_name_entry.get()
    new_ship_type = ship_type_entry.get()
    if new_ship_name and new_ship_type:
        new_ship = Spaceship(new_ship_name, new_ship_type)
        try:
            fleet.append_spaceship(new_ship)
            spaceships[new_ship_name] = new_ship
            messagebox.showinfo("Succès", f"Vaisseau '{new_ship_name}' ajouté à la flotte.")
        except ValueError as e:
            messagebox.showwarning("Erreur", str(e))
    else:
        messagebox.showwarning("Erreur", "Veuillez entrer un nom et un type pour le vaisseau.")


root = tk.Tk()
root.title("Gestion de la flotte")

tk.Label(root, text="=== Gestion de la flotte ===", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Renommer la flotte :").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Button(root, text="Renommer", command=rename_fleet).pack(pady=5)

tk.Label(root, text="Ajouter un vaisseau :").pack()
tk.Label(root, text="Nom du vaisseau :").pack()
ship_name_entry = tk.Entry(root)
ship_name_entry.pack()
tk.Label(root, text="Type de vaisseau :").pack()
ship_type_entry = tk.Entry(root)
ship_type_entry.pack()
tk.Button(root, text="Ajouter le vaisseau", command=add_spaceship).pack(pady=5)

tk.Button(root, text="Afficher les statistiques", command=show_statistics).pack(pady=10)

tk.Button(root, text="Quitter", command=root.quit).pack(pady=5)

root.mainloop()
