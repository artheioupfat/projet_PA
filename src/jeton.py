class Jeton:
    def __init__(self):
        self.occupant = None

    def placer(self, joueur):
        self.occupant = joueur.symbole

    def __str__(self):
        return self.occupant if self.occupant else ' '
