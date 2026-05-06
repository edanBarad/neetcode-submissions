from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        td = Counter(t)
        counts = {}
        sd = {}
        start = 0
        ans = ""

        for i, c in enumerate(s):
            if c in td:
                counts[c] = counts.get(c, 0) + 1
                
                if counts[c] >= td[c]:
                    sd[c] = True

            while len(sd) == len(td):
                current = s[start:i+1]
                if not ans or len(current) < len(ans):
                    ans = current
                
                char_at_start = s[start]
                if char_at_start in td:
                    counts[char_at_start] -= 1
                    if counts[char_at_start] < td[char_at_start]:
                        if char_at_start in sd:
                            del sd[char_at_start]
                
                start += 1
        
        return ans