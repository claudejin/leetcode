class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Initialize
        h, w = len(dungeon), len(dungeon[0])
        
        dcost = [[0]*w for _ in range(h)]
        dcost[h-1][w-1] = 1
        
        # Calculation (Dynamic Programming)
        for y in reversed(range(h)):
            for x in reversed(range(w)):
                dcost[y][x] += -dungeon[y][x]
                
                precost = []
                if y + 1 < h: # From bottom
                    precost.append(dcost[y+1][x])
                if x + 1 < w: # From right
                    precost.append(dcost[y][x+1])
                
                if len(precost) > 0:
                    dcost[y][x] += min(precost)
                    
                dcost[y][x] = max(1, dcost[y][x])
        
        return (dcost[0][0])