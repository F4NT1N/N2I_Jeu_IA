class Piece:
    def __init__(self, x : int, y : int, player_id : int):
        self.pos_x = x
        self.pos_y = y
        self.player_id = player_id
        self.neutralized = 0


class Piece_protector(Piece):
    def move(self, x : int, y : int):
        self.pos_x = x
        self.pos_y = y
    
    def to_base(self):
        if self.player_id == 1:
            self.pos_x = 4
            self.pos_y = 8
        else:
            self.pos_x = 1
            self.pos_y = 0
        
class Piece_explorator(Piece):
    def move(self, x : int, y : int):
        self.pos_x = 2*x
        self.pos_y = 2*y
    
    def to_base(self):
        if self.player_id == 1:
            self.pos_x = 3
            self.pos_y = 8
        else:
            self.pos_x = 2
            self.pos_y = 0


class Piece_destructor(Piece):
    def move(self, x : int, y : int):
        self.pos_x = x
        self.pos_y = y
    
    def to_base(self):
        if self.player_id == 1:
            self.pos_x = 1
            self.pos_y = 8
        else:
            self.pos_x = 4
            self.pos_y = 0


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