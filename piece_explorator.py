import piece
class piece_explorator(piece):
    def move(self, x, y):
        self.pos_x = 2*x
        self.pos_y = 2*y