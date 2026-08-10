class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        i = 0
        l = 0
        r = 0

        res = []

        for i in range(len(sort)):
            if i > 0 and sort[i] == sort[i-1]:
                continue
            
            l = i + 1
            r = len(sort) - 1

            lastShift = ''

            while l < r:
                check = sort[i] + sort[l] + sort[r]

                if check > 0:
                    while r > 0 and sort[r-1] == sort[r]:
                        r -= 1
                    r -= 1
                elif check < 0:
                    while l < len(sort) and sort[l+1] == sort[l]:
                        l += 1
                    l += 1
                else:
                    res.append([sort[i], sort[l], sort[r]])
                    while r > 0 and sort[r-1] == sort[r]:
                        r -= 1
                    r -= 1

        
        
        return res






                

        
        