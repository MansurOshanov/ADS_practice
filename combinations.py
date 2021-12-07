class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        output = []
        
        def dfs(cur_comb, start):
            if len(cur_comb) == k:
                output.append(cur_comb.copy())
                return
            
            for i in range(start, n+1):
                cur_comb.append(i)
                dfs(cur_comb, i+1)
                cur_comb.pop()
        
        dfs([], 1)
        return output