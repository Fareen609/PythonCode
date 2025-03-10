def lucas_number(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
n = 10
print(f"The {n}th Lucas number is: {lucas_number(n)}")
