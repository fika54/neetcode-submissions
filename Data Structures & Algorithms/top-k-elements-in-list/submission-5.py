class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for num in nums:
            hmap[num] = hmap[num] + 1

        heapList = [(v, k) for k,v in hmap.items()]

        sortedList = sorted(heapList, reverse=True)

        return [v[1] for v in sortedList[0:k]]

        # heapq.heapify(heapList)


        # i = 0
        # res = []
        # for i in range(k):
        #     if len(heapList) > 0:
        #         value, key = heapq.heappop(heapList)
        #         res.append(key)
        #         i = i + 1
        #     else:
        #         break
        # return res
        
        