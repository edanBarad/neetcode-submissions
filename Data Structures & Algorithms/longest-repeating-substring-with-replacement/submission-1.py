class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        start, max_length = 0, 0
        for i, c in enumerate(s):
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
            
            cur_length = (i-start) + 1
            if (cur_length - max(freq.values())) > k:
                freq[s[start]] -= 1
                start += 1
                
            else:
                max_length = max(max_length, cur_length)

        return max_length