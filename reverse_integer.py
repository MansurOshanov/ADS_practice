class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = x if x >= 0 else -x
        string_repr = str(x)
        reversed_repr = string_repr[::-1]
        result = int(reversed_repr) * sign
        if result >= -2**31 and result <= 2**31 - 1:
            return int(result)
        return 0