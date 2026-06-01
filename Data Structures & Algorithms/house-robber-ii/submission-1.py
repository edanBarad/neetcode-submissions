class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        def houseRobber1(houses):
            DP = [0]*len(houses)
            DP[0] = houses[0]
            for i in range(1, len(houses)):
                if i > 1:
                    DP[i] = max(houses[i] + DP[i-2], DP[i-1])
                else:
                    DP[i] = max(houses[i], DP[i-1])
            return DP[-1]

        #We take away the first/last house and do the same thing
        return max(houseRobber1(nums[1:]), houseRobber1(nums[:-1]))