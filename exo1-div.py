def diviser(a, b):
    """Divise a par b avec gestion d'erreurs."""
    try:
        if b == 0:
            print("Erreur : division par zéro impossible")
            return None
        return a / b
    except TypeError:
        print("Erreur : les deux arguments doivent être des nombres")
        return None


# Tests
print(diviser(10, 2))      # 5.0
print(diviser(10, 0))      # Erreur : division par zéro impossible
print(diviser("dix", 2))   # Erreur : les deux arguments doivent être des nombres