import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.linspace(0, 10, 1000)
y = np.sin(x)

sns.set()
plt.style.use("seaborn-whitegrid")
plt.plot(x, y)
plt.title("Sinus")

# jeu de données iris importé directement de seaborn
iris = sns.load_dataset("iris")

iris.head()
# comme on le voit, iris contient des données sur la longueur, largeur des sépales et pétales de 3 espèces d'iris

# analyse pair à pair des graph
sns.pairplot(iris, hue="species", height=2.5)
""" 
La diagonale est traitée différemment, variable en fonction d'elle-même...
À la place,  sns.pairplot  trace un graph des données en fonction de 
la variable en question pour chaque classe de données.
"""

# distribution jointe de deux caractéristiques
with sns.axes_style('white'):
    sns.jointplot(x="petal_length", y="petal_width", data=iris, kind='reg')

plt.show()
