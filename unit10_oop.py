class Person:
    count = 0#类属性，所有实例共享
    def __init__(self, name: str, age: int):#构造方法，实例化对象时自动调用
        self.name = name#实例属性
        self.age = age
        self._b = 20     #约定私有
        self.__c = 30    #名称改写

    def say_hello(self):
        print(f"你好，我叫{self.name}，今年{self.age}岁")

class Student(Person):
    def __init__(self, name, age, stu_id):#
        super().__init__(name, age)#调用父类方法
        self.stu_id = stu_id

    def show_stu_info(self):
        self.say_hello()
        print(f"我的学号 {self.stu_id}")

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):#调试打印
        return f"《{self.title}》"

class Car:
    def __init__(self, brand: str, max_speed: int):
        self.brand = brand
        self.max_speed = max_speed

    def run(self, speed):
        #speed可以直接调用
        print(f"{self.brand}以{speed}KM/h行驶")
        if speed > self.max_speed:
            print("已超速")
if __name__ == "__main__":
    my_car = Car("比亚迪", 120)
    my_car.run(80)
    my_car.run(140)



#测试
p = Person("张三",20)
p.say_hello()

s1 = Student("小王",19,"S10086")
s1.show_stu_info()

bk = Book("Python开发实战")
print(bk)

car = Car("LINk&CO", 150)#car就是对象
car.run(160)



# 对象包含两部分：

# 1. **属性（成员变量）**：对象身上存的数据 `my_car.brand`、`my_car.max_speed`
# 2. **方法（成员函数）**：对象可以做的动作