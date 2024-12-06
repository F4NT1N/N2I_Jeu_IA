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
                    for p in self.pieces_p2 if self.round % 2 == 0 else self.pieces_p1:
                        if (p.pos_x, p.pos_y) == (x,y) :
                            # si on clique sur une piece adverse dans les pos possibles, on utilise la capacité
                            self.use_ability(p)
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

        


    def use_ability(self, piece):
        if self.selected_piece != None:
            match type(self.selected_piece).__name__:
                case "Piece_protector":
                    piece.neutralized = 2
                case "Piece_destructor":
                    piece.to_base()

    def next(self):
        round += 1
        if round > 20 : #partie terminée
            return True
        
        # modifier les valeurs de neutralized des pions
        for piece in self.pieces_p1 :
            zone = self.piece_on_zone(piece)
            if piece.neutralized > 0 :
                if piece.neutralized == 2 and zone != None :
                    zone.remain = 3
                piece.neutralized-=1
            if piece.neutralized < 2 and zone != None :
                if zone.remain > 0 :
                    zone.remain -= 1
                else :
                    if piece.player_id == 1 :
                        self.player1.points += 5
                    else :
                        self.player2.points += 5
                    zone.remain = 3
                    self.replace_object(zone)

        # renvoie un booléen si la partie est terminée ou pas
        return False
    
    def replace_object (self, object):
        all_coordinates = [(x, y) for x in range(GRID_WIDTH) for y in range(1, GRID_HEIGHT-1)]
        for piece in self.pieces_p1 :
            if (piece.pos_x, piece.pos_y) in all_coordinates :
                all_coordinates.remove((piece.pos_x, piece.pos_y))
        for piece in self.pieces_p2 :
            if (piece.pos_x, piece.pos_y) in all_coordinates :
                all_coordinates.remove((piece.pos_x, piece.pos_y))
        for piece in self.zones :
            if (piece.pos_x, piece.pos_y) in all_coordinates :
                all_coordinates.remove((piece.pos_x, piece.pos_y))
        for piece in self.resources :
            if (piece.pos_x, piece.pos_y) in all_coordinates :
                all_coordinates.remove((piece.pos_x, piece.pos_y))
        
        new_coordinate  = random.randint(len(all_coordinates)-1)
        object.pos_x = all_coordinates[new_coordinate ][0]
        object.pos_y = all_coordinates[new_coordinate ][1]


    def piece_on_zone(self, piece : Piece):
        if (piece.pos_x, piece.pos_y) == (self.zones[0].pos_x, self.zones[0].pos_y) :
            return self.zone[0]
        elif (piece.pos_x, piece.pos_y) == (self.zones[1].pos_x, self.zones[1].pos_y) :
            return self.zone[1]
        elif (piece.pos_x, piece.pos_y) == (self.zones[2].pos_x, self.zones[2].pos_y) :
            return self.zone[2]
        else :
            return None
        
