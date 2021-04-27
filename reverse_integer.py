class Solution:
    def reverse_using_python(self, x: int) -> int:
        
        sign = 1 if x >= 0 else -1
        x = x if x >= 0 else -x
        string_repr = str(x)
        reversed_repr = string_repr[::-1]
        result = int(reversed_repr) * sign
        if result >= -2**31 and result <= 2**31 - 1:
            return int(result)
        return 0
    
    def reverse(self, x: int) -> int:
        
        max_int = 2**31 - 1
        min_int = -(2**31)
        print(max_int)
        print(min_int)
        
        sign = 1 if x>=0 else -1
        x = x if x>=0 else -x
        
        result = 0
        while x>0:
            last_digit = x % 10
            x = x // 10
            result = result * 10 + last_digit
            print(result)
        result = result * sign
        if result >= min_int and result <= max_int:
            return int(result)
        return 0
        