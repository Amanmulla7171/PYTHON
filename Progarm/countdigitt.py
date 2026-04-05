num = 123456
count = 0
while num != 0:
     num //= 10  # Integer division by 10 removes the last digit
     count += 1  # Increment the count for each digit removed
print("Number of digits:", count)
