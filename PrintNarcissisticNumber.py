def narcissistic_numbers(n):
    start = 10**(n-1)
    end = 10**n
    narcissistic_nums = []
    for num in range(start, end):
        num_str = str(num)
        sum_of_powers = sum(int(digit) ** n for digit in num_str)
        if sum_of_powers == num:
            narcissistic_nums.append(num)
    return narcissistic_nums
n = int(input("Enter the value of 'n': "))
result = narcissistic_numbers(n)
if result:
    print(f"All {n}-digit narcissistic numbers are: {', '.join(map(str, result))}")
else:
    print(f"No {n}-digit narcissistic numbers found.")
