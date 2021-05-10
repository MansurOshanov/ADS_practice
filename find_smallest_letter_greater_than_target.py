class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        '''Seem like ordering in Python is ABC...Zab...xyz
        print("A"<"a") #True
        print("Z"<"a") #True
        print("a"<"b") #True
        '''
        
        '''
        Since characters are sorted, we can use Binary Search to find required char.
        We also need to keep track of the smallest element in right subarray, which 
        could be a result.
        '''
        
        left, right = 0, len(letters) - 1
        result = letters[0]
        while left <= right:
            pivot = (left+right) // 2
            
            if target < letters[pivot]:
                right = pivot - 1
                result = letters[pivot]
            else:
                left = pivot + 1
        return result
                
        
        
        