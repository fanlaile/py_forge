# Day5 dict set
# 字典操作

person = {
    "username": "fan",
    "age": 30,
    "skill": ["c","c++","python"]
}
print(person["username"])
print(person.get("phone","unknown"))

# 改增
person["age"] = 31
person["location"] = "shenzhen"
print(person)

for k,v in person.items():
    print(f"key:{k}, value:{v}")

#set集合
data = [1,1,2,2,3,4,4,4]
s = set(data)
print("去重",s)
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print("交集",s1 & s2)
print("并集",s1 | s2)
print("差集",s1 - s2)

#空集合
es = set()
print(type(es))
print(type({}))

src = [2,2,1,3,3,5]
temp = {}
for i in src:
    temp[i] = None
res = list(temp.keys())
print(res)