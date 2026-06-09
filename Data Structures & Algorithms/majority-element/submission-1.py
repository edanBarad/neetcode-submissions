class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr, count = nums[0], 1
        for num in nums[1:]:
            if num == curr: count += 1
            else:
                count -= 1
                if count == 0:
                    curr = num
                    count = 1
        return curr