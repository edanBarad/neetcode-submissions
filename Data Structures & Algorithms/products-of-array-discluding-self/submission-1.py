class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        p = 1
        for i in range(len(nums)):
            left.append(p)
            p *= nums[i]
        p = 1
        right = []
        for i in range(len(nums)-1, -1, -1):
            right.append(p)
            p *= nums[i]
        right.reverse()
        return [left[i]*right[i] for i in range(len(nums))]