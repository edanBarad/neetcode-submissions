class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count, slow = 0, 0
        for i in range(len(nums)):
            if nums[i] != val:
                count += 1
                nums[slow] = nums[i]
                slow += 1
        return count