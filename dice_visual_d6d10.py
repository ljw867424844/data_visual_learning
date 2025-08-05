import plotly.express as px
from dice import Dice

dice_1 = Dice()
dice_2 = Dice(10)

results = []
for i in range(50_000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

max_result = dice_1.num_sides + dice_2.num_sides
poss_results = range(2,max_result+1)
frequencies = [results.count(i) for i in poss_results]

title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results,y=frequencies,title=title,labels=labels)
fig.update_layout(xaxis_dtick=1)

fig.write_html("dice_visual_d6d10.html")
print("图表已经写入 HTML 文件，请手动打开")

