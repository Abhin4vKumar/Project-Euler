def funcn(n,d):
    continue_ = False
    if isinstance(d,tuple) and isinstance(n,int):
        continue_ = True
    else:
        print('n == class int , d == class tuple')
    multiples = []
    sum_ = 0
    code = 'if '
    count = 0
    for i in d:
        if count == 0:
            extra_code = ''
        else:
            extra_code = 'or '
        count+=1
        code += extra_code + f'i%{i} == 0 '
    code += ':\n\tmultiples.append(i)'
    if continue_:
        for i in range(n):
            exec(code)
    sum_ = sum(multiples)
    print(sum_)
funcn(1000,(3,5))