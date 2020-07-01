class Trie:
    def __init__(self):
        self.endOfWord = False
        self.children = [None]*26
    
    def insert(self, word):
        curr = self
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None: curr.children[idx] = Trie()
            curr = curr.children[idx]
        
        curr.endOfWord = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        h, w = len(board), len(board[0])
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = set([])
        
        def backtrack(myboard: List[List[str]], word: str, trie, s: tuple):
            # Out of bound
            x, y = s
            if x < 0 or y < 0 or x == w or y == h:
                return False
            
            # Meet a letter used already
            if myboard[y][x] == '-': return False
            
            # No existance of letter
            t = trie.children[ord(myboard[y][x]) - ord('a')]
            if t is None: return False
            
            c = myboard[y][x]
            word += c
            
            # Found the word
            if t.endOfWord: res.add(word)
            
            # Backtracking
            myboard[y][x] = '-'
            backtrack(myboard, word, t, (x-1, y))
            backtrack(myboard, word, t, (x, y-1))
            backtrack(myboard, word, t, (x+1, y))
            backtrack(myboard, word, t, (x, y+1))
            myboard[y][x] = c
        
        for y in range(h):
            for x in range(w):
                backtrack(board, "", trie, (x, y))
        
        return list(res)