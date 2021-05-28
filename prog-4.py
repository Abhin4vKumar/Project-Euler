def calc():
    largest = {}
    items = []
    for i in range(100,1000):
        for j in range(100,1000):
            prod = i*j
            str_prod = str(prod)
            if str_prod == str_prod[::-1]:
                largest['i'] = i
                largest['j'] = j
                items.append(prod)
    return {'largest':largest,'items':items}
data = calc()
while True:
    try:
        exec(input(':$ '))
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(e)