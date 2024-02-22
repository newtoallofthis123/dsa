nums = []

while True:
    num = int(input())
    if num == 42:
        break
    nums.append(num)

for num in nums:
    if num == 42:
        break
    print(num)
