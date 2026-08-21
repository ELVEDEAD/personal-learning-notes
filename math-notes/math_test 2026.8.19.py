c = []
while True:
    try:
        b = int(input("请输入学生成绩："))
    except ValueError:
        break
    if 0 <= b <=750:
        c.append(b)
        continue
    else:
        break
print("成绩列表", c)
def a():
    total=0
    max=c[0]
    min=c[0]
    for i in range(len(c)):
       total+=c[i]
       e=total/len(c)
       if c[i]>=max:
           max=c[i]
       if c[i]<=min:
           min=c[i]
    return max,min,total,e
max,min,total,e=a()
print(f"最大值为:{max}")
print(f"最小值为:{min}")
print(f"平均值为:{e}")