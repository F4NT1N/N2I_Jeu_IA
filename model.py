import random
from classes import *
GRID_HEIGHT = 8
GRID_WIDTH = 6

class model:

    def __init__(self):
        # joueur 1, joueur2
        player1 = Player(1)
        player2 = Player(2)

        pieces_p1 = [Piece_destructor(1, GRID_HEIGHT-1, 1), Piece_explorator(3, GRID_HEIGHT-1, 1), Piece_protector(4, GRID_HEIGHT-1, 1)] # [pions joueur1] (3)
        pieces_p2 = [Piece_destructor(4, 0, 2), Piece_explorator(2, 0, 2), Piece_protector(1, 0, 2)]  # [pions joueur2] (3)

        all_coordinates = [(x, y) for x in range(GRID_WIDTH) for y in range(1, GRID_HEIGHT-1)]
        selected_coordinates = random.sample(all_coordinates, 6)
        resources = [Ressource(selected_coordinates[i][0], selected_coordinates[i][1]) for i in range(3)] # [ressources] (3)
        zones = [Zone(selected_coordinates[i][0], selected_coordinates[i][1]) for i in range(3, 6)]# [zones] (3)
        
        self.selected_piece = None # piece séléctionnée
        self.round = 0



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



        
