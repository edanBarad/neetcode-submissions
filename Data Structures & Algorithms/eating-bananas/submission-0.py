import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        l, r = 1, maxPile
        ans = maxPile
        while l <= r:
            k = (l+r)//2
            print("k=", k)
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)

            if hours <= h:
                ans = min(ans, k)
                r = k - 1
            else:
                l = k + 1

        return ans