class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set = dict()

        for i in range(len(nums)):

            if nums[i] in set:
                return True
            
            set[nums[i]] = "done"
        
        return False