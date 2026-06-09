from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [key for key in counter.keys() if counter[key] > len(nums)//3]