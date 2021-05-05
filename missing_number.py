class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = int((n+1) * (n/2)) 
        for i,v in enumerate(nums):
            total -= v
        return total
        