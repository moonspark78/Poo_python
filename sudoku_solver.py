import sys

SIZE = 9
FULL = (1 << 9) - 1

def solve(board):
    rows = [0] * SIZE
    cols = [0] * SIZE
    boxes = [0] * SIZE