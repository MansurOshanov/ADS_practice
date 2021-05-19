class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Idea is to run house robber separately on two subarrays, which 
        either include first house or last house, and compare their
        results.
        '''

        def helper(arr):
            rob1 = rob2 = temp = 0
            for num in arr:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return temp
    
        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))