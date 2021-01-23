s = 'a'
a = 10

def repeatedString(s, n):
    str_len = len(s)

    if str_len == 1 and s == 'a':
        return n

    count_a_in_str = 0

    for c in s:
        if c == 'a':
            count_a_in_str = count_a_in_str + 1

    if count_a_in_str == 0:
        #no a in s
        return 0
    
    num_repeats = n // str_len

    tail_str_len = n % str_len

    remaining = 0
    for i in range(tail_str_len):
        if s[i] == 'a':
            remaining = remaining + 1

    return num_repeats * count_a_in_str + remaining

print(repeatedString(s, 10))