class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[-1] = 1
        maxLIS = 1
        for i in range(len(nums)-2, -1, -1):
            LIS, j = 1, i+1
            while j < len(nums):
                if nums[j] > nums[i]:
                    LIS = max(LIS, 1 + dp[j])
                j += 1
            dp[i] = LIS
            maxLIS = max(maxLIS, LIS)
        
        return maxLIS