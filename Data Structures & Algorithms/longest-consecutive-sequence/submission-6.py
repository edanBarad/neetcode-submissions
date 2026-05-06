import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        heapq.heapify(nums)
        last = heapq.heappop(nums)
        seq, max_seq = 1, 1
        while nums:
            cur = heapq.heappop(nums)
            if cur - last == 1:
                seq += 1
            else:
                if seq > max_seq:
                    max_seq = seq
                seq = 1
            last = cur
        if seq > max_seq:
            max_seq = seq

        return max_seq