class Solution:
    def __init__(self):
        self.uglys = [1]
        self.next_idx = [0, 0, 0]
        
    def nthUglyNumber(self, n: int) -> int:
        while len(self.uglys) < n:
            candidates = [self.uglys[self.next_idx[0]]*2,
                          self.uglys[self.next_idx[1]]*3,
                          self.uglys[self.next_idx[2]]*5]
            
            next = min(candidates)
            self.uglys.append(next)
                        
            if next == candidates[0]: self.next_idx[0] += 1
            if next == candidates[1]: self.next_idx[1] += 1
            if next == candidates[2]: self.next_idx[2] += 1
        
        return self.uglys[n-1]