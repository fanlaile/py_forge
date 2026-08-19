#异常演示
try:
    x = int(1)#int("not_number")
except ValueError as e:
    print(f"发生错误:{e}")
finally:
    print("执行finally")#finally不加return，否则会覆盖掉try中的return

#文件写入 with open 不用手动close
with open("unit8_demo.txt","w",encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("This is a test file.\n")

#文件逐行读取
with open("unit8_demo.txt","r",encoding="utf-8") as f:
    for line in f:
        s = line.strip()  # 去掉换行符
        print(s)