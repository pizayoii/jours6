try:
    with open('fichier-a-lire.txt', 'r') as fichier:
        notes = [int(ligne.strip()) for ligne in fichier.readlines()]
    
    print("Notes :", notes)
    print("Moyenne :", sum(notes) / len(notes))
    
except FileNotFoundError:
    print("Erreur : Le fichier fichier-a-lire.txt n'existe pas dans le dossier courant.")
except ValueError:
    print("Erreur : Le fichier contient des valeurs non numériques.")