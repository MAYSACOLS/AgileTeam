import pandas as pd
import numpy as np
# Liste des utilisateurs et leurs salaires
users = ["Iryna", "Slim", "Isabelle", "Romain"]
from datetime import datetime

def get_user_input():
    # Demander à l'utilisateur son revenu et ses dépenses par catégorie
    print("Veuillez entrer vos informations financières pour chaque mois.")
    
    # Demander le nom de l'utilisateur
    name = input("Nom de l'utilisateur: ")
    income = float(input(f"Quel est votre revenu mensuel, {name}? (en €): "))

    # Demander le mois sous forme de texte (janvier, février, etc.)
    month_str = input("Entrez le mois (par exemple, janvier, février, mars, etc.): ").lower()

    # Dictionnaire pour convertir les mois en numéros
    months = {
        "janvier": 1,
        "février": 2,
        "mars": 3,
        "avril": 4,
        "mai": 5,
        "juin": 6,
        "juillet": 7,
        "août": 8,
        "septembre": 9,
        "octobre": 10,
        "novembre": 11,
        "décembre": 12
    }

    # Vérifier si le mois est valide
    if month_str not in months:
        print("Mois invalide. Veuillez entrer un mois correct.")
        return

    # Convertir le mois en nombre
    month = months[month_str]

    # Définir les catégories
    categories = ["Loyer", "Épicerie", "Transports", "Hobbies", "Voyages"]
    
    # Dictionnaire pour stocker les dépenses de chaque catégorie
    expenses = {}
    
    for category in categories:
        expense = float(input(f"Entrez votre dépense pour {category} (en €): "))
        expenses[category] = expense

    # Retourner toutes les valeurs demandées
    return name, income, month, expenses

def save_to_csv(name, income, month, expenses, total_expenses, remaining):
    # Préparer les données sous forme de dictionnaire pour le CSV
    data = {
        "Name": [name],
        "Month": [month],
        "Income (€)": [income],
        "Loyer (€)": [expenses["Loyer"]],
        "Épicerie (€)": [expenses["Épicerie"]],
        "Transports (€)": [expenses["Transports"]],
        "Hobbies (€)": [expenses["Hobbies"]],
        "Voyages (€)": [expenses["Voyages"]],
        "Total Expenses (€)": [total_expenses],
        "Remaining (€)": [remaining]
    }

    # Convertir les données en DataFrame
    df = pd.DataFrame(data)

    # Sauvegarder dans un fichier CSV
    df.to_csv("finance_report.csv", mode="a", header=False, index=False)
    print("\nDonnées sauvegardées dans le fichier 'finance_report.csv'.")

def calculate_remaining_budget(income, expenses):
    total_expenses = sum(expenses.values())
    remaining = income - total_expenses
    return total_expenses, remaining

def main():
    # Collecte des données de l'utilisateur
    name, income, month, expenses = get_user_input()

    if name is None:  # Si le mois était invalide, on arrête le programme
        return

    # Calcul du total des dépenses et du reste
    total_expenses, remaining = calculate_remaining_budget(income, expenses)

    # Sauvegarde des données dans un fichier CSV
    save_to_csv(name, income, month, expenses, total_expenses, remaining)

if __name__ == "__main__":
    main()