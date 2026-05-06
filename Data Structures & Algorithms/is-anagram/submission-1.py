from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd, td = defaultdict(int), defaultdict(int)
        for char in s:
            sd[char] += 1
        for char in t:
            td[char] += 1
        return sd == td