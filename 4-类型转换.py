name = 'zhangsan'
print(name)

#input

username = input('请输入姓名：') #阻塞性函数，运行到此处会暂停，input输入类型只为字符串类型
print(username)
print(type(username))

money = input('请输入金额：') 
print(money)
print(type(money))#输入数字也为字符串

#类型转换 str--->int

print(int(money)+1000)

#类型转换 int--->str

print(money+str(1000))




