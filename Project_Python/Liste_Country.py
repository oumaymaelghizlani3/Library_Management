import csv

chemin_fichier_csv = 'WorldHappiness.csv'
liste_donnees = []
liste_country = []
import csv

chemin_fichier_csv = 'WorldHappiness.csv'
liste_donnees = []
dict_moyennes = {}

# Sauvegarder dans une liste de listes
with open(chemin_fichier_csv, newline='', encoding='utf-8') as fichier_csv:
    lecteur_csv = csv.DictReader(fichier_csv)
    for ligne in lecteur_csv:
        liste_donnees.append([ligne['Country'], ligne['happiness_score'], ligne['freedom'], ligne['gdp_per_capita']])

# Créer un dictionnaire avec les moyennes
for data in liste_donnees:
    country = data[0]
    happiness_score = float(data[1])
    freedom = float(data[2])
    gdp_per_capita = float(data[3])

    if country not in dict_moyennes:
        dict_moyennes[country] = {'Happiness Score': [], 'Freedom': [], 'GDP': []}
    # ['Happiness Score'], ['Freedom'], ['GDP']: Cela accède à la liste spécifique de "Happiness Score", "Freedom" et "GDP" à l'intérieur du sous-dictionnaire associé au pays.
    # .append(): Cela ajoute la valeur actuelle (happiness_score, freedom, gdp_per_capita) à la liste correspondante dans le sous-dictionnaire du pays.
    dict_moyennes[country]['Happiness Score'].append(happiness_score)
    dict_moyennes[country]['Freedom'].append(freedom)
    dict_moyennes[country]['GDP'].append(gdp_per_capita)

# Calculer les moyennes pour chaque pays
for country, values in dict_moyennes.items():
    moyenne_happiness = sum(values['Happiness Score']) / len(values['Happiness Score'])
    moyenne_freedom = sum(values['Freedom']) / len(values['Freedom'])
    moyenne_gdp = sum(values['GDP']) / len(values['GDP'])

    # Mettre à jour le dictionnaire avec les listes de moyennes
    dict_moyennes[country] = [moyenne_happiness, moyenne_freedom, moyenne_gdp]

# Afficher le dictionnaire final
print("Dictionnaire des moyennes par pays:")
print(dict_moyennes)

# Trouver le pays avec les meilleures moyennes sur les 6 années
pays_meilleures_moyennes = max(dict_moyennes, key=lambda x: sum(dict_moyennes[x]))
print(f"\nLe pays avec les meilleures moyennes sur les 6 années est : {pays_meilleures_moyennes}")
