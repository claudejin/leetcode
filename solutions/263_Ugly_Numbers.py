class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        
        # factor of 2
        ugly_factors = [2, 3, 5]
        
        for f in ugly_factors:
            while num % f == 0:
                num /= f
        
        return (num == 1)