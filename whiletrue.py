while True:
	mode = input('請輸入遊戲模式：(q 表離開)')
	if mode == 'q':
		break
	elif mode == '1':
		print('進入模式一')
	elif mode == '2':
		print('進入模式二')
	else:
		print('請輸入正確代號: 1/2/q')