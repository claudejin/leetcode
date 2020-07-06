class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        while x > 0 or y > 0:
            xr, yr = (x % 2), (y % 2)
            x, y = int(x / 2), int(y / 2)
            
            if xr != yr:
                cnt += 1
        
        return cnt