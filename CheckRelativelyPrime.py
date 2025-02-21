def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if gcd(num1, num2) == 1:
    print(f"{num1} and {num2} are relatively prime.")
else:
    print(f"{num1} and {num2} are not relatively prime.")
