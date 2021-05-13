class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Naive solution is to take iterate through array, and take product of other elements
        It would take O(n^2) time and O(N) space
        '''
        # result = []
        # for i,v in enumerate(nums):
        #     product = 1
        #     for i2,v2 in enumerate(nums):
        #         if i != i2:
        #             product *= v2
        #     result.append(product)
        # return result
        '''
        Second idea is to multiply all numbers, and divide by corresponding value in array
        It would take O(n) time and O(n) space for output array.
        But zero elements ruin this solution.
        '''
        #bad idea
        
        '''
        Another idea is to find product of elements to the left and to the right 
        of each element in array.
        '''
#         left_products = [1]
#         right_products = [1] * len(nums)
        
#         for i in range(1, len(nums)):
#             left_products.append(left_products[i-1] * nums[i-1])
            
#         for i in range(len(nums) - 2, -1, -1):
#             right_products[i] = right_products[i+1] * nums[i+1]
        
#         output = []
#         print(left_products)
#         print(right_products)
#         for i in range(len(nums)):
#             output.append(left_products[i] * right_products[i])
#         return output

        '''
        In place solution using variables
        '''
    
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = nums[i-1] * output[i-1]
            
        R = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = R * output[i]
            R = R * nums[i]
        return output
    
    
        