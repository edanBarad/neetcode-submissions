class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        max_length = 1

        for i in range(len(s)):
            l, r = i, i     #Odd length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if max_length < (r-l)+1:
                    max_length = (r-l)+1
                    longest = s[l:r+1]
                l -= 1
                r += 1

            l, r = i, i+1   #Even length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if max_length < (r-l)+1:
                    max_length = (r-l)+1
                    longest = s[l:r+1]
                l -= 1
                r += 1
                

        return longest