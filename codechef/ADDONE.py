def add_large_numbers(num1, num2):
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    num2 = num2.zfill(len(num1))
    carry = 0
    result = ''
    for i in range(len(num1) - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        result = str(digit_sum % 10) + result
        carry = digit_sum // 10
    if carry:
        result = str(carry) + result
    
    return result

t = int(input())

while t > 0:
    s = input()

    s = add_large_numbers(s, '1')

    print(s)

    t -= 1
