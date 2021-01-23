arr = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]


def hourglassSum(arr):
    hourglass = [
        [1, 1, 1],
        [0, 1, 0],
        [1, 1, 1]
    ]

    cols = len(arr)
    rows = len(arr[0])

    arr_indices = [-1, 0, 1]
    col_max = []
    
    for i in range(1, cols - 1):
        row_sum = []
        for j in range(1, rows - 1):
            sum = 0
            for x in arr_indices:
                for y in arr_indices:
                    sum = sum + hourglass[x + 1][y + 1] * arr[i + x][j + y]
            row_sum.append(sum)
            sum = 0
        row_max = max(row_sum)
        col_max.append(row_max)        

    return max(col_max)

print(hourglassSum(arr))
