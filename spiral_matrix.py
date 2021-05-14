class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L = 0 
        R = len(matrix[0]) - 1
        U = 0
        D = len(matrix) - 1
        output = []
        dir = 0
        
        while(D>=U and R>=L):
            if dir == 0:
                for i in range(L, R+1):
                    output.append(matrix[U][i])
                U += 1
            if dir == 1:
                for i in range(U, D+1):
                    output.append(matrix[i][R])
                R -= 1
            if dir == 2:
                for i in range(R, L-1, -1):
                    output.append(matrix[D][i])
                D -= 1
            if dir == 3:
                for i in range(D, U-1, -1):
                    output.append(matrix[i][L])
                L += 1
            dir += 1
            dir = dir % 4
        
        return output
            
                    
                
        
        