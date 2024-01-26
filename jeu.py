

from grille import Grille
from joueur import Joueur

class Jeu:
    def __init__(self):
        self.grille = Grille()
        self.joueur1 = Joueur('X','Arthur')
        self.joueur2 = Joueur('O','Alexis')
        self.joueur_actuel = self.joueur1
        self.tour = 1

    def changer_joueur(self):
        self.joueur_actuel = self.joueur2 if self.joueur_actuel == self.joueur1 else self.joueur1
        return self.joueur_actuel



    def jouer(self, colonne):
        if self.grille.est_colonne_valide(colonne):
            if self.grille.placer_jeton(colonne, self.joueur_actuel):
                if self.est_victoire():
                    print(f"Le joueur {self.joueur_actuel.symbole} remporte la victoire !")
                    return True
                elif self.est_match_nul():
                    print("Match nul ! La grille est pleine.")
                    return True
                else:
                    self.tour += 1
                    self.changer_joueur()
                return False
            else:
                print("La colonne est pleine. Choisissez une autre colonne.")
                return False
        else:
            print("Colonne invalide. Choisissez une colonne entre 0 et 6.")
            return False


    def est_victoire(self):
        # Vérification des alignements horizontaux
        for row in range(6):
            for col in range(4):
                if all(self.grille.grid[row][col + i].occupant == self.joueur_actuel.symbole for i in range(4)):  #Cette ligne utilise une expression générale de compréhension de liste pour créer une liste de valeurs booléennes. Ces valeurs booléennes indiquent si les jetons dans la séquence spécifiée (de la colonne col à col + 3 inclus) appartiennent tous au joueur actuel.
                    return True

        # Vérification des alignements verticaux
        for col in range(7):
            for row in range(3):
                if all(self.grille.grid[row + i][col].occupant == self.joueur_actuel.symbole for i in range(4)):
                    return True

        # Vérification des alignements diagonaux (ascendants)
        for row in range(3, 6):
            for col in range(4):
                if all(self.grille.grid[row - i][col + i].occupant == self.joueur_actuel.symbole for i in range(4)):
                    return True

        # Vérification des alignements diagonaux (descendants)
        for row in range(3):
            for col in range(4):
                if all(self.grille.grid[row + i][col + i].occupant == self.joueur_actuel.symbole for i in range(4)):
                    return True

        return False

    def est_match_nul(self):
        for row in self.grille.grid:
            for cell in row:
                if cell.occupant is None:
                    return False  # Il y a au moins une cellule vide, le match nul n'est pas atteint
        return True  # Toutes les cellules sont occupées, le match nul est atteint