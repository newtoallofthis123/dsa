t = int(input())

for _ in range(t):
    scores = {} 
    for i in range(22):
        runs, wickets = map(int, input().split())
        score = runs + (wickets * 20)
        scores[i+1] = score
    scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print(scores[0][0])
