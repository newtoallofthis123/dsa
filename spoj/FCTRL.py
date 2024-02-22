t = int(input())

nums = []

for _ in range(t):
    nums.append(int(input()))

for num in nums:
    count = 0
    i = 5
    while num // i > 0:
        count += num // i
        i *= 5

    print(count)
