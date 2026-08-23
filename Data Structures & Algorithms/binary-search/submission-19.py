class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        size = r - l + 1

        while size > 1:
            middle = l + (size // 2)

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1
            
            
            
            size = r - l + 1
        if size == 1 and nums[l] == target:
            return l
        
        return -1