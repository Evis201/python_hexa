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

def display_member(crew):

# Exemple d'utilisation
if __name__ == "__main__":
    from crew import crew
    remove_member(crew)
    print(crew)
