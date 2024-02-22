from math import ceil 
while True:
	p, b, f = map(int, input().split())
	if b == 0: break
	print('No accounting tablet')  if (p-f)%b else print(int(ceil(abs(p-f)/b/3.0)))
