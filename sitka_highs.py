import csv
import matplotlib.pyplot as plt
from pathlib import Path

path = Path('weather_data/sitka_weather_07-2018_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index,column_header in enumerate(header_row):
#     print(index,column_header)

# 提取最高温度
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)
print(highs)

# 根据最高温度绘图
plt.style.use('classic')
fig,ax = plt.subplots()
ax.plot(highs,color='red')
ax.set_title("Daily High Temperatures, July 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()

