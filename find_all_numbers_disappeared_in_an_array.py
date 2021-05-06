class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i,v in enumerate(nums):
            nums[abs(v)-1] = abs(nums[abs(v)-1]) * -1
        result = []
        for i,v in enumerate(nums):
            if v > 0:
                result.append(i+1)
        return result