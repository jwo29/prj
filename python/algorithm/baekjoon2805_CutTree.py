# 나무 자르기
from sys import stdin
n, m = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

min_h, max_h = 0, max(trees)
#
# if min_h < max_h:
#     while True:
#         mid = (min_h + max_h) // 2
#         length = 0
#
#         for t in trees:
#             if t > mid:
#                 length += t-mid
#
#         if length < m: # 나무를 더 잘라야 함 -> 높이 더 낮게
#             max_h = mid
#         elif length > m: # 나무를 덜 잘라야 함 -> 높이 더 높게
#             min_h = mid
#         else:
#             print(mid)
#             break
# else:
#     print(m//n+1) if m%n else print(m//n)


mid = 0
while min_h < max_h:
    mid = (min_h + max_h) // 2
    length = 0

    for t in trees:
        if t > mid:
            length += t-mid

    if length < m: # 나무를 더 잘라야 함 -> 높이 더 낮게
        max_h = mid-1
    elif length > m: # 나무를 덜 잘라야 함 -> 높이 더 높게
        min_h = mid+1
    else:
        break

print(mid)