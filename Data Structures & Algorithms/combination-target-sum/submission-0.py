from collections import Counter
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        ans = []
        
        def helper(target_left, start_index, backpack):
            if target_left == 0:
                ans.append(backpack.copy())
                return

            elif target_left < 0:
                return

            for i in range(start_index, len(nums)):
                current_num = nums[i]
                
                if current_num > target_left:   #List is sorted, no need to check further on
                    break 
                
                backpack.append(current_num)
                helper(target_left-current_num, i, backpack)
                backpack.pop() #Ignore current choice and continue to the next numer in the list

        
        helper(target, 0, [])
        return ans