t = int(input())

while t > 0:
    amount = int(input())
    s = input()

    carlsen = 0
    chef = 0
    for match in s:
        if match == "C":
            carlsen += 2
        elif match == "N":
            chef += 2
        else:
            carlsen += 1
            chef += 1
    
    points = 0
    if carlsen > chef:
        points = 60 * amount
    elif carlsen == chef:
        points = 55 * amount
    else:
        points = 40 * amount

    print(points)

    t -= 1
