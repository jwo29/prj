# 숫자 할리갈리 게임
from sys import stdin
from collections import deque

def halli_galli(M):
    ground = [[], []]

    turn = 0
    while M:
        card = deque[turn].popleft()
        ground[turn].append(card)

        if not deque[turn]:
            return turn ^ 1 # 상대방의 승리

        if ground[0] and ground[1] and ground[0][-1] + ground[1][-1] == 5: # 수연이 종을 침
            deque[1].extend(ground[0]+ground[1]) # 수연의 덱에 도도, 수연 카드 추가
            ground = [[], []] # 그라운드 초기화

        if card == 5: # 도도 or 수연이 방금 내린 카드가 5이고,
            if ground[1]: # 수연의 그라운드가 비어 있지 않으면
                deque[0].extend(ground[1]) # 도도의 덱에 수연 카드 추가
            if ground[0]: # 도도의 그라운드가 비어 있지 않으면
                deque[0].extend(ground[0]) # 도도의 덱에 도도 카드 추가
            ground = [[], []] # 그라운드 초기화

        M -= 1 # 게임 횟수 차감
        turn ^= 1 # 턴 바꾸기

    # M번의 실행이 끝난 후
    if len(deque[0]) > len(deque[1]): return 0 # 도도 승
    elif len(deque[0]) < len(deque[1]): return 1 # 수연 승
    else: return -1 # 비김

n, m = map(int, input().split())
deque = [deque(), deque()]

for _ in range(n):
    do, su = map(int, stdin.readline().split())
    deque[0].appendleft(do)
    deque[1].appendleft(su)

result = halli_galli(m)

if result == 0: # 도도 승
    print('do')
elif result == 1: # 수연 승
    print('su')
else: # 비김
    print('dosu')
