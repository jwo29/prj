class Solution:
    def countBits(self, n: int) -> List[int]:

        if n < 2:
            return list(range(n + 1))

        ans = [0] * (n + 1)
        ans[1] = 1

        for i in range(2, n + 1):
            # 값이 1/2배가 되면 이진수로는 비트가 오른쪽으로 한 칸 이동하는 성질을 이용
            ans[i] = ans[i // 2] + i % 2

        return ans
