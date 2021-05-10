class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        '''My solution, probably has extra conditions, but works in O(logN) time'''
        left,right = 0, len(arr) - 1
        
        while(left<=right):
            pivot = (left+right) // 2
            
            left_neigh = arr[pivot-1] if pivot>0 else float('-inf')
            right_neigh = arr[pivot+1] if pivot < len(arr) - 1 else float('inf')
            
            if arr[pivot] >left_neigh and arr[pivot] > right_neigh:
                return pivot
            if arr[pivot] > left_neigh and arr[pivot] < right_neigh:
                left = pivot + 1
            else:
                right = pivot - 1

            
        