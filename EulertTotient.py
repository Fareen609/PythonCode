def euler_totient(n):
    count = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            count += 1
    return count
import math
num = int(input("Enter a number : "))
totient_value = euler_totient(num)
print(f"The Euler's Totient of {num} is {totient_value}.")
