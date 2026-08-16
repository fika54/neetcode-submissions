class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}

        l = 0
        cur = 0
        res = 0

        for i, char in enumerate(s):
            if char in unique and unique[char] >= l:
                l = unique[char]
                cur = i - l
            else:
                cur += 1
            unique[char] = i
            res = max(res, cur)
 
        return res