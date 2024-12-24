def fibonacci(n):
    return [0, 1] + [fib[i-1] + fib[i-2] for i in range(2, n)]