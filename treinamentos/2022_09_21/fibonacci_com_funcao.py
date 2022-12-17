def fibonacci(val):
    if val <= 1:
        return val
    return fibonacci(val-1) + fibonacci(val-2)

v = int(input())
print(fibonacci(v))