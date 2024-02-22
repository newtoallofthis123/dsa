from math import sqrt
for _ in range(int(input())):
	n = int(input()) - 1
	print(int((sqrt(8*n + 1) + 1)/2 - 1))
