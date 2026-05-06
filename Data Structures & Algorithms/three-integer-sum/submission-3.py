class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            target = -num
            low, high = i+1, len(nums)-1
            while(low<high):
                if i == high:
                    high -= 1
                cur_sum = nums[low] + nums[high]
                if cur_sum == target:
                    res.append([num, nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif cur_sum < target:
                    low += 1
                else:
                    high -= 1
        return res