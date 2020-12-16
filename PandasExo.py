from urllib import request
# The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker
sns.set()

"""
Faire une carte de vœux pour chaque jour de la semaine avec un nombre d'années pré-inscrit.
Le nombre va dépendre du nombre de naissances de la bdd
"""

# importation de données de naissance aux États-Unis
request.urlretrieve("https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv", "births.csv")
births = pd.read_csv("births.csv")

print(births.describe())  # check
print(births.head())  # check

# rajoute une collone avec la décade pour trier les données
births['decade'] = 10 * (births['year'] // 10)

plt.figure(figsize=(11, 8))
sns.boxplot(x=births.births)  # affiche la distribution des nombres de naissances de la bdd
plt.title("Nombre de naissance")
plt.show()

# on vire les valeurs abérantes
# births = births.dropna()
births = births.query('(births > 1000) & (births < 100000)')
# Query (requête) the columns of a DataFrame avec une expression booléénne
plt.figure(figsize=(11, 8))
sns.boxplot(x=births.births)
plt.show()

print(births.info())  # check

# le but de la prochaine manip est de mettre le format jour en fonction de la date
# on doit tout mettre en int pour la fonction datetime
for field in ["day", "month", "year"]:
    births[field] = births[field].astype(int)

# create a datetime index from the year, month, day
births.index = pd.to_datetime(10000 * births.year + 100 * births.month + births.day, format='%Y%m%d')
births['dayofweek'] = births.index.dayofweek

print(births.head())  # check


# nombre de naissance par jour
births_per_day = births.pivot_table('births', index='dayofweek', columns='decade', aggfunc='sum')
births_per_day.plot(figsize=(11, 8))
ticks_loc = plt.gca().get_xticks().tolist()
plt.gca().xaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
plt.gca().set_xticklabels(['', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', ''])
plt.ylabel('Births per day')
plt.show()

"""
On part de 69, on a donc peut de données des années 60 donc rien d'anormal
On peut aussi regarder la moyenne des naissances qui va lisser la différence 
pour avoir une prédiction pour les années 60
"""

births_per_day = births.pivot_table('births', index='dayofweek', columns='decade', aggfunc='mean')
births_per_day.plot(figsize=(11, 8))
ticks_loc = plt.gca().get_xticks().tolist()
plt.gca().xaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
plt.gca().set_xticklabels(['', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', ''])
plt.ylabel('Births per day')
plt.show()
