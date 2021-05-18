from functools import lru_cache

@lru_cache(maxsize=3)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def main():
    n = 3000
    for i in range(n):
        print(f"{i}\t{fib(i)}")

if __name__ == '__main__':
    main()
