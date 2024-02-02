import pygame
import os
from pygame.locals import *
from jeu import Jeu

class GameView:
    IMAGE_DIRECTORY = "images"

    def __init__(self):
        self.ma_classe_jeu = Jeu()
        self.pyGame = pygame

        # État du bouton (clicqué ou non)
        self.button_clicked = False

        # initialiser l'interface
        pygame.init()
        # charger l'image du plateau de jeu
        self.board_picture = pygame.image.load(os.path.join(GameView.IMAGE_DIRECTORY, "plateau.png"))

        # obtenir la taille du plateau de jeu
        taille_plateau_de_jeu = self.board_picture.get_size()
        print(taille_plateau_de_jeu)
        # stocker cette taille
        self.size = (taille_plateau_de_jeu[0] * 1, taille_plateau_de_jeu[1])
        self.colonne = taille_plateau_de_jeu[0]/7
        # Définir les limites des colonnes
        self.limites_colonnes = [i * self.colonne for i in range(8)]
        # setter la taille de la fenetre jeu au meme dimension que celle du plateau de jeu (image)
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(self.board_picture, (0, 0))
        pygame.display.flip()

        # charger l'image du pion jaune
        self.yellowChip = pygame.image.load(os.path.join(GameView.IMAGE_DIRECTORY, "pion_jaune.png"))
        # charger l'image du pion rouge
        self.redChip = pygame.image.load(os.path.join(GameView.IMAGE_DIRECTORY, "pion_rouge.png"))
        # Police pour le jeu
        self.font = pygame.font.Font("freesansbold.ttf", 30)
        self.pions_colonnes = {i: [] for i in range(7)}
        #692, 701 taille plateau 2
        #346, 350,5 milieux plateau 2
        jeu = Jeu()
        continuer = True
        while continuer:
            message_nul = self.font.render("Puissance 4", True, (255, 0, 0))  # Couleur du texte : Noir
            self.screen.blit(message_nul, (20, 30))
            message_nul = self.font.render("Tour du joueur :", True, (255, 255, 255))  # Couleur du texte : Noir
            self.screen.blit(message_nul, (300, 30))

            pygame.display.update()
            for event in self.pyGame.event.get():
                if event.type == QUIT:
                    continuer = False
                elif event.type == MOUSEBUTTONDOWN:

                    if jeu.victoire == 0:
                        self.rouge_jaune()
                        # Vérifier dans quelle colonne la souris a été cliquée
                        x, y = event.pos
                        colonne_cliquee = self.get_colonne_cliquee(x)
                        self.placer_pion(colonne_cliquee - 1)
                        jeu.jouer(colonne_cliquee - 1)
                        jeu.grille.afficher_grille()  # Afficher la grille après la dernière action
                        print(f"Colonne cliquée : {colonne_cliquee}")
                    else:
                        if jeu.est_victoire():
                            print(f"Le joueur {jeu.joueur_actuel.nom} remporte la victoire !")
                            self.message_victoire()
                            self.bouton_rejouer()
                            # Utilisez une boucle while True pour vérifier en permanence le clic sur le bouton "Rejouer"
                            while True:
                                if self.clic_rejouer():
                                    # Réinitialiser le jeu
                                    GameView()
                                    break  # Sortez de la boucle while True après avoir effectué l'action

                            pygame.display.update()
                        if jeu.est_match_nul():
                            print("Match nul ! La grille est pleine.")
                            message_nul = self.font.render("Match nul ! La grille est pleine !", True,
                                                           (255, 255, 255))  # Couleur du texte : rouge
                            self.screen.blit(message_nul, (150, 290))
                            self.bouton_rejouer()
                            # Utilisez une boucle while True pour vérifier en permanence le clic sur le bouton "Rejouer"
                            while True:
                                if self.clic_rejouer():
                                    # Réinitialiser le jeu
                                    # self.reinitialiser_jeu()
                                    break  # Sortez de la boucle while True après avoir effectué l'action

                            pygame.display.update()


        pygame.quit()

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

        # Trouver la position verticale libre dans la colonne
        positions_verticales = self.pions_colonnes[colonne]
        hauteur_pion = self.yellowChip.get_height()


        y = self.size[1] - self.yellowChip.get_height() - 10 if not positions_verticales else min(positions_verticales, key=lambda pos: pos[1])[1] - hauteur_pion - 16


        if y >= 110:
            # Ajouter les coordonnées à la liste des pions dans cette colonne
            self.pions_colonnes[colonne].append((x, y))

            # Afficher tous les pions dans cette colonne
            joueur_actuel = self.ma_classe_jeu.joueur_actuel
            colonne_a_afficher = self.pions_colonnes[colonne]

            for i, (pion_x, pion_y) in enumerate(colonne_a_afficher):
                if joueur_actuel == self.ma_classe_jeu.joueur1:
                    couleur = self.redChip
                    if i == len(colonne_a_afficher) - 1:  # Vérifier si c'est le dernier pion ajouté
                        self.screen.blit(couleur, (pion_x, pion_y))
                elif joueur_actuel == self.ma_classe_jeu.joueur2:
                    couleur = self.yellowChip
                    if i == len(colonne_a_afficher) - 1:  # Vérifier si c'est le dernier pion ajouté
                        self.screen.blit(couleur, (pion_x, pion_y))

            pygame.display.flip()

            self.ma_classe_jeu.changer_joueur()

    def bouton_rejouer(self):
        couleur = (195, 195, 195)
        pygame.draw.rect(self.screen, couleur,
                         (346-75, 350.5-10, 150, 30))
        message_rejouer = self.font.render(
            f"REJOUER", True,
            (255, 255, 255))  # Couleur du texte : rouge
        self.screen.blit(message_rejouer, (346-75, 350.5-10))
        pygame.display.flip()

    def clic_rejouer(self):
        for event in self.pyGame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                print(x,y)
                if 346 - 75 <= x <= 346 - 75 + 150 and 350.5 - 10 <= y <= 350.5 - 10 + 30:
                    print("Bouton REJOUER cliqué !")
                    return True
        return False

    def message_victoire(self):
        jeu = Jeu()
        couleur = (195, 195, 195)
        pygame.draw.rect(self.screen, couleur,
                         (75, 300, 550, 35))
        message_victoire = self.font.render(
            f"Le joueur {jeu.joueur_actuel.nom} remporte la victoire !", True,
            (255, 255, 255))  # Couleur du texte : rouge
        self.screen.blit(message_victoire, (75, 300))

    def rouge_jaune(self):
        jeu = Jeu()
        if self.ma_classe_jeu.joueur_actuel == self.ma_classe_jeu.joueur1:  # sert à afficher le nom de la personne qui doit jouer
            pygame.draw.rect(self.screen, (195, 195, 195,), (550, 30, 120, 40))
            pygame.display.flip()
            message_nul = self.font.render(f" {jeu.joueur2.nom}", True, (255, 255, 0))
            self.screen.blit(message_nul, (560, 30))

        else:
            pygame.draw.rect(self.screen, (195,195,195), (550, 30, 120, 40))
            pygame.display.flip()
            message_nul = self.font.render(f"{jeu.joueur1.nom}", True, (255, 0, 0))
            self.screen.blit(message_nul, (565, 30))
        return