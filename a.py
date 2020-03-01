import random
r = random.randint(1,100)
while True:
	num = input('请输入:')
	num = int(num)
	if num == r:
		print('对了')
		break
	elif num > r: 
		print('比答案大')
	else:
		print('比答案小')