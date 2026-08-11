a=[]
while True:
    x=int(input("请输入学生成绩："))
    if x<0 or x>100:
        break
    else:
     a.append(x)
    continue
b=10
c=[]
for i in range(len(a)):
    if a[i]+b<100:
     c.append(int(a[i])+b)
print(c)
def count(num):
    if num>=60:
        return "合格"
    else:
        return "不合格"
d=[]
for score in c:
 d.append(count(score))
print(d)