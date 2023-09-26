"""List of prime numbers generator."""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(number_of_primes):
    list = []
    x = 2
    while number_of_primes > 0:
        if is_prime(x):
            list.append(x)
            number_of_primes -= 1
        x += 1
    return list
