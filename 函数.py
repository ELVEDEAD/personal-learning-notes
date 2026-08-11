import numpy as np
import matplotlib.pyplot as plt
#开始输入
a=float(input("请输入一个数字："))
b=float(input("请输入下一个数字："))
res=a+b
lista=[a,b,res]
listb=['数字1','数字2','和']
plt.bar(listb,lista,color=['#555555',"#8A2525",'#556666'])
plt.title("柱状图")
plt.show()
