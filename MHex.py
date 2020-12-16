# Comme toujours, check les docs pour plus d'info
from random import randint, seed  # int rand, customize random
from enum import Enum
# Structure de données d'un ensemble d'e nommés. Une Var de ce type peut com valeur un de ces e
import matplotlib.pyplot as plt

"""wiki : "Le problème de Monty Hall est un casse-tête probabiliste librement inspiré du jeu télévisé
 américain Let's Make a Deal."
3 portes --> un choix
on retire une des 2 portes restantes (toujours une porte vide ofc) 
--> le joueur peux choisir de conserver sa porte ou d'en changer.
MHex démontre que la proba de gagner est plus grande quand on change de porte.  
"""


class Strategy(Enum):
    Change = 1
    Keep = 2

# dans une version plus propre, on peut mettre les fonction dans un .py
# from "file".py import function(arguments)


def play_game(strategy):
    """
    Choix d"une porte par le joueur
    Elimination d'une porte
    choix final.

    argument :
        strategy (Strategy): change ou keep

    Returns:
        booléen: Le joueur gange ?
    """

    doors = [0, 1, 2]

    right_door = randint(0, 2)

    # Choix du joueur
    first_choice = randint(0, 2)

    # retrait de la liste
    doors.remove(first_choice)

    # Le présentateur élimine une porte
    if first_choice == right_door:
        doors.remove(doors[randint(0, 1)])
    else:
        doors = [right_door]

    # Le deuxieme choix depend de la Strategy
    if strategy == Strategy.Change:
        second_choice = doors[0]
    elif strategy == Strategy.Keep:
        second_choice = first_choice
    else:
        raise ValueError("Stratégie non reconnue !")

    return second_choice == right_door


def play(strategy, nb_tours):
    """
    Simule plusieurs parties.
    Retourne plusieurs parties sous forme d'une liste de gains par le joueur.

    arguments :
        strategy (Strategy): La strategy du joueur (garder ou changer)
        nb_tours (int): Nombre de tours

    Returns:
        list: Liste des gains du joueurs à chaque partie
    """

    # Liste en compréhension. check le cours "Apprenez à programmer en Python" sur OpenClassrooms
    # return [1 if play_game(strategy) else 0 for i in range(nb_tours)]
    return [int(play_game(strategy)) for _ in range(nb_tours)]


seed(4)  # test random similaire

print("En changeant de porte, le joueur a gagné {} sur 10000 parties."
      .format(sum(play(Strategy.Change, 10000))))

print("En gardant son choix initial, le joueur a gagné {} sur 10000 parties."
      .format(sum(play(Strategy.Keep, 10000))))

plt.figure()
plt.plot(play(Strategy.Keep, 100))
plt.title("Tirages")

plt.figure()
plt.bar([1, 2], [sum(play(Strategy.Change, 10000)), sum(play(Strategy.Keep, 10000))],
        tick_label=["Changement de porte", "Garder la même porte"])
plt.title("Nombre de réussites")
plt.show()
