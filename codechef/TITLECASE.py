t = int(input())

while t > 0:
    s = input()
    words = s.split()

    for word in words:
        if word[0].isupper():
            print(word, end=" ")
        else:
            print(word.capitalize(), end=" ")
    print()

    t -= 1
