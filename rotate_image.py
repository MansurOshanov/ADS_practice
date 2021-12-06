class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        '''Not in place solution'''
#         rows = len(matrix)
#         cols = len(matrix[0])
        
#         m2 = [[0]*rows for i in range(cols)]
        
#         for col in range(cols):
#             i = 0
#             for row in range(rows-1, -1, -1):
#                 m2[col][i] = matrix[row][col]
#                 i += 1
        
#         for row in range(rows):
#             for col in range(cols):
#                 matrix[row][col] = m2[row][col]

        
        '''
        In-place solution:
        '''
        n = len(matrix)
        
        for i in range(n//2 + n%2):
            for j in range(n//2):
                temp = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                matrix[i][j] = temp
                
        
        
        
    
        