import time
import math

def is_prime(n):
    """Return True if n is a prime number, if not false"""
    if n == 1:
        return False #1 is not a prime

    #If it's even and NOT 2, then its not a prime
    if n == 2:
        return True

    if n > 2 and n % 2 == 0:
        return False

    max_div = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_div, 2):
        if n % d == 0:
            return False
    return True

# ===== Time Function =====

t0 = time.time()
for n in range(1,100000):
    is_prime(n)
t1 = time.time()
print("Time taken:", t1-t0)