class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        if s.find(" ") == -1: return len(s)
        end = len(s)-1
        while s[end] == ' ': end -= 1
        start  = end
        while s[start] != ' ' and start > 0: start -= 1
        return end-start