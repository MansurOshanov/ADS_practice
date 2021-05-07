class NumArray:
# #O(n) per query, O(1) space
#     def __init__(self, nums: List[int]):
#         self.nums = nums
        

#     def sumRange(self, left: int, right: int) -> int:
#         sum_range = 0
#         for i in range(left, right+1):
#             sum_range += self.nums[i]
#         return sum_range
    
    
    
    def __init__(self, nums: List[int]):
        self.sums = [0] * (len(nums) + 1)
        for i,v in enumerate(nums):
            self.sums[i+1] = self.sums[i] + nums[i]
            
        

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]
    
    
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)