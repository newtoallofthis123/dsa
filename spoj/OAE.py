for _ in range(int(input())):
    n = int(input()) - 1
    print((4 * pow(8, n, 314159) + 5 * pow(10, n, 314159)) % 314159)
