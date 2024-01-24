from jeton import Jeton
from joueur import Joueur
from fenetre import GameView
from jeu import Jeu
'''
jeton_rouge = Jeton("rouge")
jeton_jaune = Jeton("jaune")

print(jeton_rouge) # Affiche: Jeton de couleur rouge
print(jeton_jaune) # Affiche: Jeton de couleur jaune

joueur_1 = Joueur("1")
joueur_2 = Joueur("2")

print(joueur_1)
print(joueur_2)

joueur_1 = Joueur(nom="1", couleur="rouge")
joueur_2 = Joueur(nom="2", couleur="jaune")

joueur_1.creer_jetons(nombre_jetons=21)
joueur_2.creer_jetons(nombre_jetons=21)

print(joueur_1)
print(joueur_2)

def main():
    jeu_puissance4 = Puissance4()
    jeu_puissance4.commencer_partie()

if __name__ == "__main__":
    main()
'''


jeu = Jeu()
game_view = GameView()
while True:
    jeu.grille.afficher_grille()

    #colonne = int(input(f"Joueur {jeu.joueur_actuel.symbole}, choisissez une colonne (0-6) : "))
    colonne = game_view.get_colonne_cliquee()
    print("Colonne clique {colonne}")
    if jeu.jouer(colonne):
        jeu.grille.afficher_grille()  # Afficher la grille après la dernière action
        break  # Le jeu est terminé, sortir de la boucle

print("Fin du jeu.")
