x1, y1, x2, y2, x3, y3 = map(int, input('').split())

points = 0

l1 = [ x1, x2, x3]
l2 = [ y1, y2, y3 ]

if l1.count(0) >= 2:
	points += 10

elif l2.count(0) >= 2:
	points += 10

else:
	for i in range (3):
		if l1[i] == 0 or l2[i] == 0:
			points += 1

if y1 >= 0 and y2 >= 0 and y3 >= 0:
	points += 50
if  x1 <= 0 and x2 <= 0 and x3 <= 0:
	points += 100

print(points)