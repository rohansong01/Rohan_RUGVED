n = int(input("Enter the number : "))
def fib(n: int):
    if (n == 1):
        return (0)
    elif (n == 2):
        return (1)
    else:
        return (fib(n - 1) + fib(n - 2))


print("The fibonacci of", n, " is", fib(n))