t = int(input())

while t > 0:
    n = int(input())
    s = input()

    # window 2 elements
    i = 0
    j = 1
    res = ""
    words = {
            "00": "A",
            "01": "T",
            "10": "C",
            "11": "G"
            }
    while j < n:
        word = s[i] + s[j]
        res += words[word]
        i += 2
        j += 2
    print(res)

    t -= 1
