import random
import time
#创建卡池
card_tuple = ('诸葛亮','曹操','司马懿','刘备','貂蝉')
#定义卡的权重
weight_list = [5,10,20,50,100]
#定义用于比较的权重列表
weight_compare = [5,15,35,85,185]
#创建背包
package_dic = {}

while 1:
	choose = int(input('''
	充值能让你变得更强！
	1.抽卡
	2.查看背包
	3.退出
	'''))
	if choose == 1:
		num = int(input('请输入抽卡次数： '))
		for i in range(0,num):
			int_Randcard = random.randint(1,weight_compare[-1])
			i = 0
			while int_Randcard > weight_compare[i]:
				i += 1
			print('你抽到的卡是：{}'.format(card_tuple[i]))
			if package_dic.__contains__(card_tuple[i]):
				package_dic[card_tuple[i]] += 1
			else:
				package_dic[card_tuple[i]] = 1
			time.sleep(0.3)
		print('卡已存入背包')
		print('___________________________')
		
			
	if choose == 2:
		if len(package_dic) ==0:
			print('背包暂无英雄，快去抽卡吧')
			print('_____________________')
		else:
			for key,value in package_dic.items():
				print('{} - 数量：{}'.format(key,value))
			print('___________________________')
	if choose == 3:
		break
	
