def call_cost():
	k=int(input('Введите код города:'))
	t=int(input('Введите длительность переговоров:'))
	if k==343:
		return t*15
	elif k==381:
		return t*18
	elif k==473:
		return t*13
	elif k==485:
		return t*11
	else:
		return "Нет информации об этом городе"
