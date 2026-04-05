n = 5
if n < 0:
    print("Factorial not defined for negative numbers")

factorial = 1
for i in range(1, n + 1):
    factorial *= i     # Multiply factorial by loop counter

print(f'Factorial of {n} is : {factorial}')
