class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        i = 0
        
        max_int = 2**31 - 1
        min_int = -(2**31)
        
        #check if string is empty:
        if not s:
            return 0
        
        #check for white spaces:
        while(i<len(s) and s[i] == ' '):
            i += 1
        
        #check if sign exists
        if (i<len(s) and (s[i] == '+' or s[i] == '-')):
            sign = -1 if s[i] == '-' else 1
            i += 1
            
        #check for digits
        while (i<len(s) and s[i] >= '0' and s[i] <= '9'):
            result = result*10 + int(s[i])
            i += 1
        
        result = sign * result
        result = result if result <= max_int else max_int
        result = result if result >= min_int else min_int
        
        return result