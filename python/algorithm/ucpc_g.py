# 경품 추첨
k, n = map(int, input().split())

box = [[i for i in range(1, n+1)]]
diff = [i for i in range(1, n)]

for i in range(1, k):
    able = box[i-1][-1] + 1
    box.append([able])

    for j in range(len(box[i])):
        able += 1
        while able-box[i][j] in diff:
            able += 1
        diff.append(able-box[i][j])
        box[i].append(able)

