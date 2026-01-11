import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 生成函数图像示例：y = sin(x) 与 y = x - x^3/6 在 x ∈ [-π, π] 上的比较
x = np.linspace(-np.pi, np.pi, 1000)
y1 = np.sin(x)
y2 = x - x**3 / 6

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制函数图像
ax.plot(x, y1, label=r'$y = \sin(x)$', linewidth=2, color='blue')
ax.plot(x, y2, label=r'$y = x - \frac{x^3}{6}$', linewidth=2, linestyle='--', color='red')

# 添加辅助线
ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
ax.axvline(x=0, color='black', linestyle='-', linewidth=0.5)

# 设置坐标轴标签和标题
ax.set_xlabel(r'$x$', fontsize=12)
ax.set_ylabel(r'$y$', fontsize=12)
ax.set_title('函数图像比较', fontsize=14)

# 添加图例
ax.legend(fontsize=12, loc='upper right')

# 设置网格线
ax.grid(True, linestyle='--', alpha=0.7)

# 保存为矢量图（PDF格式）
plt.savefig('./images/function_comparison.pdf', format='pdf', dpi=300, bbox_inches='tight')

# 再生成一个几何图形示例：三角形及其内切圆
fig2, ax2 = plt.subplots(figsize=(6, 6))

# 三角形的三个顶点
A = np.array([0, 0])
B = np.array([4, 0])
C = np.array([1, 3])

# 绘制三角形
ax2.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'b-', linewidth=2, label='三角形')

# 计算三角形的内心和内切圆半径
# 边长
a = np.linalg.norm(B - C)
b = np.linalg.norm(A - C)
c = np.linalg.norm(A - B)

# 半周长
s = (a + b + c) / 2

# 内切圆半径
r = np.sqrt(s * (s - a) * (s - b) * (s - c)) / s

# 内心坐标
I = (a * A + b * B + c * C) / (a + b + c)

# 绘制内切圆
circle = plt.Circle(I, r, color='r', fill=False, linestyle='--', linewidth=2, label='内切圆')
ax2.add_artist(circle)

# 标注顶点
ax2.text(A[0] - 0.2, A[1] - 0.2, 'A', fontsize=12)
ax2.text(B[0] + 0.1, B[1] - 0.2, 'B', fontsize=12)
ax2.text(C[0] + 0.1, C[1] + 0.1, 'C', fontsize=12)

# 设置坐标轴范围
ax2.set_xlim(-1, 5)
ax2.set_ylim(-1, 4)
ax2.set_aspect('equal')

# 设置坐标轴标签
ax2.set_xlabel(r'$x$', fontsize=12)
ax2.set_ylabel(r'$y$', fontsize=12)
ax2.set_title('三角形及其内切圆', fontsize=14)

# 添加图例
ax2.legend(fontsize=12, loc='upper right')

# 设置网格线
ax2.grid(True, linestyle='--', alpha=0.7)

# 保存为矢量图（PDF格式）
plt.savefig('./images/triangle_circle.pdf', format='pdf', dpi=300, bbox_inches='tight')

print("矢量图生成完成！")