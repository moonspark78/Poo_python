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
                
    def search():
        best, candidates = None, None
        minimum = 10
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    b = (r // 3) * 3 + c // 3
                    mask = FULL & ~(rows[r] | cols[c] | boxes[b])
                    options = [i + 1 for i in range(9) if mask & (1 << i)]
                    if not options:
                        return False
                    if len(options) < minimum:
                        best, candidates, minimum = (r, c), options, len(options)
        if best is None:
            return True

        r, c = best
        b = (r // 3) * 3 + c // 3
        for n in candidates:
            bit = 1 << (n - 1)
            board[r][c] = n
            rows[r] |= bit
            cols[c] |= bit