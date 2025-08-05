import csv
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

path = Path('weather_data/sitka_weather_07-2018_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index,column_header in enumerate(header_row):
#     print(index,column_header)

# 提取日期和最高、最低温度
dates,highs,lows = [],[],[]
for row in reader:
    current_date = datetime.strptime(row[2],'%Y/%m/%d')
    try:
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {curent_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
print(highs)

plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()
ax.plot(dates,highs,color='red',alpha=0.5)
ax.plot(dates,lows,color='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

ax.set_title("Daily High and Low Temperatures, July 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()

