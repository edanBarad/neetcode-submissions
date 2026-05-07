class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i == j:
                    continue
                if num1 == num2 :
                    return num1