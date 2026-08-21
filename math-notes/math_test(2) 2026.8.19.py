biaodan={}
amount=[]
while True:   
   name=str(input("请输入商品名称："))
   if name=="q":
      break
   price=str(input("请输入商品价格："))
   biaodan[name]=price
for i in range(len(biaodan)):
    if i<=len(biaodan):
      a=input("输入商品数量：")
      amount.append(a)
    else:
       break
print(f"表单为{biaodan}")
print(f"数量表{amount}")
def t(x,y):
   d=[]
   total=[]
   for u in x.values():
    d.append(u)  
   for s in range(len(y)):
      total.append(int(y[s])*int(d[s]))
   return total
total1=t(biaodan,amount)
print(f'各商品总价{total1}')
def c():
   if total1[s]>=5000:
      pass