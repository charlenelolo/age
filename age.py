driving = input('請問你有沒有開過車?(y/n)')
if driving != 'y' and driving != 'n':
	print('亂回答')

age = input('請問你的年齡?')
age = int(age)

if driving == 'y':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪，你怎麼開過車?')
elif driving == 'n':
	if age < 18:
		print('乖!')
	else:
		print('是不是不敢考駕照?')
else:
	print('亂回答')
