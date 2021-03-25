from itertools import permutations as perms
n = int(input(''))
s = 'ААООУУЫЫ'
s += ('Т'*n)[:-1]
l = []
for s in perms(s, n):
	g = ''.join(list(s))
	l.append(g)
l = list(set(l))

def isValid(word):
	words = {'АА', 'ОО', 'УУ', 'АЫ', 'ЫА', 'ОУ', 'УА', 'А', 'О', 'У', 'Ы', ''}
	a = list(set(word.split('Т')))
	if len(a) == 1 and a[0] == '':
		return False
	for i in a :
		if len(i) > 2:
			return False
		if i not in words:
			return False
	return True

counter = 0 

for b in l:
	if isValid(b):
		counter += 1

print(counter%2021)