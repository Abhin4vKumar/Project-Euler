# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?
def check_prime_for_odd(n):
    if n ==2 or n ==3:
        return True
    elif n < 2:
        return False
    for i in range(3,n//2 + 1):
        if n%i ==0:
            return False
    return True
def function():
    count = 1
    i = 1
    while count < 10001:
        if check_prime_for_odd(i):
            count += 1
        i += 2
    print(i - 2)
function()