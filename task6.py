n = int(input("Enter the number of terms for the Fibonacci series: "))
a, b = 0, 1

print("Fibonacci Series:", a, b, end=" ")
for _ in range(n - 2):
    a, b = b, a + b
    print(b, end=" ")
