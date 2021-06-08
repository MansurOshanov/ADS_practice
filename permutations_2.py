class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        Idea is to create HashMap that stores number of occurences
        of each element. So, we cannot take one element more than 
        once in our backtracking path
        '''
        

        counter = collections.Counter(nums)
        result = []
        perm = []
        def dfs():
            
            if len(perm) == len(nums):
                result.append(perm[:])
                return 
            
            for k,v in counter.items():
                if v > 0:
                    perm.append(k)
                    counter[k] -= 1
                    dfs()
                    perm.pop()
                    counter[k] += 1
            return 
        
        dfs()
        return result
                
                    
                    
                
                
        
        