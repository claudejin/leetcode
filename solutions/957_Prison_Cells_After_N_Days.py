class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        loop = []
        
        for x in range(N):
            b = cells[0]
            
            for i in range(1, 7):
                b, cells[i] = cells[i], (1 if b == cells[i+1] else 0)
                    
            cells[0], cells[7] = 0, 0
            
            if cells[:] not in loop:
                loop.append(cells[:])
            else:
                ls = loop.index(cells[:])
                ind = (N-x) % (len(loop)-ls)
                return loop[ls+ind-1]
        
        return cells