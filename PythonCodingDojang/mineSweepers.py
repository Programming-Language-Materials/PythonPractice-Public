matrix = []

col, row = map(int, input().split(' '))
for i in range(row):
    matrix.append(list(input()))

ans = []

for r in range(row):
    tmp = []
    for c in range(col):
        if matrix[r][c] == '*':
            tmp.append('*')
        else:
            num = 0
            for r_ in range(r - 1, r + 2):
                for c_ in range(c - 1, c + 2):
                    if r_ >= 0 and c_ >= 0 and r_ < row and c_ < col and matrix[r_][c_] == '*':
                        num += 1
            tmp.append(num)
    ans.append(tmp)

for r in range(row):
    for c in range(col):
        print(ans[r][c], end='')
    print()