class Solution:
    def rob(self, nums: List[int]) -> int:
        DP = [0]*len(nums)
        DP[0] = nums[0]
        for i in range(len(nums)):
            if i >= 2:
                DP[i] = max(nums[i]+DP[i-2], DP[i-1])
            else:
                DP[i] = max(nums[i], DP[i-1])

        return DP[-1]