

from jeu import Jeu
from grille import Grille
from joueur import Joueur
from fenetre import GameView

'''
if __name__ == "__main__":
    grille = Grille()
    joueur1 = Joueur('X')
    joueur2 = Joueur('O')

    grille.afficher_grille()

    colonne = int(input(f"{joueur1.symbole}, choisissez une colonne (0-6) : "))
    grille.placer_jeton(colonne, joueur1)
    grille.afficher_grille()
'''


def main():
    jeu = Jeu()
    #game_view = GameView()



    while True:
        jeu.grille.afficher_grille()

        try:
            colonne = int(input(f"Joueur {jeu.joueur_actuel.symbole}, choisissez une colonne (0-6) : "))
        except ValueError:
            print("Veuillez entrer un numéro de colonne valide.")
            continue  # Revenir au début de la boucle

        if jeu.jouer(colonne):
            jeu.grille.afficher_grille()
            break  # Le jeu est terminé, sortir de la boucle

    print("Fin du jeu.")



if __name__ == "__main__":
    main()



