class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = False
        for aa, bb in itertools.zip_longest(reversed(a), reversed(b), fillvalue='0'):
            s = 0
            if aa == '1': s += 1
            if bb == '1': s += 1
            if carry: s += 1
            
            carry = s > 1            
            res = [str(s % 2)] + res
        
        if carry:
            res = ['1'] + res
        
        return (''.join(res))