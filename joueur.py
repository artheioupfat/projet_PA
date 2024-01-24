from jeton import Jeton

class Joueur:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur
        self.jetons = []  # Liste pour stocker les jetons du joueur

    def creer_jetons(self, nombre_jetons):
        # Méthode pour créer le nombre spécifié de jetons pour le joueur
        for _ in range(nombre_jetons):
            self.jetons.append(Jeton(couleur = self.couleur))

    def __str__(self):
        return f"Joueur n°{self.nom} - {self.couleur}"

'''
class Joueur:
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return f"Joueur n°{self.nom}"
'''