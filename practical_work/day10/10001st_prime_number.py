"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

def isPrime(n):
    if n < 2:
        return
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def nthPrime(number):
    prime_count = 0
    num = 1

    while prime_count != number:
        num += 1
        if isPrime(num):
            prime_count += 1
    return num


print(nthPrime(10001))
