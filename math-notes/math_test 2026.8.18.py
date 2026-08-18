while True:
  nub1=input("请输入一位整数")
  nub2=input("请输入一位整数")
  nub3=input("请输入一位整数")
  nub4=input("请输入一位整数")
  try:
      A=int(nub1)
      B=int(nub2)
      C=int(nub3)
      D=int(nub4)
      break
  except ValueError:
      print("请重新输入")
def a1():
    print(A+B)
    print("Okay")
    b1()
def b1():
    print(A+B+C)
    print("Okay")
    c1()
    print("OVER")
def c1():
    print("A+B+C+D")
    res=A+B+C+D
    return res
a1()
result=c1()
print(f"拿到的数字：{result}")
total=0
sum=0
for i in range(result):
    sum+=i
    total+=1
print(f"已循环{total}轮")
print(f"数字总和：{sum}")