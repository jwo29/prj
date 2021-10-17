from collections import defaultdict as dd


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        positions = dd(list)
        freqs = dd(int)
        candidates = list()

        n = len(nums)
        max_freq = 0

        for i in range(n):
            num = nums[i]
            positions[num].append(i)
            freqs[num] += 1

            if freqs[num] > max_freq:
                candidates = [num]
                max_freq = freqs[num]
            elif freqs[num] == max_freq:
                candidates.append(num)

        short_len = n

        for c in candidates:
            f, l = positions[c][0], positions[c][-1]
            short_len = min(short_len, (l - f) + 1)

        return short_len