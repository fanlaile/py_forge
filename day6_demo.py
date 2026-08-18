# 1. range练习
print("===range===")
for i in range(3,10,2):
    print(i)

# 2. enumerate拿到下标+数值
print("===enumerate===")
fruits = ["apple","banana","orange"]
for index,name in enumerate(fruits):
    print(index, name)

# 3. for else
print("===for else===")
data = [11,22,33]
for v in data:
    if v == 22:
        print("find it")
        break
else:
    print("遍历完")