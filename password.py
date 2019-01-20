answer = 'joyce520'
i = 3
while i > 0:
	guess = input('請輸入密碼: ')
	if guess == answer:
		print('登入成功!')
		break
	elif i > 1:
		i = i - 1
		print('密碼錯誤! 還有', i, '次機會')
	else:
		print('密碼錯誤!')
		break