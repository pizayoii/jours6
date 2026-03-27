import csv
import json
from pathlib import Path

def analyser_csv_et_exporter_json():
    csv_file = "etudiants.csv"
    json_file = "rapport.json"
    
    try:
        if not Path(csv_file).exists():
            raise FileNotFoundError(f"Le fichier '{csv_file}' n'existe pas.")
        
        etudiants = []
        ages = []
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            lecteur = csv.DictReader(f)
            
            if lecteur.fieldnames is None or 'nom' not in lecteur.fieldnames or 'age' not in lecteur.fieldnames:
                raise ValueError("Le CSV doit contenir les colonnes 'nom' et 'age'.")
            
            for ligne in lecteur:
                try:
                    nom = ligne.get('nom', '').strip()
                    prenom = ligne.get('prenom', '').strip()
                    age = int(ligne.get('age', 0))
                    
                    nom_complet = f"{nom} {prenom}"
                    
                    if not nom:
                        raise ValueError("Nom vide")
                    if age < 0:
                        raise ValueError("Age invalide")
                    
                    etudiants.append({'nom': nom_complet, 'age': age})
                    ages.append(age)
                    
                except ValueError as e:
                    print(f"Avertissement : ligne ignorée - {e}")
                    continue
        
        if not etudiants:
            raise ValueError("Aucun étudiant valide")
        
        age_moyen = round(sum(ages) / len(ages), 1)
        
        plus_jeune = min(etudiants, key=lambda x: x['age'])
        plus_age = max(etudiants, key=lambda x: x['age'])
        
        rapport = {
            "total_etudiants": len(etudiants),
            "age_moyen": age_moyen,
            "plus_jeune": plus_jeune,
            "plus_age": plus_age
        }
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(rapport, f, ensure_ascii=False, indent=2)
        
        print("Rapport généré")
        
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    analyser_csv_et_exporter_json()