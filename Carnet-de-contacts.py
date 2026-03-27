import json
import os

def charger_contacts(fichier):
    """Lit le fichier JSON et retourne la liste des contacts"""
    if os.path.exists(fichier):
        with open(fichier, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def ajouter_contact(contacts, nom, telephone):
    """Ajoute un contact à la liste"""
    contacts.append({"nom": nom, "tel": telephone})

def sauvegarder_contacts(fichier, contacts):
    """Sauvegarde la liste des contacts en JSON"""
    with open(fichier, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    fichier = "contacts.json"
    
    contacts = charger_contacts(fichier)
    print(f"Contacts chargés: {len(contacts)}")
    
    ajouter_contact(contacts, "eikichi onizuka", "06 12 34 56 78")
    ajouter_contact(contacts, "Bob Marley", "07 98 65 43 21")
    
    sauvegarder_contacts(fichier, contacts)
    print("Contacts sauvegardés")
    
    contacts = charger_contacts(fichier)
    print("\nTous les contacts:")
    for contact in contacts:
        print(f"  - {contact['nom']}: {contact['tel']}")