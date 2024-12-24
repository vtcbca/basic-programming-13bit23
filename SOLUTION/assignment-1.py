factorial_memo = {0: 1}
def factorial(n):
    return 1 if n == 0 else factorial_memo.get(n, n * factorial(n - 1))