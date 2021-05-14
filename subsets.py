class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        [] ---> [[]]
        [1] --> [[], [1]]
        [1,2] ->[[],[1], [2], [1,2]]
        
        '''
        
        power_set = [[]]
        
        for num in nums:
            size = len(power_set)
            for i in range(size):
                new_arr = power_set[i][:]
                new_arr.append(num)
                power_set.append(new_arr)
                #print(power_set)
        return power_set
                
        