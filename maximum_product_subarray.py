class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_pos = 1
        min_neg = 1
        result = max(nums)
        
        
        for num in nums:
            if num == 0:
                max_pos = 1
                min_neg = 1
                continue
            max_pos_temp = max_pos
            max_pos = max(max_pos * num, min_neg * num, num) 
            min_neg = min(max_pos_temp * num, min_neg * num, num)
            result = max_pos if max_pos > result else result
        return result
            
        