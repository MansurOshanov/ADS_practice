class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        #iteration: O(n^n) time
#         output = [""]
        
#         for char in s:
#             temp = []
#             if char.isalpha():
#                 for o in output:
#                     temp.append(o+char.lower())
#                     temp.append(o+char.upper())
#             else:
#                 for o in output:
#                     temp.append(o+char)
#             output = temp
        
#         return output

        '''
        DFS appoach: Backtracking
        '''
        output = []
        def dfs(cur_string, i):
            if len(cur_string) == len(s):
                output.append("".join(cur_string))
                return 
            
            if s[i].isalpha():
                cur_string.append(s[i].lower())
                dfs(cur_string, i+1)
                cur_string.pop()
                
                cur_string.append(s[i].upper())
                dfs(cur_string, i+1)
                cur_string.pop()
            
            else:
                cur_string.append(s[i])
                dfs(cur_string, i+1)
                cur_string.pop()
            return 
        
        cur_string = []
        dfs(cur_string, 0)
        return output
        
                
            
            
        
        
        
        
        