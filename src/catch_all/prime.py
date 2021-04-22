def is_prime(n):
    if not isinstance(n, int):
        return False
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True
