
GRID_HEIGHT = 8
GRID_WIDTH = 6

class model:

    def __init__(self):
        # [pions joueur1] (3)
        # [pions joueur2] (3)
        # joueur 1, joueur2
        # [ressources] (3)
        # [zones] (3)
        self.selected_piece = None # piece séléctionnée
        self.round = 0

        # positionner les pions sur les cases de la lignes 1 ou 2
        
        # positionner les ressources et les zones aléatoirement,
        # seulement aux endroits libres et aux cases centrales



    # choisir la case pour obtenir les coups possibles de la piece
    def case_click(self, x, y):

        # si la case cliquée possède une pièce, changer la piece selectionné.
        
        if self.selected_piece != None:
            # créer une liste de positions possibles de la pièces
            # si la nouvelle position n'est pas dans les positions possibles, mettre la pièce sélectionnée à None
            # si la nouvelle positoin est dans les pos possibles, déplacer la pièce
            pass

        return [] # liste de nouvelle position possible de la pièce


    def use_ability(self):
        pass


        
