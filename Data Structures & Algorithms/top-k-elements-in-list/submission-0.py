from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = [(-freq, num) for num, freq in counts.items()]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            _, num = heapq.heappop(heap)
            res.append(num)
        return res