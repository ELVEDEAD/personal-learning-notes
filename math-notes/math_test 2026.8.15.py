#简易庞加莱回归
import random
start=[0,1,2,3]
now=start.copy()
count=0
print("初始状态:",start)
while True:
    index=random.randint(0,3)
    now[index]=1-now[index]
    count=count+1
    if now==start:
        print("回到初始状态:",now)
        break
    print(f"经过{count}次变换后状态:,回到初始状态！")
    print("最终状态:",now)