# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
    # without any remainder.
# What is the smallest positive number that is evenly divisible by all of the 
    # numbers from 1 to 20?
from_what = int(input('Enter First Number:> '))
to_what = int(input('Enter Final Number (Both Inclusive):> '))
range_obj = range(from_what,to_what+1)
# 10 = 2 * 5.......LCM() of all the numbers from 1 to 10 will give 2520
def factorization(n):
    if n == 1:
        return None
    factors = {} # {2 : how much it occured , 3 : how much it occured}
    occurance = 0
    current_num = 2
    while n % 2 == 0 :
        n /= 2
        occurance += 1
    if occurance != 0:
        factors[current_num] = occurance
    for i in range(3,int(n)//2 + 1):
        if n % i == 0:
            current_num , occurance = i , 0
            while n % i == 0 :
                n /= i
                occurance += 1
            factors[int(current_num)] = occurance
        else:
            continue
    if n != 1:
        factors[int(n)] = 1
    return factors

def smallest_number(range_obj):
    overall_factors = [] # structure ---> [{2:2,3:2}, {1:2,2:2} ,  {101:2} , {12:1 , 2:4}]
    readed_max_factors = {}
    for i in range_obj:
        val = factorization(i)
        if val is not None:
            overall_factors.append(val)
    for i in overall_factors:
        for j in i.keys():
            if j not in readed_max_factors.keys() or readed_max_factors.get(j) < i[j]:
                readed_max_factors[j] = i[j]
    product = 1
    for i in readed_max_factors.keys():
        product *= i ** readed_max_factors[i]
    return product
print(smallest_number(range_obj))