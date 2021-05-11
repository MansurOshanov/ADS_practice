class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        We can find index when numbers become positive in initial array, 
        and assign two pointers in each direction
        '''
        pivot = len(nums)
        for i,v in enumerate(nums):
            if v >= 0:
                pivot = i
                break
        
        result = []
        l,r = pivot-1, pivot
        while (l>=0 and r<len(nums)):
            if abs(nums[l])<nums[r]:
                result.append(nums[l]**2)
                l -= 1
            else:
                result.append(nums[r]**2)
                r += 1
        
        if l>=0:
            result.extend([nums[i]**2 for i in range(l, -1, -1)])
        else:
            result.extend([nums[i]**2 for i in range(r, len(nums))])
        
        return result
        