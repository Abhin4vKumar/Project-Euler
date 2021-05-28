import itertools
def no_of_divisors(n):
    if n == 1:
        return 1
    nod , occurance = 1 , 0
    while n % 2 == 0 :
        n /= 2
        occurance += 1
    nod*=occurance+1
    for i in range(3,int(n)//2 + 1):
        if n % i == 0:
            occurance = 0
            while n % i == 0 :
                n /= i
                occurance += 1
            nod*=occurance+1
    if n != 1:
        nod+=1
    return nod
def main():
    for n in itertools.count(2):
        k = n // 2
        term = int(n*(n+1)/2)
        if n % 2:
            a, b = 2*k+1, k+1
        else:
            a, b = k, 2*k+1
        no_of_divisors_term = no_of_divisors(a)*no_of_divisors(b)
        if no_of_divisors_term >= 500:
            return term
print(main())