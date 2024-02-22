t = int(input())

while t > 0:
    s = input()

    window = 3
    happy = False

    vowels = ['a', 'e', 'i', 'o', 'u']

    while window < len(s):
        i = 0
        j = i + window
        
        while j <= len(s):
            sub = s[i:j]
            happy = True
            for a in sub:
                if a not in vowels:
                    happy = False
                    break
            if happy:
                break
            i += 1
            j += 1
        if happy:
            break
        window += 1

    if happy:
        print('Happy')
    else:
        print('Sad')

    t -= 1
