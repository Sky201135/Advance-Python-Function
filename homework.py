n = int(input("Enter a number: "))

odd_numbers = [x for x in range(n) if x % 2 != 0]

odd_numbers_alt = [x for x in range(1, n, 2)]

print("Odd numbers:", odd_numbers)
print("Odd numbers (alt):", odd_numbers_alt)