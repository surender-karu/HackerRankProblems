def rotate_right_in_place_using_n_space(a, d):
    n = len(a)
    arr = []

    start_num = n - d

    for i in range(n):
        num = start_num + i
        arr.append(a[num % n])

    return arr

# n = 10
# d = 2
# | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
# | 9 | 10 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
def rotate_right_in_place(a, d):
    for i in range(d):
        n = len(a) - 1        
        temp = a[n]

        while n > 0:
            a[n] = a[n - 1]
            n = n - 1

        a[0] = temp

    return a

