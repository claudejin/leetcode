class Solution:
    def reverseWords(self, s: str) -> str:
        word = []
        res = []
        
        for i in reversed(range(len(s))):
            if s[i] != ' ':
                word = [s[i]] + word
            
            if len(word) > 0 and (s[i] == ' ' or i == 0):
                res.append(''.join(word))
                word = []
        
        return ' '.join(res)