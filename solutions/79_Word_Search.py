class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h, w = len(board), len(board[0])
        
        def backtrack(board, x, y, word):
            if len(word) == 0: return True
            
            if x < 0 or y < 0 or x == w or y == h: return False
            if board[y][x] != word[0]: return False
            
            board[y][x], tmp = '-', board[y][x]
            if backtrack(board, x-1, y, word[1:]): return True
            if backtrack(board, x, y-1, word[1:]): return True
            if backtrack(board, x+1, y, word[1:]): return True
            if backtrack(board, x, y+1, word[1:]): return True            
            board[y][x] = tmp
            
            return False
        
        for y in range(h):
            for x in range(w):
                if backtrack(board, x, y, word):
                    return True
        
        return False