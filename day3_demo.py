# Day3 运算符与条件分支
# 1.算术运算
a = 7
b = 2
print("a / b =", a / b)
print("a // b =", a // b)
print("a ** b =", a ** b)

# 2.连续比较
num = 15
print(10 < num < 20)

# 3.if elif else
score = 78
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = 'B'
elif score >= 60:
    grade = 'C'
else:
    grade = 'D'
print(f"分数{score}, 等级{grade}")

# 4.三目运算符
is_pass = "及格" if score >= 60 else "不及格"
print(is_pass)

# 5.逻辑短路演示
x = 0
res = x > 10 and print("不会打印这行")
print(res)

num = int(input("请输入一个数："))
if num > 0:
    print("正数")
elif num < 0:
    print("负数")
else:
    print("零")