for _ in range(int(input())):
	n, m = map(int, input().split())
	print('%d.00' % (pow(2, n+1) - pow(2, m+1)))
