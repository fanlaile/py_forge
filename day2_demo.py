# Day2 基础类型练习
# 1. 变量动态绑定

data = 123
print(data, type(data))
data = "fanwan"
print(data, type(data))

#2. 字符串切片练习
content = "wanxintianguai"
print(content[0])
print(content[0:5])
print(content[::-1]) #反转

#3. f-string格式化
username = "Fan"
year = 2026
info = f"用户名:{username}. 学习年份:{year}"
print(info)

#4. 字符串常用方法
msg = " python Backend "
print(msg.strip())
print(msg.upper())
print(msg.split())

#5. 布尔运算
is_study = True
print(not is_study)
print(1 > 2)

name = input("请输入你的名字:")
welcome = f"欢迎 {name} 学习python后端开发"
print(welcome)

print(name[::-1]) #反转

