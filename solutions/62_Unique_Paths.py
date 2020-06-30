class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_slot = (m-1) + (n-1)
        min_slot = min(m, n)-1
        
        num, deno = 1, 1
        for x in range(min_slot):
            num *= (total_slot - x)
            deno *= (min_slot - x)
        
        return int(num / deno)