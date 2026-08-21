# 列表推导式
lst = [i*3 for i in range(1,8) if i%2==1]
print("列表推导式", lst)

#生成器 yield ，`yield`产出一个值，挂起函数状态。**不会一次性把全部数据放进内存**，适合大数据、大序列，节省内存。
#**生成器只能遍历一次，消耗完毕之后，再次 for 遍历不会产出任何数据**。
def my_gen(max_num):
    for i in range(max_num):
        yield i * 10
        print("yield后执行")

g = my_gen(4)
for v in g:
    print("gen yield:", v)

#装饰器:在不修改原函数代码、不修改调用方式前提下，给函数增加额外功能比如统计耗时、日志打印。
import functools

def time_cost(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        res = func(*args, **kwargs)
        cost = time.time() - start
        print(f"函数{func.__name__}耗时：{cost:.4f}s")
        return res
    return wrapper

@time_cost
def calc_sum(n):
    s = 0
    for i in range(n):
        s += i
    return s

print(calc_sum(200000))

nums = [10,20,30]
it = iter(nums)#迭代器记住遍历位置，**消耗式，取完就没**。`iter()`拿到迭代器，`next()`取下一个元素
print(next(it))
print(next(it))
print(next(it))


def even_gen(max_num):
    for n in range(max_num):
        if n % 2 == 0:
            yield n
print("test 1:")
g = even_gen(10)
for num in g:
    print(num)

print("test 2:")
src = [5,22,13,35,8,41,19]
# 使用列表推导式完成
res = [i for i in src if i > 20]
print(res) # [22,35,41]

print("test 3:")
def check_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i in args:
            if i < 0:
                print("参数不能为负数")
                return
        else:
            res = func(*args, **kwargs)
            return res
    return wrapper

@check_args
def calc(a,b):
    return a + b

print(calc(10,20))  #30
print(calc(-5, 8))  #打印：参数不能为负数，无返回


