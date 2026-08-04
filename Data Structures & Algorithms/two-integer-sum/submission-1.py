class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for int1 in range(len(nums)):
            for int2 in range(len(nums)):
                if int1 != int2:
                    if nums[int1] + nums[int2] == target:
                        return [int1, int2]
        
        return []