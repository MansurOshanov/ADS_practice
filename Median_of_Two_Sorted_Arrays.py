class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #naive approach n(logn) time.
        #Runtime: 84 ms, faster than 92.61% of Python3 online 
        #submissions for Median of Two Sorted Arrays. Memory Usage: 14.6 MB, less than    
        #21.89% of Python3 online submissions for Median of Two Sorted Arrays.
        ''' 
        nums1.extend(nums2)
        nums1.sort()
        
        m = (len(nums1) - 1) // 2 
        if len(nums1) % 2 == 0:
            result = (nums1[m] + nums1[m + 1]) / 2
            return result
        else:
            return nums1[m]
            
        '''
        
        #logn solution(binary search approach)
        A, B = nums1, nums2
        
        if len(A) > len(B):
            A, B = B, A
            
        total = len(A) + len(B)
        half = total // 2
        
        l = 0
        r = len(A) - 1
        
        while True:
            i = (l+r) // 2 # estimated median index of A
            j = half - i - 2 # estimated median index of B. Since arrays starts from zero,                              we need to substract 2, to find a correct median index of B.
            #print("i:", i, "j", j, "r", r)
            #Let's initilize edges(max left and min right side) of each array
            A_left = A[i] if i >= 0 else float(-inf)
            A_right = A[i+1] if i+1 < len(A) else float(inf)
            B_left = B[j] if j >= 0 else float(-inf)
            B_right = B[j+1] if j+1 < len(B) else float(inf)
            
            #correct case
            if A_left <= B_right and B_left <= A_right:
                #odd case
                if total % 2:
                    return min(A_right, B_right)
                #even case
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1
                
                
        