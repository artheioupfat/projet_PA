import pygame
import os
from pygame.locals import *


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
        # setter la taille de la fenetre jeu au meme dimension que celle du plateau de jeu (image)
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(self.board_picture, (0, 0))
        pygame.display.flip()

        # charger l'image du pion jaune
        self.yellowChip = pygame.image.load(os.path.join(GameView.IMAGE_DIRECTORY, "pion_jaune.png"))
        # charger l'image du pion rouge
        self.redChip = pygame.image.load(os.path.join(GameView.IMAGE_DIRECTORY, "pion_rouge.png"))
        # Police pour le jeu
        #self.font = pygame.font.Font("freesansbold.ttf", 15)

        continuer = True
        while continuer:
            for event in self.pyGame.event.get():
            #for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = False

        pygame.quit()
#à mettre dans le main pour executer la fenêtre
