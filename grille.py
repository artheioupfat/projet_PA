from jeton import Jeton

class Grille:
    def __init__(self):
        self.grid = [[Jeton() for _ in range(7)] for _ in range(6)]

    def afficher_grille(self):
        for row in self.grid:
            print('|  '.join(str(cell) for cell in row))
        print('-' * 29)                        # Après avoir affiché toutes les lignes de la grille, une ligne de séparation est affichée. Cela ajoute une ligne horizontale de 29 caractères '-' pour séparer visuellement les différentes lignes de la grille.

    def est_colonne_valide(self, colonne):
        return 0 <= colonne < 7 and self.grid[0][colonne].occupant is None    #verifie si on ne choisit pas une colonne qui n'existe pas et on vérifie également qu'il reste une place

    def placer_jeton(self, colonne, joueur):     #cherche si le placement est possible et si oui placel'empreinte du joueur
        if self.est_colonne_valide(colonne):
            # Trouver la première cellule vide dans la colonne
            for row in range(5, -1, -1):
                if self.grid[row][colonne].occupant is None:      #À chaque itération de la boucle, la condition vérifie si la cellule à la position actuelle est vide (None). Si c'est le cas, cela signifie qu'il y a de la place pour placer un jeton dans cette cellule.
                    self.grid[row][colonne].placer(joueur)        #Si une cellule vide est trouvée, la méthode placer de la classe Jeton est appelée pour placer le jeton du joueur dans cette cellule
                    return True  # Le placement du jeton est réussi
        print("Colonne remplie ou inexistante")
        return False # La colonne est pleine



