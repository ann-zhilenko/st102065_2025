def find_two_smallest(a):
    b = a[0]
    c = a[1]
    if b > c:
        b, c = c, b

    for i in a:
        if i < b:
            c = b
            b = i
        elif i < c:
            c = i

    return b, c
