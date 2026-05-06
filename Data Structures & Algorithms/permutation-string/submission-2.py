from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = Counter(s1)
        left = 0
        freq2 = Counter(s2[left:len(s1)])
        if freq1 == freq2:
            return True
        for c in s2[len(s1):]:
            freq2[s2[left]] -= 1
            if freq2[s2[left]] == 0:
                del freq2[s2[left]]
            left += 1
            freq2[c] = freq2.get(c, 0) + 1
            if freq1 == freq2:
                return True

        return False