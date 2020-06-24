class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniq = list(set(nums))
        scan = [0 for _ in range(len(uniq))]
        for v in nums:
            scan[uniq.index(v)] += 1
        
        res = [i for i, e in enumerate(scan) if e != 3]
        return (uniq[res[0]])