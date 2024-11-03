# a. 生成 10x10 的整數 2 維陣列 map，其每個元素初始為 0
map=[[0 for _ in range(10)] for _ in range(10)]

# b. 生成 10x10 的整數 1 維陣列 rowMap 並將其主要用來儲存炸彈位置 (以 0 或 1 作為儲存)。
rowMap:list[int]=[0]*100 #0為變數 設定陣列每格為0

# c. 設定 rowMap 給定的索引 [0, 7, 13, 28, 44, 62, 74, 75, 87, 90]

for a in range(0,10):
    bomb_indices=int(input())
    rowMap[bomb_indices]=1

#bomb_indices = [0, 7, 13, 28, 44, 62, 74, 75, 87, 90]

# 將炸彈放入 map_array 中
'''
for index in bomb_indices:
    row, col = divmod(index, 10)
    map_array[row][col] = 1
'''
# d. 設定周圍的數字
'''
def is_valid(x, y):
    return 0 <= x < 10 and 0 <= y < 10

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for index in bomb_indices:
    row, col = divmod(index, 10)
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if is_valid(r, c):
            map_array[r][c] += 1
'''

# d. 設定周圍的數字
'''
for index in bomb_indices:
    row, col = divmod(index, 10)
    for dr in [-1, 0, 1]:  # 行偏移量
        for dc in [-1, 0, 1]:  # 列偏移量
            # 跳过炸弹本身
            if dr == 0 and dc == 0:
                continue
            # 边界检查
            if 0 <= row + dr < 10 and 0 <= col + dc < 10:
                map[row + dr][col + dc] += 1
'''
for i in range(0,10):
     for j in range(0,10):
         if rowMap[i*10+j]==1:
             map[i][j]='*'
              

# e. 最後, 請將該二維陣列值輸出
for row in map:
    output_row = []
    for cell in row:
        # 如果大於 1，顯示為 1，否則顯示原數值
        output_row.append(1 if cell > 1 else cell)
    print(" ".join(map(str, output_row)))

output_map = [[1 if cell > 1 else cell for cell in row] for row in map]

for row in output_map:
    print(" ".join(map(str, row)))