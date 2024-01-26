import pygame
import os
from pygame.locals import *
from jeu import Jeu

class GameView:
    IMAGE_DIRECTORY = "images"

    def __init__(self):
        self.gamer = 1
        #self.gameBoard = GameBoard()
        self.pyGame = pygame

        # initialiser l'interface
        # utiliser la librairie pygame
        pygame.init()
        # charger l'image du plateau de jeu
        self.board_picture = pygame.image.load(os.path.join(GameView.IMAGE_DIRECTORY, "plateau.png"))

        # obtenir la taille du plateau de jeu
        taille_plateau_de_jeu = self.board_picture.get_size()
        # stocker cette taille
        self.size = (taille_plateau_de_jeu[0] * 1, taille_plateau_de_jeu[1])
        #print(self.size)
        self.colonne = taille_plateau_de_jeu[0]/7
        #print(self.colonne)
        # Définir les limites des colonnes
        self.limites_colonnes = [i * self.colonne for i in range(8)]
        #print(self.limites_colonnes)
        # setter la taille de la fenetre jeu au meme dimension que celle du plateau de jeu (image)
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(self.board_picture, (0, 0))
        pygame.display.flip()

        # charger l'image du pion jaune
        self.yellowChip = pygame.image.load(os.path.join(GameView.IMAGE_DIRECTORY, "pion_jaune.png"))
        # charger l'image du pion rouge
        self.redChip = pygame.image.load(os.path.join(GameView.IMAGE_DIRECTORY, "pion_rouge.png"))
        # Police pour le jeu
        self.font = pygame.font.Font("freesansbold.ttf", 15)

        self.pions_colonnes = {i: [] for i in range(7)}

        jeu = Jeu()
        continuer = True
        while continuer:
            for event in self.pyGame.event.get():
            #for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = False
                elif event.type == MOUSEBUTTONDOWN:
                    # Vérifier dans quelle colonne la souris a été cliquée
                    x, y = event.pos
                    colonne_cliquee = self.get_colonne_cliquee(x)
                    self.placer_pion(colonne_cliquee-1)
                    jeu.jouer(colonne_cliquee-1)
                    jeu.grille.afficher_grille()  # Afficher la grille après la dernière action
                    print(f"Colonne cliquée : {colonne_cliquee}")

        pygame.quit()


        '''
        while True:
            jeu.grille.afficher_grille()

            # colonne = int(input(f"Joueur {jeu.joueur_actuel.symbole}, choisissez une colonne (0-6) : "))
            colonne = colonne_cliquee
            print("Colonne clique {colonne}")
            if jeu.jouer(colonne):
                jeu.grille.afficher_grille()  # Afficher la grille après la dernière action
                break  # Le jeu est terminé, sortir de la boucle

        print("Fin du jeu.")
        '''
    def get_colonne_cliquee(self, x):
        # Trouver la colonne dans laquelle la souris a été cliquée
        for i, limite in enumerate(self.limites_colonnes):
            if x < limite:
                return i
        num_colonne_clic = len(self.limites_colonnes) - 1
        return num_colonne_clic

    def placer_pion(self, colonne):
        # Calculer les coordonnées pour placer l'image en bas de la colonne
        x = colonne * self.colonne + (self.colonne // 2) - (self.yellowChip.get_width() // 2) + 3
        #y = self.size[1] - self.yellowChip.get_height()

        # Trouver la position verticale libre dans la colonne
        positions_verticales = self.pions_colonnes[colonne]
        hauteur_pion = self.yellowChip.get_height()

        #y = positions_verticales
        y = self.size[1] - self.yellowChip.get_height() - 10 if not positions_verticales else min(positions_verticales, key=lambda pos: pos[1])[1] - hauteur_pion - 16

        # Ajouter les coordonnées à la liste des pions dans cette colonne
        self.pions_colonnes[colonne].append((x, y))

        # Afficher tous les pions dans cette colonne
        for pion_x, pion_y in self.pions_colonnes[colonne]:
            self.screen.blit(self.yellowChip, (pion_x, pion_y))

        # Afficher l'image du pion (jaune pour l'exemple)
        #self.screen.blit(self.yellowChip, (x, y))
        pygame.display.flip()
