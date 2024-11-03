map: list[list[chr]] = [['0'] * 10 for _ in range(10)]
rowMap: list[int] = [0] * 100
for a in range(0, 10):
    boom = int(input())
    rowMap[boom] = 1
for i in range(0, 10):
    for j in range(0, 10):
        if rowMap[i * 10 + j] == 1:
            map[i][j] = '*'
for i in range(0, 10):
    for j in range(0, 10):
        if map[i][j] != '*':
            n = 0
            for x in range(max(0, i - 1), min(10, i + 2)):
                for y in range(max(0, j - 1), min(10, j + 2)):
                    if map[x][y] == '*':
                        n += 1
            if n > 0:
                map[i][j] = chr(n + ord('0'))
            else:
                map[i][j] = ' '
for row in map:
    print(' '.join(row))