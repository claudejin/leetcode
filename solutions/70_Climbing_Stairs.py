class Solution:
    def climbStairs(self, n: int) -> int:
        def combination(n, r):
            res = 1
            for x in range(r):
                res = res * (n-x) / (x+1)
            return int(res)

        two_max = int(n / 2)
        res = 0
        for x in range(two_max + 1):
            print(n-x, x, combination(n-x, x))
            res += combination(n-x, x)

        return res

