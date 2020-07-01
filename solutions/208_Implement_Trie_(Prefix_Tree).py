class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.endOfWord = False
        self.children = [None] * 26
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        for c in word:
            idx = ord(c) - ord('a')
            if self.children[idx] == None: self.children[idx] = Trie()
            self = self.children[idx]
        
        self.endOfWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self
        for idx in range(len(word)):
            t = t.children[ord(word[idx]) - ord('a')]
            if t is None: break
            if t.endOfWord and (idx+1) == len(word): return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self
        for c in prefix:
            t = t.children[ord(c) - ord('a')]
            if t is None: return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)