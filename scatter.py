"""绘制散点图"""
import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()

# 设置颜色渐变
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,s=10)

ax.set_title("Scatter Diagram",fontsize=24)
ax.set_xlabel("Value of X",fontsize=14)
ax.set_ylabel("Value of Y",fontsize=14)

ax.tick_params(labelsize=14)
# 在刻度标记表示的数足够大时，Matplotlib 将默认使用科学记数法。
ax.ticklabel_format(style='plain')

plt.show()
