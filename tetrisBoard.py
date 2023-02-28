from tetrisPiece import TetrisPiece


class TetrisBoard:
    def __init__(self, width, height, piece):
        self.width = width
        self.height = height
        self.pieces = [piece]
        self.board = [[0 for _ in range(width)] for _ in range(height)]

    def can_move(self, direction):
        falling_piece = self.pieces[-1]
        pos_x = falling_piece.get_pos_x()
        pos_y = falling_piece.get_pos_y()
        for i in range(len(falling_piece.get_piece()[0])):
            for j in range(len(falling_piece.get_piece())):
                if falling_piece.get_piece()[j][i] == 1 and (pos_x + i + direction < 0 or pos_x + i + direction > self.width - 1):
                    return False
                elif falling_piece.get_piece()[j][i] == 1 and self.board[pos_y + j][pos_x + i + direction] == 1:
                    return False
        return True

    def can_rotate(self):
        falling_piece = self.pieces[-1]
        pos_x = falling_piece.get_pos_x()
        pos_y = falling_piece.get_pos_y()
        next_rotation_idx = falling_piece.get_next_rotation_idx()
        rotated_piece = falling_piece.get_rotations()[next_rotation_idx]
        for i in range(len(rotated_piece[0])):
            for j in range(len(rotated_piece)):
                if rotated_piece[j][i] == 1 and (pos_x + i < 0 or pos_x + i > self.width - 1):
                    return False
                elif rotated_piece[j][i] == 1 and self.board[pos_y + j][pos_x + i] == 1:
                    return False
        return True

    def no_collision(self):
        falling_piece = self.pieces[-1]
        pos_x = falling_piece.get_pos_x()
        pos_y = falling_piece.get_pos_y()
        for i in range(len(falling_piece.get_piece()[0])):
            for j in range(len(falling_piece.get_piece())):
                if falling_piece.get_piece()[j][i] == 1 and self.board[pos_y + j][pos_x + i] == 1:
                    return False
        return True

    def move_left(self):
        pos_x = self.pieces[-1].get_pos_x()
        if self.can_move(-1):
            self.pieces[-1].set_pos_x(pos_x - 1)
        else:
            self.move_down()

    def move_right(self):
        pos_x = self.pieces[-1].get_pos_x()
        if self.can_move(1):
            self.pieces[-1].set_pos_x(pos_x + 1)
        else:
            self.move_down()

    def move_down(self):
        pos_y = self.pieces[-1].get_pos_y()
        if self.max_drop_dist(self.pieces[-1]) > 1:
            self.pieces[-1].set_pos_y(pos_y + 1)
        elif self.max_drop_dist(self.pieces[-1]) == 1:
            self.pieces[-1].set_pos_y(pos_y + 1)
            self.spawn_new_piece()
        else:
            self.spawn_new_piece()

    def rotate_piece(self):
        falling_piece = self.pieces[-1]
        if self.can_rotate():
            falling_piece.rotate()
        else:
            self.move_down()

    def get_highest_per_column(self):
        highest = [self.height for _ in range(self.width)]
        for i in range(self.width):
            print(self.pieces[-1].get_pos_y())
            for j in range(self.pieces[-1].get_pos_y(), self.height):
                if self.board[j][i] == 1:
                    highest[i] = j
                    break
        return highest

    def max_drop_dist(self, falling_piece):
        lowest = falling_piece.get_lowest_per_column()
        highest = self.get_highest_per_column()[falling_piece.get_pos_x():falling_piece.get_pos_x() + falling_piece.get_width()]
        min_dist = self.height
        for i in range(falling_piece.get_width()):
            dist = highest[i] - lowest[i] - falling_piece.get_pos_y()
            if dist < min_dist:
                min_dist = dist
        return min_dist - 1

    def drop_piece(self):
        falling_piece = self.pieces[-1]
        drop_dist = self.max_drop_dist(falling_piece)
        falling_piece.set_pos_y(falling_piece.get_pos_y() + drop_dist)
        self.spawn_new_piece()

    def update_board(self, pos_x, pos_y, val):
        self.board[pos_y][pos_x] = val

    def fix_piece_on_board(self, piece):
        for i in range(len(piece.get_piece())):
            for j in range(len(piece.get_piece()[0])):
                if piece.get_piece()[i][j] == 1:
                    self.update_board(piece.get_pos_x() + j, piece.get_pos_y() + i, 1)

    def print_board(self):
        print(self.board)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_pieces(self):
        return self.pieces

    def get_board(self):
        return self.board

    def delete_complete_rows(self):
        to_insert = [0 for _ in range(self.width)]
        row = self.height - 1
        while row >= 0:
            deleted = False
            for col in range(self.width):
                if self.board[row][col] == 0:
                    break
                if col == self.width - 1 and self.board[row][col] == 1:
                    del self.board[row]
                    self.board.insert(0, to_insert)
                    deleted = True
            if not deleted:
                row -= 1

    def spawn_new_piece(self):
        falling_piece = self.pieces[-1]
        self.fix_piece_on_board(falling_piece)
        self.delete_complete_rows()
        new_piece = TetrisPiece(TetrisPiece.generate_piece())
        self.pieces.append(new_piece)






