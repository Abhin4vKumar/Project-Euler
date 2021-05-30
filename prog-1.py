def funcn(n):
    if isinstance(n,int):
        pass
    else:
        print('Unsupported Data types')
        return None
    sum = 0
    for i in range(n):
        if i%3 == 0 or i%5 == 0:
            sum += i
    print(sum)
funcn(1000)
