g_val = 10
# 1.基础函数
def calc_sum(a,b):
    return a+b

print(calc_sum(11,22))
if __name__ == "__main__":
    print("unit7 测试")

#2.多返回值
def get_min_max(lst):
    return min(lst),max(lst)

mi,ma = get_min_max([5,1,9,3])
print(mi,ma)

#3.可变参数
def sum_all(*args):
    s = 0
    for num in args:
        s += num
    return s#没有return 返回none

print(sum_all(1,2,3,4))

def test():
    global g_val#修改外部全局变量，global声明
    g_val = 20

test()
print(g_val)