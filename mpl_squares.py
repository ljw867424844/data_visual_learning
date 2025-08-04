"""绘制简单的折线图"""
import matplotlib.pyplot as plt

# 创建列表，存储要用来制作图形的数据
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

# 使用内置样式
plt.style.use('seaborn-v0_8')

# 在一个图形（figure）中绘制一或多个绘图（plot）
# 变量 fig 表示由生成的一系列绘图构成的整个图形
# 变量 ax 表示图形中的绘图，使用这个变量来定义和定制绘图。
fig,ax = plt.subplots()
ax.plot(input_values,squares,linewidth=4)   # 输入值，输出值，线条粗细

# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value",fontsize=14)

# 设置刻度标记的样式
ax.tick_params(labelsize=14)

plt.show()
