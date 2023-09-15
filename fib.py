previous = {0:0, 1:1}

def fib(i):
    for inc in range(i-1):
        if inc not in previous:
            fib(inc)
    if i in previous.keys():
        return previous[i]
    first = fib(i - 1)
    second = fib(i-2)
    result = first + second
    previous[i] = result
    return result

print(fib(1000))
