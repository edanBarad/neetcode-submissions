class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum, max_sum = 0, -1000
        for num in nums:
            if curr_sum < 0 and num >= 0 or curr_sum < 0 and curr_sum < num:
                curr_sum = num
            else:
                curr_sum += num
    
            max_sum = max(max_sum, curr_sum)

        return max_sum