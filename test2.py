import random
card_turple=('诸葛亮','曹操','司马懿','刘备','貂蝉','吕布')
package=[]
while 1:
	choose=int(input('''
	充值能让你变得更强！！
	请选择指令：
	1.抽卡
	2.查看背包
	3.整理背包
	4.退出
	'''))
	
	if choose == 1:
		num = int(input('请输入抽卡次数： '))
		for i in range(0,num):
			n = random.randint(0,6)
			print('你抽到了：{}'.format(card_turple[n]))
		
			package.append(card_turple[n])
		print('卡已存入背包')
		
	if choose == 2:
		if len(package) == 0:
			print('背包没有卡片，快去抽卡吧！')
		else:
			for i in package:
				print(i)
			
	if choose == 3:
		if len(package) == 0:
			print('背包没有卡片，快去抽卡吧！')
		else:
			package.sort()
			for i in package:
				print(i)
		
	if choose == 4:
		break
	
	
