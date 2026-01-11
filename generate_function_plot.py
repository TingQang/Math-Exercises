import numpy as np
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 生成数据
x = np.linspace(-2, 2, 1000)
y1 = np.sin(x)
y2 = x - x**3 / 6

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制函数曲线
plt.plot(x, y1, label=r'$y = \sin(x)$', linewidth=2, color='blue')
plt.plot(x, y2, label=r'$y = x - \frac{x^3}{6}$', linewidth=2, color='red', linestyle='--')

# 添加标签和标题
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title(r'函数图像比较：$\sin(x)$ 与 $x - \frac{x^3}{6}$', fontsize=16)

# 添加网格线
plt.grid(True, alpha=0.3)

# 添加图例
plt.legend(fontsize=12)

# 保存为PDF矢量图
plt.savefig('images/function_comparison.pdf', dpi=300, bbox_inches='tight', format='pdf')

# 关闭图形
plt.close()

print('函数比较图已生成：images/function_comparison.pdf')
