class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:#
        sortedList = sorted(nums)
        maxSeq = 0
        curSeq = 0
        lastNum = None

        for i in range(len(sortedList)):
            cur = sortedList[i]
            if cur == lastNum:
                continue
            if cur-1 == lastNum:
                curSeq += 1
            else:
                curSeq = 1
            if curSeq > maxSeq:
                maxSeq = curSeq
            
            lastNum = cur
            
            


        return maxSeq
        