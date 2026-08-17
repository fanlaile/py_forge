# Day4 list tuple练习

# 1.列表基础操作
my_list = [11,22,33,44]
print("原始列表:", my_list)
print(my_list[0])
print(my_list[1:3])
print(my_list[::-1])
print("列表长度:", len(my_list))

# 增删
my_list.append(55)
my_list.extend([66,77])
my_list.insert(0,0)
print("追加后", my_list)

pop_val = my_list.pop()
print(f"pop弹出的值：{pop_val}, 列表：{my_list}")

my_list.remove(0)
print("remove后", my_list)

#查询
print(22 in my_list)
print(my_list.index(33))

#2.元组练习
my_tuple = (100,200,300)
print("\n元组切片",my_tuple[0:2])

#单元素元组
t_s = (88,)
print(type(t_s))

#元组内部嵌套列表
mix_tuple = (1,[2,3])
mix_tuple[1].append(4)
print("嵌套元组：",mix_tuple)

#解包
x,y,z = my_tuple
print(f"解包 x={x}, y={y}, z={z}")

nums = []
for i in range(5):
    n = int(input(f"请输入第{i+1}个数:"))
    nums.append(n)

print("列表：", nums)
print("max: ",max(nums))
print("min: ",min(nums))
