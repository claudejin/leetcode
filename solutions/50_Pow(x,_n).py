class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return pow(x, n) # Simple in python
        
        if n < 0:
            x = 1 / x
            
        res = 1
        while n != 0:
            if n % 2 != 0:
                res *= x
            n = int(n/2)
            x *= x
            
        return res