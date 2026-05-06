class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        start, max_len = 0, 0
        for i in range(len(s)):
            if s[i] not in letters:
                letters[s[i]] = 1
                if (i-start+1) > max_len:
                    max_len = (i-start+1)
            else:
                letters[s[i]] += 1
                while True:
                    if letters[s[start]] > 1:
                        letters[s[start]] = 1
                        start += 1
                        break
                    else:
                        letters.pop(s[start])
                        start += 1
        return max_len