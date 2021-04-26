import math
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_str = s[0]
        i = 0
        while (i<n):
            shift = 0
            max_len = 1
            l = math.floor(i-shift)
            r = math.ceil(i+shift)
            while(l >=0 and r < n and s[l] == s[r]):
                current_str = s[l:r+1]
                if len(current_str) > len(longest_str):
                    longest_str = current_str
                
                shift+=1
                l = math.floor(i-shift)
                r = math.ceil(i+shift)
            i+=0.5
        
        return longest_str
                    
                    
                    
                    
                