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