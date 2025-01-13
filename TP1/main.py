import random

# Path: TP1/main.py

def get_member_info():
    first_name = input("Prenom du membre d’équipage : ")
    last_name = input("Nom du membre d’équipage : ")
    gender = input("Genre du membre d’équipage (homme, femme, hehe) : ")
    age = int(input("Age du membre d’équipage : "))
    role = input("Role du membre d’équipage (commandant, pilote, marchant, armurier, entretien, technicien) : ")
    experience = int(input("Année d'expérience : ")) if role == "technicien" else 0
    return {
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "age": age,
        "role": role,
        "experience": experience
    }

def is_unique_last_name(crew, last_name):
    for member in crew:
        if member["last_name"] == last_name:
            return False
    return True

def is_valid_name(name):
    return 3 <= len(name) <= 15

def is_valid_age(member):
    if member["age"] > 65:
        print("L'age maximum pour un membre d'équipage est de 65 ans")
        return False
    if member["role"] == "pilote" and member["age"] < 25:
        print("L'age minimum pour un pilote est de 25 ans")
        return False
    if member["role"] == "technicien" and member["age"] < 18:
        print("L'age minimum pour un technicien est de 18 ans")
        return False
    return True

# CREW PART
def add_member(crew):
    new_member = get_member_info()
    
    if not is_unique_last_name(crew, new_member["last_name"]):
        print("Le nom de famille doit être unique")
        return
    
    if not is_valid_name(new_member["first_name"]) or not is_valid_name(new_member["last_name"]):
        print("Le prénom et le nom doit être entre 3 et 15 caractères")
        return
    
    if not is_valid_age(new_member):
        return
    
    crew.append(new_member)
    print("Le membre a été ajouté")
    
def remove_member(crew):
    last_name = input("Nom du membre d’équipage à supprimer : ")
    
    for member in crew:
        if member["last_name"] == last_name:
            crew.remove(member)
            print("Le membre a été supprimé")
            return
    
    print("Erreur : Aucun membre d’équipage ne correspond à ce nom de famille.")

def display_crew(crew):
    if not crew:
        print("T'es seul ou pas ?")
        return
    
    for member in crew:
        print(f"Prenom: {member['first_name']}, Nom: {member['last_name']}, Genre: {member['gender']}, Age: {member['age']}, Role: {member['role']}, Experience: {member.get('experience', 0)} ans")
    print("\n")

def check_crew(crew):
    if len(crew) < 2:
        print("L'équipage doit avoir au moins 2 membres")
        return
    
    has_pilot = any(member['role'] == 'pilote' for member in crew)
    has_technician = any(member['role'] == 'technicien' for member in crew)
    
    if has_pilot and has_technician:
        print("L'équipage est prêt pour la mission !")
    else:
        print("L'équipage doit avoir au moins un pilote et un technicien")

def crew_report(crew):
    total_members = len(crew)
    role_distribution = {}
    members_near_max_age = [member for member in crew if member["age"] > 60]
    
    for member in crew:
        role = member["role"]
        if role in role_distribution:
            role_distribution[role] += 1
        else:
            role_distribution[role] = 1
    
    print(f"Nombre total de membres d'équipage : {total_members}")
    print("Répartition par role :")
    for role, count in role_distribution.items():
        print(f"  {role}: {count}")
    
    if members_near_max_age:
        print("Membres proches de l'age maximum :")
        for member in members_near_max_age:
            print(f"  {member['first_name']} {member['last_name']}, age: {member['age']}")

def random_event(crew):
    event = random.choice(["quit", "promote"])
    if event == "quit":
        member = random.choice(crew)
        crew.remove(member)
        print(f"EVENT AUREVOIR : {member['first_name']} {member['last_name']} a quitté l'équipage.")
    elif event == "fall_ouhhhhhhhhhhhhhh":
        member = random.choice(crew)
        crew.remove(member)
        print(f"EVENT OH NON : {member['first_name']} {member['last_name']} est tombé dans l'espace.")
    elif event == "promote":
        member = random.choice(crew)
        if member["role"] == "technicien" and member["experience"] >= 10 and member["age"] >= 25:
            member["role"] = "pilote"
            print(f"EVENT YOPI : {member['first_name']} {member['last_name']} a été promu au role de pilote.")
        else:
            print(f"EVENT DOWNFALL : Aucun membre n'a été promu")

# DISPLAY PART
def display_menu():
    print("\nMenu:")
    print("1. Afficher l'equipage")
    print("2. Ajouter un membre")
    print("3. Supprimer un membre")
    print("4. Verifier l'equipage")
    print("5. Rapport de l'equipage")
    print("6. Quitter")

if __name__ == "__main__":
    from crew import crew
    action_count = 0
    
    while True:
        display_menu()
        choice = input("Choisissez une option : ")
        
        match choice:
            case "1":
                display_crew(crew)
            case "2":
                add_member(crew)
            case "3":
                remove_member(crew)
            case "4":
                check_crew(crew)
            case "5":
                crew_report(crew)
            case "6":
                print("BYE BYE")
                break
            case _:
                print("BAH NON TOUJOURS PAS")
        
        action_count += 1
        if action_count % 5 == 0:
            random_event(crew)
