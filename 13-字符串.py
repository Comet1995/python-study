"""
切片: 字符串，列表
格式:
字符串变量[start:end]
字符审变量[start:end:step]
默认是从左向右一个一个取元囊
从左往右为0 -- n-1
从右往左为-n -- -1
step:
1.步长
2.方同
"""
s1 = "hello"
s2 = s1
s3 = "hello"
print(s1, s2, s3)
print(id(s1))
print(id(s2))
print(id(s3))
print(s1[2:4])
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
"""
https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
"""
path = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"

# 查找内容:find.index,rfind,rindex

# 获取图片文件名:d9c8750bed0b3c7d089fa7d55720d6cf.png
# find:从左往右查找第一个值,返回位置,如果找不到任何一个,返回-1
i = path.find("_") + 1
print(path[i:])

# 获取图片扩展名
# rfind:从右往左查找第一个值,返回位置,如果找不到任何一个,返回-1
i = path.rfind(".")
print(path[i:])
