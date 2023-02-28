import random
o = [[[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]],[[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]],[[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]],[[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]]]
i = [[[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]],[[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]]
j = [[[1,0,0,0],[1,1,1,0],[0,0,0,0],[0,0,0,0]],[[1,1,0,0],[1,0,0,0],[1,0,0,0],[0,0,0,0]],[[1,1,1,0],[0,0,1,0],[0,0,0,0],[0,0,0,0]],[[0,1,0,0],[0,1,0,0],[1,1,0,0],[0,0,0,0]]]
l = [[[0,0,1,0],[1,1,1,0],[0,0,0,0],[0,0,0,0]],[[1,0,0,0],[1,0,0,0],[1,1,0,0],[0,0,0,0]],[[1,1,1,0],[1,0,0,0],[0,0,0,0],[0,0,0,0]],[[1,1,0,0],[0,1,0,0],[0,1,0,0],[0,0,0,0]]]
s = [[[0,1,1,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]],[[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,0,0,0]],[[0,1,1,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]],[[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,0,0,0]]]
z = [[[1,1,0,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]],[[0,1,0,0],[1,1,0,0],[1,0,0,0],[0,0,0,0]],[[1,1,0,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]],[[0,1,0,0],[1,1,0,0],[1,0,0,0],[0,0,0,0]]]
t = [[[0,1,0,0],[1,1,1,0],[0,0,0,0],[0,0,0,0]],[[1,0,0,0],[1,1,0,0],[1,0,0,0],[0,0,0,0]],[[1,1,1,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]],[[0,1,0,0],[1,1,0,0],[0,1,0,0],[0,0,0,0]]]


class TetrisPiece:
    def __init__(self, rotations):
        self.piece = rotations[0]
        self.pos_x = 0
        self.pos_y = 0
        self.width = TetrisPiece.calculate_width(self.piece)
        self.rotations = rotations
        self.rotation_idx = 0

    def rotate(self):
        self.rotation_idx = self.get_next_rotation_idx()
        self.piece = self.rotations[self.rotation_idx]
        self.width = TetrisPiece.calculate_width(self.piece)

    def set_pos_x(self, val):
        self.pos_x = val

    def set_pos_y(self, val):
        self.pos_y = val

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def get_piece(self):
        return self.piece

    def get_width(self):
        return self.width

    def get_rotation_idx(self):
        return self.rotation_idx

    def get_next_rotation_idx(self):
        return (self.rotation_idx + 1) % 4

    def get_rotations(self):
        return self.rotations

    def get_lowest_per_column(self):
        lowest = [0 for _ in range(4)]
        for i in range(4):
            for j in reversed(range(4)):
                if self.piece[j][i] == 1:
                    lowest[i] = j
                    break
        return lowest

    @staticmethod
    def generate_piece():
        random_index = random.randint(0, 6)
        pieces = [o, i, j, l, s, z, t]
        return pieces[random_index]

    @staticmethod
    def calculate_width(piece):
        for x in reversed(range(4)):
            for y in range(4):
                if piece[y][x] == 1:
                    return x + 1

