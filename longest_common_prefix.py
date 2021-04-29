class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        common_prefix = ''
        while(True):
            cur_char = ''
            for word in strs:
                if i > len(word) - 1:
                    return common_prefix
                cur_char = word[i] if cur_char == '' else cur_char
                if word[i] != cur_char:
                    return common_prefix
            i += 1
            common_prefix += cur_char

            #space complexity = O(S) where S is sum of all characters in list
            
            
        