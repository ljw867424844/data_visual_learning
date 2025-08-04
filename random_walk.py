import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    """一个生成随机游走数据的类"""

    def __init__(self,num_points=5000):
        """初始化随机游走的属性"""
        self.num_points = num_points

        # 所有的随机游走都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """计算随机游走包含的所有点"""

        # 不断游走，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:

            # 决定前进的方向以及沿这个方向前进的距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step ==0 and y_step ==0:
                continue

            # 计算下一个点的x坐标和y坐标
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


# 只要程序处于活动状态，就不断地模拟随机游走
while True:
    
    # 创建一个RandomWalk实例
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # 将所有的点都绘制出来
    plt.style.use('classic')
    fig,ax = plt.subplots(figsize=(16, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none', s=1)
    ax.set_aspect('equal')

    # 突出起点和终点
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    
    plt.show()
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
    

            
