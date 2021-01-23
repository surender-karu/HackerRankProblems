def rotLeft(a, d):
    n = len(a)
    right_shift_places = n - d
    arr = []

    start_num = n - right_shift_places

    for i in range(n):
        num = start_num + i
        arr.append(a[num % n])

    return arr

def rotate_right_in_place(a, d):


    return a

print(rotLeft([1, 2, 3, 4, 5], 4))
