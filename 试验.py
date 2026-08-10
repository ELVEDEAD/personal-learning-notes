import matplotlib.pyplot as plt
start = int(input("起始抽数："))
end = int(input("结束抽数："))
draw_tags = []
prob_data = []
for n in range(start, end + 1):
    cycle_pos = n % 79
    if cycle_pos == 0:
        cycle_pos = 79
    if cycle_pos <= 65:
        p = 0.8
    elif 66 <= cycle_pos <= 70:
        p = 0.8 + 4 * (cycle_pos - 65)
    elif 71 <= cycle_pos <= 75:
        p = 20.8 + 8 * (cycle_pos - 70)
    elif 76 <= cycle_pos <= 78:
        p = 60.8 + 10 * (cycle_pos - 75)
    else:
        p = 100
    draw_tags.append(f"第{n}抽")
    prob_data.append(p)
    print(f"第{n}抽概率：{p:.2f}%")
plt.bar(draw_tags, prob_data, color="#4285F4")
plt.title("循环重置型抽卡概率变化")
plt.ylabel("概率(%)")
plt.show()