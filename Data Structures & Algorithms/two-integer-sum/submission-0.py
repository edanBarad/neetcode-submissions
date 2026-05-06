class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indecies = {}
        for i, num in enumerate(nums):
            left = (target - num)
            if (left in indecies and indecies[left] != i):
                return [indecies[left], i]
            else: indecies[num] = i