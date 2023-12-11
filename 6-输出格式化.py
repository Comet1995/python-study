name = "蔡徐坤"
age = 26
# 我喜欢听26岁的蔡徐坤唱歌
print("我喜欢听" + str(age) + "岁的" + name + "唱歌")
"""
符号：
%% 输出%号
%s 字符串 string
%d 有符号十进制整数 digit
%f 浮点数 float
%c 字符 char
%u 无符号十进制整数
%o 八进制整数
%x 十六进制整数
%b 二进制
%e 科学计数法
"""
print("我喜欢听%d岁的%s唱歌" % (age, name))

money = 999.95

# 26岁的蔡徐坤一首歌挣了999.95元

print("%d岁的%s一首歌挣了%f元" % (age, name, money))
print("%s岁的%s一首歌挣了%s元" % (age, name, money))
print("%d岁的%s一首歌挣了%.2f元" % (age, name, money))
