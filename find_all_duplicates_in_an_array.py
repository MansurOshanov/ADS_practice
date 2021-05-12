class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        O(n) time and O(n) space using HashMap
        '''
        # counter = collections.Counter(nums)
        # return [i for i in counter if counter[i] == 2]
    
        '''
        O(NlogN) time and O(1) space using in line sorting (assuming output space 
        does not count)
        '''
        
        # nums.sort()
        # output = []
        # for i in range(len(nums)):
        #     if i+1<len(nums) and nums[i] == nums[i+1]:
        #         output.append(nums[i])
        #         i += 1
        # return output
        
        '''
        inline checking using indices
        O(N) time and O(1) memory
        '''
        output = []
        for i,v in enumerate(nums):
            if nums[abs(v)-1] < 0:
                output.append(abs(v))
            else:
                nums[abs(v)-1] = nums[abs(v)-1] * -1
        return output    
            
                
                
    
        