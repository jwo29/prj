class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [[], []]
        dp[0] = [True] * (n + 1)  # Bob Score
        dp[1] = [False] * (n + 1)  # Alice Score

        for k in range(2, n + 1):
            for x in range(k - 1, 0, -1):
                if k % x == 0:
                    # 초기 n이 k-x일 때 Alice의 결과가 False
                    # -> 이번에는 그 결과가 Bob의 결과가 됨
                    # -> Bob과 반대로 Alice는 True가 됨
                    dp[1][k] = dp[1][k] or not dp[1][k - x]

                    if dp[1][k]:
                        dp[0][k] = False
                        break

        return dp[1][n]  # 초기 n에 대한 Alice의 승패 여부