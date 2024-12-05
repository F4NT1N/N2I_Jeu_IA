import random
from classes import *
GRID_HEIGHT = 8
GRID_WIDTH = 6

class model:

    def __init__(self):
        # joueur 1, joueur2
        self.player1 = Player(1)
        self.player2 = Player(2)

        self.pieces_p1 = [Piece_destructor(1, GRID_HEIGHT-1, 1), Piece_explorator(3, GRID_HEIGHT-1, 1), Piece_protector(4, GRID_HEIGHT-1, 1)] # [pions joueur1] (3)
        self.pieces_p2 = [Piece_destructor(4, 0, 2), Piece_explorator(2, 0, 2), Piece_protector(1, 0, 2)]  # [pions joueur2] (3)

        all_coordinates = [(x, y) for x in range(GRID_WIDTH) for y in range(1, GRID_HEIGHT-1)]
        selected_coordinates = random.sample(all_coordinates, 6)
        self.resources = [Ressource(selected_coordinates[i][0], selected_coordinates[i][1]) for i in range(3)] # [ressources] (3)
        self.zones = [Zone(selected_coordinates[i][0], selected_coordinates[i][1]) for i in range(3, 6)]# [zones] (3)
        
        self.selected_piece = None # piece séléctionnée
        self.round = 0


    # choisir la case pour obtenir les coups possibles de la piece
    def cell_clicked(self, x, y):
        
        # si la case cliquée possède une pièce du joueur, changer la piece selectionné. et return ses positions possibles
        if self.selected_piece == None:
            for p in self.pieces_p1 if self.round % 2 == 0 else self.pieces_p2:
                if p.pos_x == x and p.pos_y == y:
                    self.selected_piece = p
                    return self.possible_moves(p)
        else:
            # créer une liste de positions possibles de la pièces
            possible_moves = self.possible_moves(self.selected_piece)
    
            # si la nouvelle position n'est pas dans les positions possibles, mettre la pièce sélectionnée à None et vider positions possibles
            if (x,y) not in possible_moves:
                self.selected_piece = None
                return []
            # si la nouvelle position est dans les pos possibles, faire l'action demandée
            else:
                if type(self.selected_piece).__name__() != "Piece_explorator":
                    if (x,y) in self.pieces_p2 if self.round % 2 == 0 else self.pieces_p1: 
                        # si on clique sur une piece adverse dans les pos possibles, on utilise la capacité
                        self.use_ability()
                    else:
                        self.selected_piece.pos_x = x
                        self.selected_piece.pox_y = y

                self.selected_piece = None
                return []
    
    
    def possible_moves(self,piece):
        x = piece.pos_x
        y = piece.pos_y
        if type(piece).__name__() == "Piece_explorator" :
            positions = [
                (x-1, y),(x-2, y)
                (x+1, y),(x+2, y)
                (x, y-1),(x, y-2)
                (x, y+1),(x, y+2),
                (x+1, y+1),(x+1, y-1),
                (x-1, y+1), (x-1, y+1)
            ]

            opponent_pieces = self.pieces_p1 if round % 2 == 1 else self.pieces_p2
            positions = [(x,y) for x, y in positions if x == p.pos_x and y == p.pos_y for p in opponent_pieces]
        else:
            positions = [
                (x-1, y),
                (x+1, y),
                (x, y-1),
                (x, y+1)
            ]

            return [(x, y) for x, y in positions if 0 <= x <  GRID_WIDTH and 0 <= y < GRID_HEIGHT]

        


    def use_ability(self):
        if self.selected_piece != None:
            # faire l'action en fonction de la pièce sélectionnée. 
            pass

        pass

    def next(self):
        round += 1
        # modifier les valeurs de neutralized des joueurs et de reset des zones en fonctions de la position des joueurs
        # renvoie un booléen si la partie est terminée ou pas.



        
