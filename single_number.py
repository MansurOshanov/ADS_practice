class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         pairs = dict()
#         for i,v in enumerate(nums):
#             if v in pairs:
#                 pairs[v] += 1
#             else:
#                 pairs[v] = 1
        
#         for key in pairs:
#             if pairs[key] == 1:
#                 return key

        a = 0
        for i,v in enumerate(nums):
            a ^= v
        return a
        
            
            
        