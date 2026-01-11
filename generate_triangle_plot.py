import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 三角形顶点坐标
A = (0, 0)
B = (4, 0)
C = (1, 3)

# 计算边长
a = np.sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2)  # BC
b = np.sqrt((A[0] - C[0])**2 + (A[1] - C[1])**2)  # AC
c = np.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)  # AB

# 计算半周长和面积
s = (a + b + c) / 2
area = 0.5 * np.abs((B[0] - A[0]) * (C[1] - A[1]) - (C[0] - A[0]) * (B[1] - A[1]))

# 计算内切圆半径
r = area / s

# 计算内切圆圆心（使用坐标公式）
x = (a * A[0] + b * B[0] + c * C[0]) / (a + b + c)
y = (a * A[1] + b * B[1] + c * C[1]) / (a + b + c)
center = (x, y)

# 创建图形
plt.figure(figsize=(8, 6))

# 绘制三角形
plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], linewidth=2, color='black')

# 标记顶点
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='red', s=50)
plt.text(A[0]-0.2, A[1]-0.2, 'A(0,0)', fontsize=12)
plt.text(B[0]+0.1, B[1]-0.2, 'B(4,0)', fontsize=12)
plt.text(C[0]+0.1, C[1], 'C(1,3)', fontsize=12)

# 绘制内切圆
incircle = Circle(center, r, fill=False, color='blue', linewidth=2, linestyle='--')
plt.gca().add_patch(incircle)

# 标记内切圆圆心
plt.scatter(center[0], center[1], color='blue', s=50)
plt.text(center[0]+0.1, center[1], f'内切圆圆心', fontsize=10)

# 设置坐标轴
plt.xlim(-1, 5)
plt.ylim(-1, 4)
plt.grid(True, alpha=0.3)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('三角形及其内切圆', fontsize=16)

# 保存为PDF矢量图
plt.savefig('images/triangle_circle.pdf', dpi=300, bbox_inches='tight', format='pdf')

# 关闭图形
plt.close()

print('三角形及其内切圆图已生成：images/triangle_circle.pdf')
