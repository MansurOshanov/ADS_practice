class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        output = []
        cur_word = []
        
        def dfs(cur_word, i):
            if i == len(s):
                output.append("".join(cur_word))
                return
            
            if s[i].isalpha():
                cur_word.append(s[i].lower())
                dfs(cur_word, i+1)
                cur_word.pop()
                cur_word.append(s[i].upper())
                dfs(cur_word, i+1)
                cur_word.pop()
            else:
                cur_word.append(s[i])
                dfs(cur_word, i+1)
                cur_word.pop()
            
        dfs(cur_word, 0)
        return output
                
            
            
        
        
        
        
        