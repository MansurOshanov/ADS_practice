class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        cur_str = []
        
        #Sort nums so that content of tupes will have the correct order.
        nums.sort()
        
        def dfs(i):
            if i == len(nums):
                output.append(tuple(cur_str))
                return
            
            cur_str.append(nums[i])
            dfs(i+1)
            cur_str.pop()
            dfs(i+1)
            
        dfs(0)
        
        return set(output)
            
        
            
        
        p