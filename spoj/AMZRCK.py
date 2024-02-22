p = 5**0.5
for _ in range(int(input())):
    n = int(input()) + 2
    print(int(((1 + p) ** n - (1 - p) ** n) / (2**n * p)))
