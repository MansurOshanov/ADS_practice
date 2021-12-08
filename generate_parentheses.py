class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []
        
        def dfs(cur_str, opened, closed):
            if len(cur_str) == 2*n:
                output.append("".join(cur_str))
                return
            
            if opened<n:
                cur_str.append("(")
                dfs(cur_str, opened+1, closed)
                cur_str.pop()
            if closed<opened:
                cur_str.append(")")
                dfs(cur_str, opened, closed+1)
                cur_str.pop()
            
            return            
         
        dfs([], 0, 0)
        return output
                