def fib(n):
    fib_series = [0, 1]
    for i in range(2, n + 1):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

if __name__ == "__main__":
    n = 10
    print(f"fib_array({n}) = {fib(n)}")
