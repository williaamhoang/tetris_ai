import numpy as np
import random

BOARD_HEIGHT = 20
BOARD_WIDTH = 10


class TetrisEnv:
    def __init__(self):
        self.board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH), dtype=int)
        self.current_piece = self.get_new_piece()

    def get_new_piece(self):
        return random.choice(['I', 'O', 'T', 'S', 'Z', 'J', 'L'])
