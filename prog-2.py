def funcn(n,series=None,curr=None):
    series_ = [1,2]
    curr_ = len(series_)
    if series is not None:
        series_ = series
    if curr is not None:
        curr_ = curr
    series_.append(series_[curr_ - 1] + series_[curr_ - 2])
    curr_ += 1
    if series_[-1] <= n:
        print(series_[-1])
        return funcn(n,series_,curr_)
    else:
        rem_el = series_.pop()
        print(rem_el)
        print('Ended')
        print(series_[-1])
    print(sum(even_series_(series_)))
def even_series_(obj):
    even_series = []
    for i in obj:
        if i%2 ==0:
            even_series.append(i)
    return (even_series)

funcn(4000000)