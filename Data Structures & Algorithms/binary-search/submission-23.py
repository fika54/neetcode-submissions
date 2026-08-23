class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        size = r - l + 1

        if size == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        while size >= 1:
            middle = int(l + (r - l) / 2)

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1
            
            
            
            size = r - l + 1
        
        return -1