# Path: TP1/main.py

def get_member_info():
    first_name = input("Prénom du membre d’équipage : ")
    last_name = input("Nom du membre d’équipage : ")
    gender = input("Genre du membre d’équipage : ")
    age = int(input("Âge du membre d’équipage : "))
    role = input("Rôle du membre d’équipage ( commandant, pilote, marchant, armurier, entretien, technicien ) : ")
    return {
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "age": age,
        "role": role
    }

def is_unique_last_name(crew, last_name):
    for member in crew:
        if member["last_name"] == last_name:
            return False
    return True

def is_valid_name(name):
    return 3 <= len(name) <= 15

#
def add_member(crew):
    new_member = get_member_info()
    
    if not is_unique_last_name(crew, new_member["last_name"]):
        print("Le nom de famille doit être unique.")
        return
    
    if not is_valid_name(new_member["first_name"]) or not is_valid_name(new_member["last_name"]):
        print("Le prénom et le nom doit être entre 3 et 15 caractères.")
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
    
    print("Erreur Nom")

def display_crew(crew):
    if not crew:
        print("Equipage est vide.")
        return
    
    for member in crew:
        print(f"Prénom: {member['first_name']}, Nom: {member['last_name']}, Genre: {member['gender']}, Âge: {member['age']}, Rôle: {member['role']}")
    print("\n")

def check_crew(crew):
    if len(crew) < 2:
        print("Equipage doit contenir au moins 2 membres.")
        return
    
    has_pilot = any(member['role'] == 'pilote' for member in crew)
    has_technician = any(member['role'] == 'technicien' for member in crew)
    
    if has_pilot and has_technician:
        print("Equipage est prêt pour la mission !")
    else:
        print("Equipage doit contenir au moins un pilote et un technicien.")

# Exemple d'utilisation
if __name__ == "__main__":
    from crew import crew
    display_crew(crew)
    check_crew(crew)
