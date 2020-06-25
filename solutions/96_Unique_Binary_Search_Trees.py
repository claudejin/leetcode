class Solution:
    def __init__(self):
        self.dp = dict()
        self.dp[0] = 1
        self.dp[1] = 1
        self.m = 1
    
    def numTrees(self, n: int) -> int:
        if n <= self.m:
            return self.dp[n]
        
        c = 0
        for root in range(n):
            c += (self.numTrees(root) * self.numTrees(n-root-1))
        self.dp[n] = c
        self.m = n
        
        return c