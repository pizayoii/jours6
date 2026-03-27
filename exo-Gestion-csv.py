import csv
        # Ajouter un nouvel étudiant
nouvel_etudiant = {'nom': 'Dupuis', 'prenom': 'Marie', 'age': '21'}
        
with open('fichier-exo3.csv', 'a', newline='') as fichier:
            writer = csv.DictWriter(fichier, fieldnames=['nom', 'prenom', 'age'])
            writer.writerow(nouvel_etudiant)
        
        # Relire et afficher tous les étudiants
print("\n--- Affichage des étudiants ---")
with open('fichier-exo3.csv', 'r') as fichier:
            reader = csv.DictReader(fichier)
            for etudiant in reader:
                print(f"{etudiant['prenom']} {etudiant['nom']} - {etudiant['age']} ans")
