n = int(input())
nums = [int(x) for x in input().split()] # list comprehension

max_ele = nums[0]

for num in nums:
    if num > max_ele:
        max_ele = num

print(max_ele)
