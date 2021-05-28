# The sum of the squares of the first ten natural numbers is, 385

# The square of the sum of the first ten natural numbers is, 3025

# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is . 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one 
# hundred natural numbers and the square of the sum.

def sum_of_squares(n):
    # sum of squares ---> n(n+1)(2*n + 1)/6
    return (n * (n+1) * ( (2 * n )+ 1))/6
def square_of_sum(n):
    #square of sum ----> (n(n+1)/2)^2
    return ((n * (n + 1))/2) ** 2
def difference(a,b):
    #difference --> |a - b| --or-> (n(n+1)/2)(n(n+1)/2 - (2*n + 1)/3)
    res = int( a - b )
    if res <= 0:
        return -1 * res
    return res
def function():
    n = int(input('Enter Number :> '))
    print(difference(sum_of_squares(n),square_of_sum(n)))
function()