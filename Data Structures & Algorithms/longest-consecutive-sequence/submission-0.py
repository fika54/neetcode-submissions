class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:#
        heapq.heapify(nums)
        maxSeq = 0
        curSeq = 0
        lastNum = None

        for i in range(len(nums)):
            cur = heapq.heappop(nums)
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
        