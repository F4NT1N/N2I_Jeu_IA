
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

        # si la case cliquée possède une pièce, changer la piece selectionné. et return ses positions possibles
        
        if self.selected_piece != None:
            # créer une liste de positions possibles de la pièces
            # si la nouvelle position n'est pas dans les positions possibles, mettre la pièce sélectionnée à None et vider positions possibles 
            # si la nouvelle positoin est dans les pos possibles, déplacer la pièce puis vérifier si une piece 
            
            pass
        
        return [] # renvoyer les positions possibles
        


    def use_ability(self):
        if self.selected_piece != None:
            # faire l'action en fonction de la pièce sélectionnée. 
            pass

        pass

    def next(self):
        round += 1
        # modifier les valeurs de neutralized des joueurs et de reset des zones en fonctions de la position des joueurs
        # renvoie un booléen si la partie est terminée ou pas.



        
