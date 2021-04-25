class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values_dict = dict()
        for index, value in enumerate(nums):
            needed_num = target - value
            if needed_num in values_dict:
                return [values_dict[needed_num], index]
            values_dict[value] = index
    