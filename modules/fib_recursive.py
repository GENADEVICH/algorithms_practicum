import time

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    test_values = [20, 25, 30, 35, 40]
    for n in test_values:
        start = time.time()
        result = fib(n)
        end = time.time()
        print(f"fib({n}) = {result}, Time: {round((end - start) * 1000, 2)}ms")
