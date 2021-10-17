# 크게 만들기
n, k = map(int, input().split())
num = input()

front = list(num)
new_num = ''

for i in range(n-k, 0, -1):

    mid, back = [], []

    for j in range(i):
        back.append(front.pop())

    while front:
        if front[-1] >= back[-1]:
            mid.append(back.pop())
            back.append(front.pop())
        else:
            front.pop()

    new_num += back.pop()
    front = list(reversed(back + mid))

print(new_num)