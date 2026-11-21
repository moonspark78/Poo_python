import sys

SIZE = 9
FULL = (1 << 9) - 1

def solve(board):
    rows = [0] * SIZE
    cols = [0] * SIZE
    boxes = [0] * SIZE

    for r in range(SIZE):
        for c in range(SIZE):
            n = board[r][c]
            if n:
                bit = 1 << (n - 1)
                b = (r // 3) * 3 + c // 3
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit