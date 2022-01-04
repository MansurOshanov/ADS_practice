class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        def rec(y, x):
            if y==1 or x==1:
                return 1
            if (y, x) in memo:
                return memo[(y, x)]
            
            memo[(y, x)] = rec(y-1, x) + rec(y, x-1)
            return memo[(y, x)]
        
        return rec(m, n)
