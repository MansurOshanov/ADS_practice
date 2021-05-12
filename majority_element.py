class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        O(n) time and O(n) space solution
        '''
        # counter = collections.Counter(nums)
        # return max(counter, key = counter.get)
        
        '''
        O(n) time and O(1) space solution
        '''
        cand = nums[0]
        check_sum = 0
        for i,v in enumerate(nums):
            if v == cand:
                check_sum += 1
            else:
                check_sum -= 1
            if check_sum == 0:
                cand = nums[i + 1]
            
        return cand
                