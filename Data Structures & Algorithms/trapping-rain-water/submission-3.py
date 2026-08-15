class Solution:
    def trap(self, height: List[int]) -> int:

        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        maxl = 0
        maxr = 0

        i = 0

        while i < len(height):
            j = len(height) - i - 1

            maxLeft[i] = maxl
            maxRight[j] = maxr

            if height[i] > maxl:
                maxl = height[i]
            
            if height[j] > maxr:
                maxr = height[j]
            
            i+= 1

        res = 0
        
        i = 0

        while i < len(height):
            res += max(min(maxLeft[i], maxRight[i]) - height[i], 0)
            i += 1
        
        return res


