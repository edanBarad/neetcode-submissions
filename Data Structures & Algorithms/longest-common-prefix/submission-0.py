class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        elif len(strs)==2:
            lcp = []
            i, m = 0, min(len(strs[0]), len(strs[1]))
            while i < m and strs[0][i] == strs[1][i]:
                lcp.append(strs[0][i])
                i += 1
            return "".join(lcp)
        else:
            n = len(strs)
            left = self.longestCommonPrefix(strs[:n//2])
            right = self.longestCommonPrefix(strs[n//2:])
            return self.longestCommonPrefix([left, right])