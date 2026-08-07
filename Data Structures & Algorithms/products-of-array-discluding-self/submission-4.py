class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        suffix = []

        i = 0
        n = len(nums)

        while i < n:
            if i == 0:
                prefix.append(1)
                suffix.append(1)
            else:
                prefix.append(nums[i-1] * prefix[i-1])
                suffix.append(nums[n - i] * suffix[len(suffix)-1])
                
            i += 1
        

        res = []

        i = 0
        while i < n:
            res.append(prefix[i] * suffix[n-1-i])
            i += 1

        return res
        