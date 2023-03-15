"""
Ce module contient une fonction pour calculer la soustraction de deux nombres.
"""

def soustraction():
    """
    Cette fonction demande à l'utilisateur de saisir deux nombres et calcule la soustraction de ces deux nombres.
    """
    # Demander à l'utilisateur de saisir les deux nombres
    premier_nombre = float(input("Entrez le premier nombre : "))
    deuxieme_nombre = float(input("Entrez le deuxième nombre : "))

    # Vérifier si le deuxième nombre n'est pas 0
    if deuxieme_nombre == 0:
        print("Le deuxième nombre ne peut pas être zéro. Veuillez réessayer.")
    else:
        # Calculer la soustraction de deux nombres
        resultat = premier_nombre - deuxieme_nombre

        # Afficher le résultat
        print("Le résultat de la soustraction est :", resultat)

# Appeler la fonction pour exécuter le programme
soustraction()