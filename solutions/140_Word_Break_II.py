class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        freq = dict()

        def tokenizer(s: str):
            if s in freq: return freq[s]

            res = []
            for word in wordDict:
                if s[:len(word)] != word:
                    continue

                if len(s) == len(word):
                    res.append(word)
                else:
                    for ss in tokenizer(s[len(word):]):
                        res.append(' '.join([word, ss]).rstrip())

            freq[s] = res
            return res

        return tokenizer(s)

