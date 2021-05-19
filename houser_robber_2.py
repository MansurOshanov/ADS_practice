class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Idea is to run house robber separately on two subarrays, which 
        either include first house or last house, and compare their
        results.
        '''

        def helper(arr, memo = {}):
            print(arr)
            print(memo)
            if len(arr) == 0:
                return 0
            if len(arr) == 1:
                return arr[0]
            if len(arr) == 2:
                return max(arr)
            if len(arr) in memo:
                return memo[len(arr)]
            memo[len(arr)] = max(helper(arr[:-2], memo) + arr[-1], helper(arr[:-1], memo))
            return memo[len(arr)]
        
        a1 = helper(nums[:-1], {})
        a2 = helper(nums[1:], {})
        return max(nums[0], a1, a2)