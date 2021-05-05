class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for i,v in enumerate(nums):
            if v in my_set:
                return True
            my_set.add(v)
        return False
                
        