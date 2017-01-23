print("\n\n                  您好！欢迎光临侏罗纪公园~~~！！！！   ")
print('\n                                       程序开发：张锋, 版本：1.0')
print('\n###############################################################################')
print('\n    本系统按年龄购票，请输入正确的年龄!!!')

age=input('\n\n请输入您的年龄：')
	
while not age.isdigit():
    age = input('\n请输入数字，谢谢！: ')
    
age = int(age)

if age <= 4 or age >= 65 :
	print('\n\n               不用买票，免费游览！')
	
elif age <18 :
	print ('\n\n              半价购票，请付5元!')
	
elif age >=18 and age <=65 :
	print ('\n\n              请付费10元，谢谢光临！')	
	
	
while True :
	getwords = input("\n\n\n退出请输入quit,继续购票请输入ok:  ")
	if getwords.lower()=='quit':
		break
	
	if getwords.lower()=='ok':
		print('\n\n##############################################################################')
		print("\n\n                 欢迎继续购票！")
		
	age1=input('\n\n请输入您的年龄：')
	
	while not age1.isdigit():
		age1 = input('请输入数字，谢谢！: ')
    
	age1 = int(age1)

	if age1 <= 4 or age1 >= 65 :
		print('\n         不用买票，免费游览！')
	
	elif age1 <18 :
		print ('\n        半价购票，请付5元!')
	
	elif age1 >=18 and age1 <=65 :
		print ('\n        请付费10元，谢谢光临！')	
	

print("\n\n       谢谢惠顾，祝你玩的开心!\n\n\t")
    
	
