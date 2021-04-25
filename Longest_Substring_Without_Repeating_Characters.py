class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occured_characters = set()
        window = []
        max_len = 0
        for char in s:
            while char in occured_characters:
                occured_characters.remove(window[0])
                window.pop(0)
            window.append(char)
            occured_characters.add(char)
            max_len = len(window) if len(window) > max_len else max_len
        return max_len
                