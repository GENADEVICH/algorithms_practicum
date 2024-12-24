import time

def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    test_values = [10, 15, 20, 25, 35]
    for n in test_values:
        start = time.perf_counter()
        result = fib(n)
        end = time.perf_counter()
        elapsed_time = (end - start) * 1000
        print(f"fib({n}) = {result}, Time: {elapsed_time:.6f}ms")
