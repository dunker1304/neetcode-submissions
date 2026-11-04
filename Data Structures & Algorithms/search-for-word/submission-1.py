class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(wordIdx, path, row, col):
            if board[row][col] != word[wordIdx]:
                return False
            else:    
                newpath = path.copy()
                newpath.add((row, col))
                if wordIdx == len(word) - 1:
                    return True
            if (row-1) >= 0 and (row-1, col) not in path:
                if backtrack(wordIdx + 1, newpath, row-1, col):
                    return True
            if (row+1) < len(board) and (row+1, col) not in path:
                if backtrack(wordIdx + 1, newpath, row+1, col):
                    return True
            if (col-1) >= 0 and (row, col-1) not in path:
                if backtrack(wordIdx + 1, newpath, row, col-1):
                    return True
            if (col+1) < len(board[0]) and (row, col+1) not in path:
                if backtrack(wordIdx + 1, newpath, row, col+1):
                    return True

            return False
        

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    if backtrack(0, set(), r, c):
                        return True
        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False