"""
字符串的常见操作包括
获取长度:len
查找内容:find,index,rfind,rindex
判断:startswith,endswith,isalpha,isdigit,isalnum,isspace
计算出现次数:count
替换内容:replace
切割字符串:split,rsplit,splitlines,partition,rpartition
修改大小写;capitalize,title,upper,lower
空格处理:ljust,rjust,center,lstrip,rstrip,strip
字符串拼接:join
"""

path = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"

# 获取长度:len

print(len(path))

# 查找内容:find.index,rfind,rindex

# 获取图片文件名:d9c8750bed0b3c7d089fa7d55720d6cf.png
# find:从左往右查找第一个值,返回位置,如果找不到任何一个,返回-1
i = path.find("_") + 1
print(path[i:])

# 获取图片扩展名
# rfind:从右往左查找第一个值,返回位置,如果找不到任何一个,返回-1
i = path.rfind(".")
print(path[i:])

# index:从左往右查找第一个值,返回位置,如果找不到任何一个,报错
# rindex:从右往左查找第一个值,返回位置,如果找不到任何一个,报错

# 判断:startswith,endswith,isalpha,isdigit,isalnum,isspace

# startswith,endswith:字符串是否以XXX开始/结束,返回boolean
print(path.startswith("https"))
print(path.endswith(".png"))

# isalpha:检测字符串是否只由字母组成,返回boolean
# isdigit:检测字符串是否只由数字组成,返回boolean
# isalnum:检测字符串是否只由字母或数字组成,返回boolean
# isspace:检测字符串是否只由空格组成,返回boolean

# 计算出现次数:count
# 统计某个字符或某段字符串在整个字符串中出现的次数,返回int
print(path.count("."))
print(path.count("//"))

#替换内容:replace
#替换字符串中指定的内容
i=path.replace('baidu', 'google')
print(i)


