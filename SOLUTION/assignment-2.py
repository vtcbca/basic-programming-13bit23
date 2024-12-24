def is_prime(n):
    if n <= 1:
        return False
    return not any(n % i == 0 for i in range(2, int(n**0.5) + 1))