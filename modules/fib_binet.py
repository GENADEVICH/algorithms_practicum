import math

def fib(n):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return round((phi ** n - psi ** n) / sqrt_5)

if __name__ == "__main__":
    n = 32
    print(f"fib({n}) = {fib(n)}")
