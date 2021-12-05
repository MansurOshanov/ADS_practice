class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if m*n != len(original):
            return []
        
        output = [[1]*n for i in range(m)]
        
        i = 0 
        for row in range(m):
            for col in range(n):
                output[row][col] = original[i]
                i+=1
        
        return output