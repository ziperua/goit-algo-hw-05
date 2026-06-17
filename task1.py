def caching_fibonacci(): #outter function
    cache = dict()
    def fibonacci(present):#inner function
        if present <= 0: return 0
        if present == 1: return 1
        if present in cache: return cache[present]

        cache[present] = fibonacci(present-1)+fibonacci(present-2) #recursion
        return cache[present]
    return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))