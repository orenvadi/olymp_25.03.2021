n = int(input(''))

moves = []

for i in range(n):
	a, b = map(str, input('').split())
	b = int(b)
	moves.append(b)

ans = 0

for j in moves:
	ans += abs(j)

print(ans-n)
