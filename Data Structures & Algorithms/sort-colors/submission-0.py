class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, blue = 0, len(nums)-1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        while i <= blue:
            if nums[i] == 0:
                swap(red, i)
                red += 1
            elif nums[i] == 2:
                swap(i, blue)
                blue -= 1
                i -= 1
            i += 1
            