"""
# new:      20231018
# edit:     syz
# handin due:   20231025
# 使用matplotlib绘制 f(x) = (sin((x-2))^2 * e^(-x^2) 函数,其中x的取值范围为[0, 2]
# 在图中添加合适的轴刻度、轴标签和图名等，并展示结果
"""

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(0, 2, 100)
fig = plt.figure()

f = (np.sin(x - 2)) ** 2 * np.e ** (-x ** 2)
plt.plot(x, f, "r-", label="f(x)")  # "r"为红色, "s"为方块, "-"为实线
plt.legend()

# 设置坐标轴范围
plt.xlim((-0.5, 2.5))
plt.ylim((-0.2, 1.2))
# 设置坐标轴刻度
my_x_ticks = np.arange(-0.5, 2.5, 0.3)
plt.xticks(my_x_ticks)

# 设置轴标签和图名
plt.title('f(x)= (sin((x-2))^2 * e^(-x^2)')
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.savefig('4_2_1_result.png', dpi=400, bbox_inches='tight')
plt.show()
