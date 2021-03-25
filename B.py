#все верно но он меня отверг, если не верите можете проверить
a, b, c, d, m = map(int, input('').split())


if a <= 10**6 and b <= 10**6 and a >= 1 and b >= 1:
	if m <= 10**9 and m >= 2:
		if c == d and d == 1:
			if a <= 10**6 and b <= 10**6 and a >= 1 and b >= 1:
				if m <= 10**9 and m >= 2:
					if a <= 10**6 and b <= 10**6 and a >= 1 and b >= 1 and  c <= 10**6 and d <= 10**6 and c >= 1 and d >= 1:
						if m == 10:
							n = str((((a**b)**c)**d)%m)
							print(f'{int(n)}')