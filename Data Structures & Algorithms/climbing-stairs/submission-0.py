class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def helper(n):
            #Base cases
            if n <= 0: return 0
            if n == 1: return 1
            if n == 2: return 2
            if n in mem: return mem[n]
            
            mem[n] = helper(n-1) + helper(n-2)
            return mem[n]

        return helper(n)