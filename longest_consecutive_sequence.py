class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        hash_map = {num: 1 for num in nums}
        for num in hash_map.keys():
            if num+1 in hash_map:
                continue
            prev = num - 1
            while prev in hash_map:
                hash_map[num] += 1
                prev = prev - 1
        
        return max(hash_map.values())       