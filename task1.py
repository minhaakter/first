numbers = list(map(int, input("Enter numbers: ").split()))
sum_even = sum_odd = 0

for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
