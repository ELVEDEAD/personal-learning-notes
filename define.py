import numpy as np
import matplotlib.pyplot as plt
def hanshu(x, y):
    result = x + y
    return result
apple = eval(input("输入一个数："))
bag = eval(input("输入一个数："))
res = hanshu(apple, bag)
c = [apple, bag, res]
if sum(c) >= 15:
    print("周佳佑是傻瓜")
else:
    print(c)
L = ["数一", "数二", "相加结果"]
plt.bar(L, c, color=["blue", "green", "red"])
plt.title("可视化图表")
plt.show()