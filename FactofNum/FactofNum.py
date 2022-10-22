def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))


num = 7

result = factorial(num)
print("The factorial of", num, "is", result)
