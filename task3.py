start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

total = sum(num for num in range(start, end + 1) if num % 3 == 0 and num % 5 != 0)
print("Sum:", total)
