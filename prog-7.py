# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?
import math
def check_prime_for_odd(n):
    if n == 1:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
def function():
    # even numbers are skipped so 2 is also skipped which is the only even prime no
    #hence count should be = 1
    count = 1
    i = 1
    while count < 10001:
        if check_prime_for_odd(i):
            count += 1
        i += 2
    print(i - 2)
function()