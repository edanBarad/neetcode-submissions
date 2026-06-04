class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {}

        def helper(curr_s):
            if curr_s in mem: return mem[curr_s]
            elif not curr_s: return True

            for word in wordDict:
                if curr_s.startswith(word):
                    if helper(curr_s[len(word):]):
                        mem[curr_s] = True
                        return True

            mem[curr_s] = False
            return False
        
        return helper(s)