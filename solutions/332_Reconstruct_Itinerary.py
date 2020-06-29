class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.g = {}
        self.path = []
        
        # Initialize graph
        for fromto in tickets:
            if fromto[0] in self.g:
                self.g[fromto[0]].append(fromto[1])
            else:
                self.g[fromto[0]] = [fromto[1]]
        
        # Sort alphabetical order
        for key in self.g:
            self.g[key].sort()
        
        # Start from JFK
        self.dfs("JFK")
        return self.path
        
    def dfs(self, node: str):
        while node in self.g and len(self.g[node]) > 0:
            self.dfs(self.g[node].pop(0))
        self.path = [node] + self.path