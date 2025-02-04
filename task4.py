numbers = list(map(int, input("Enter the numbers: ").split()))
numbers.sort(reverse=True)

if len(numbers) > 1:
    print("Second highest number:", numbers[1])
else:
    print("Not enough numbers to determine the second highest.")
