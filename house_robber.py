class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Let's divide it into subproblems:
        If we had one house, rob it.
        if we had two house, rob which is more valuable
        if we had three house, add the result of robbery of not adjacent house
        '''
#         memo = {}
#         def dp_rob(nums):
#             #print(nums)
#             if len(nums) == 0:
#                 return 0
#             if len(nums) == 1:
#                 return nums[0]
#             if len(nums) == 2:
#                 return max(nums)
#             if len(nums) in memo:
#                 return memo[len(nums)]
#             else:
#                 memo[len(nums)] = max(dp_rob(nums[:-2]) + nums[-1], dp_rob(nums[:-1]))

#             return memo[len(nums)]
#         return dp_rob(nums)
    
        '''
        Iterative DP approach:
        '''
        rob1 = 0
        rob2 = 0
        
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return temp
        
        