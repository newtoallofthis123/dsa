for i in range(int(input())):
    x, n = map(int, input().split())
    x += x // (n - 1)

    print(x if x % n else x - 1)
