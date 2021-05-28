# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import math
def check_prime_for_odd(n):
    if n == 1:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
# prime is only checked for odd numbers... hence 2 is not checked....
sum = 2
prime = 1
while prime < 2000000:
    if check_prime_for_odd(prime):
        sum += prime
    prime += 2
print(sum)
