'''
键盘输入两个整数，输出两个整数的和，输出差
input('输入第一个数:)
input('输入第二个数:)
'''

first_int = input('输入第一个数:')
second_int = input('输入第二个数:')
print('两数之和为：'+str(float(first_int)+float(second_int)))
print('两数之差为：'+str(float(first_int)-float(second_int)))

'''
str ---> int int(a) 但是如果'9.9"而且是字符串类型转成int的时候报错了
str ---> float float(a)
int ----> str str(a)
float ----> str str(a)
int ---> float float(a)
float ---> int int(a) 只不过float类型中小数点后面的数字被抹掉了
'''