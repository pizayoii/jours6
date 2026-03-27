def saisir_age():

    while True:
        try:
            age = int(input("Entrez votre âge : "))
            
            if age < 0 or age > 120:
                raise ValueError("L'âge doit être entre 0 et 120")
            
            return age
        
        except ValueError as e:
            print(f"Erreur : {e}. Veuillez entrer un nombre valide.")


if __name__ == "__main__":
    age = saisir_age()
    print(f"Vous avez : {age} ans")