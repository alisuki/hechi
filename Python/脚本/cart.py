#!/usr/bin/env python
# coding=utf-8
product_info = {
	'orange':'15',
	'bag':'120',
	'apple':'12',
	'banana':'3.5',
	'table':'260',
	'cup':'56',
	'nike':'1500',
}
	
cart = {}

RMB = input('往钱包充值：')

print	'''
-------------------------------------
可购买的商品有：
		orange:	15	元/斤
		   bag:	120	元/个
		 apple:	12	元/斤
		banana:	3.5	元/斤
		 table:	260	元/张
		   cup:	56	元/个
		  nike:	1500元/辆
-------------------------------------
'''
while True:
	choice_pro = raw_input('请选择商品：')	
	if product_info.has_key(choice_pro) == False:
		print "		商品未上架！"
		continue
	choice_num = input('      数量：')

	if cart.has_key(choice_pro) == False:
		cart[choice_pro] = choice_num
	else:
		cart[choice_pro] = cart[choice_pro] + choice_num

	anser = raw_input('继续购买？ y|n :')
	if anser == 'n':
		break

print '''\n\n\n你购物车里的商品有：
---------------------------------------------------------------------
	商品名称	单价（元）	数量（个）	总额（元）'''
count_all = 0
zong_all = 0
for i in cart.items():
	name = i[0]
	price =  float(product_info[name])
	count =  int(i[1])
	zong = price * count
	print '	',name,'		',price,'		',count,'		',zong
	count_all += count
	zong_all += zong
print '\n---------------------------------------------------------------------'
print '\n	总计：				',count_all,'个		',zong_all,'元'
print '\n---------------------------------------------------------------------'
RMB_YU = RMB - zong_all
print '					还剩余额：	',RMB_YU,'元\n\n\n'







#	print type(zong)
