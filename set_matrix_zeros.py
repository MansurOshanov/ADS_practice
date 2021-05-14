class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        '''
        Create two arrays, that keeps count, which rows and columns to zero
        O(m*n) time, O(m+n) space(2 arrays)
        '''

        
#         ROWS = len(matrix)
#         COLS = len(matrix[0])
        
#         vertical = [False] * ROWS
#         horizontal = [False] * COLS
        
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if matrix[r][c] == 0:
#                     vertical[r] = True
#                     horizontal[c] = True
        
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if vertical[r] or horizontal[c]:
#                     matrix[r][c] = 0

        '''
        Instead of creating 2 arrays, we can use first column and first row
        '''
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        vertical_first = False
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r == 0:
                        vertical_first = True
                        matrix[0][c] = 0
                    else:
                        matrix[r][0] = 0
                        matrix[0][c] = 0
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        for r in range(ROWS):
            if matrix[0][0] == 0:
                matrix[r][0] = 0
        
        for c in range(COLS):
            if vertical_first:
                matrix[0][c] = 0
                
                
                    
                    
                    
        