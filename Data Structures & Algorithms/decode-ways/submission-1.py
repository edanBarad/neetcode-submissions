class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        DP = [0]*len(s)
        DP[0] = 1
        for i in range(1, len(DP)):
            #1 digit
            if int(s[i]) in range(1, 10):
                DP[i] += DP[i-1]

            #2 digit case
            if int(s[i]) == 0:
                if int(s[i-1]) in (1, 2):
                    DP[i] += (DP[i-2] if i>1 else 1)
                else:
                    return 0
            elif int(s[i]) in (7, 8, 9):
                if int(s[i-1]) == 1:
                    DP[i] += (DP[i-2] if i>1 else 1)
            elif int(s[i]) in range(1, 7):
                if int(s[i-1]) in (1, 2):
                    DP[i] += (DP[i-2] if i>1 else 1)

        return DP[-1]