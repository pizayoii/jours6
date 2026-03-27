import csv

def etudiant_existe(nom, prenom):
    """Vérifie si un étudiant existe déjà dans le fichier CSV"""
    try:
        with open('fichier-exo3.csv', 'r') as fichier:
            reader = csv.DictReader(fichier)
            for etudiant in reader:
                if etudiant['nom'] == nom and etudiant['prenom'] == prenom:
                    return True
        return False
    except FileNotFoundError:
        return False

# Ajouter un nouvel étudiant seulement s'il n'existe pas déjà
nouvel_etudiant = {'nom': 'Dupuis', 'prenom': 'Marie', 'age': '21'}

if not etudiant_existe(nouvel_etudiant['nom'], nouvel_etudiant['prenom']):
    with open('fichier-exo3.csv', 'a', newline='') as fichier:
        writer = csv.DictWriter(fichier, fieldnames=['nom', 'prenom', 'age'])
        writer.writerow(nouvel_etudiant)
    print("Nouvel étudiant ajouté.")
else:
    print("L'étudiant existe déjà.")

# Relire et afficher tous les étudiants
print("\n--- Affichage des étudiants ---")
with open('fichier-exo3.csv', 'r') as fichier:
    reader = csv.DictReader(fichier)
    for etudiant in reader:
        if etudiant['nom'] and etudiant['prenom'] and etudiant['age']:  # Vérifier que tous les champs sont présents
            print(f"{etudiant['prenom']} {etudiant['nom']} - {etudiant['age']} ans")
