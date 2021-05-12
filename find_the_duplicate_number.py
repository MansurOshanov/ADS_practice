class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        O(N) time and O(1) space
        '''
        for i,v in enumerate(nums):
            if nums[abs(v) - 1] < 0:
                return abs(v)
            else:
                nums[abs(v) - 1] = nums[abs(v) - 1] * -1
        
        
        '''
        O(NlogN) time, O(1) space
        '''
        # nums.sort()
        # for i,v in enumerate(nums):
        #     if v == nums[i+1]:
        #         return v
        