class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = sorted([x for x in nums if x < 0])
        Z = sorted([x for x in nums if x == 0])
        P = sorted([x for x in nums if x > 0])
        sol = set()
                
        # All zeros
        if len(Z) > 2:
            sol.add((0, 0, 0))
        
        Ns = set(N)
        Ps = set(P)
        
        # N-Z-P
        if len(Z) > 0:
            for n in Ns:
                if (-n) in Ps:
                    sol.add((n, 0, -n))
        
        # N-N-P
        for n1 in range(len(N)-1):
            for n2 in range(n1+1, len(N)):
                t = -N[n1] - N[n2]
                if t in Ps:
                    sol.add(tuple(sorted([N[n1], N[n2], t])))
        
        # N-P-P
        for p1 in range(len(P)-1):
            for p2 in range(p1+1, len(P)):
                t = -P[p1] - P[p2]
                if t in Ns:
                    sol.add(tuple(sorted([t, P[p1], P[p2]])))
        
        return sorted(list(sol))