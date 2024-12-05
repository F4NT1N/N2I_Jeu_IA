class piece:
    def __init__(self, x, y, id_joueur):
        self.pos_x = x
        self.pos_y = y
        self.id_joueur = id_joueur
        self.neutralized = False