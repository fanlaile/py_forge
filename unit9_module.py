import math
import random
import unit7_func as u7

print(math.pi)
print(math.pow(2, 10))

res = u7.calc_sum(1,2)
print(res)

rand_num = random.randrange(1, 100)
print("随机数", rand_num)

def mul(x,y):
    return x*y

if __name__ == "__main__":#用于本文件自测，调试用的代码，别的文件导入时不会调用
    print("本文件直接运行，执行测试")
    print(mul(6,7))




























# #安装
# pip install requests

# #查看已安装包
# pip list

# #导出依赖清单（给别人部署项目用）
# pip freeze > requirements.txt

# #别人拿到项目一键安装全部依赖
# pip install -r requirements.txt
