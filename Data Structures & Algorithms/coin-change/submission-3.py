class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        DP = [0] * (amount+1)
        for i in range(1, len(DP)):
            if i in coins:
                DP[i] = 1
            else:
                min_ans = 2**31 - 1
                for coin in coins:
                    if i-coin >= 0:
                        if DP[i-coin] == -1:
                            continue
                        else:
                            min_ans = min(min_ans, 1 + DP[i-coin])
                DP[i] = min_ans if -1 < min_ans < (2**31 - 1) else -1

        return DP[amount]