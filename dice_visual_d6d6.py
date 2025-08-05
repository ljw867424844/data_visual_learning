"""模拟同时掷两个D6骰子1000次"""
import plotly.express as px
from dice import Dice

# 创建两个个D6
dice_1 = Dice()
dice_2 = Dice()

# 投几次骰子并将结果存储在一个列表中
results = []
for i in range(1000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
poss_results = range(2,max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化
title = "Results of Rolling Two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results,y=frequencies,title=title,labels=labels)

# 进一步定制图形
fig.update_layout(xaxis_dtick=1)

# 由于未知原因，fig.show()打不开网页，故用下面的方法
fig.write_html("dice_visual_d6d6.html")
print("图表已经写入 HTML 文件，请手动打开")
