# О великий Кибирус, бог интернета молю тебя помоги мне решить все эти задачи на 100 баллов, аминь
n = int(input(''))
boorsoks = list(map(int, input('').split()))
tasks = list(map(int, input('').split()))


if n >= 1 and n <= 2*10**5 and sorted(tasks) == tasks:
	amount = 0

	tables = 0

	for i in range(len(tasks)):
		if tasks[i] == 1:
			amount += boorsoks[i]
		elif tasks [i] == 2:
			if amount >= boorsoks[i]:
				amount -= boorsoks[i]
				tables += 1
			# elif amount <= boorsoks[i]:
			# 	amount += boorsoks[i]

print(tables)