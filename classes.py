class Piece:
    def __init__(self, x : int, y : int, id_joueur : int):
        self.pos_x = x
        self.pos_y = y
        self.id_joueur = id_joueur
        self.neutralized = False


class Piece_protector(Piece):
    def move(self, x : int, y : int):
        self.pos_x = x
        self.pos_y = y

        
class Piece_explorator(Piece):
    def move(self, x : int, y : int):
        self.pos_x = 2*x
        self.pos_y = 2*y


class Piece_destructor(Piece):
    def move(self, x : int, y : int):
        self.pos_x = x
        self.pos_y = y


class Player:
	def __init__(self, id : int):
		self.id = id
		self.points = 0


class Ressource:
	def __init__(self,x : int,y : int):
		self.pos_x = x
		self.pos_y = y


class Zone:
	def __init__(self,x : int,y : int):
		self.pos_x = x
		self.pos_y = y
		self.remain = 3