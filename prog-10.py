# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


def check_prime_for_odd(n):
    if n ==2 or n ==3:
        return True
    elif n < 2:
        return False
    for i in range(3,n//2 + 1):
        if n%i ==0:
            return False
    return True

sum = 0
prime = 1
while prime < 2000000:
    if check_prime_for_odd(prime):
        sum += prime
    prime += 2
print(sum)
