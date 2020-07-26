class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if nums[0] < nums[-1]: return nums[0]

        m = int(len(nums) / 2)
        return min(self.findMin(nums[0:m]), self.findMin(nums[m:]))

