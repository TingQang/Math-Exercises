import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 1. 解决中文显示问题
rcParams['font.sans-serif'] = ['Microsoft YaHei']
rcParams['axes.unicode_minus'] = False
rcParams['font.family'] = 'sans-serif'

# 2. 定义题目中的 g(x)
def g(x):
    return np.where(x <= 1, x**2, x**3)

# 3. 拆分数据（适配 g(x) 的分段逻辑）
x_left = np.linspace(-2, 1, 1000)       # x ≤ 1 部分，包含 1
y_left = x_left ** 2
x_right = np.linspace(1, 2, 1000, endpoint=False)  # x > 1 部分，不包含 1
y_right = x_right ** 3

# 4. 创建画布
plt.figure(figsize=(8, 8), dpi=100)
ax = plt.gca()

# 5. 绘制曲线
ax.plot(x_left, y_left, color='#2E86AB', linewidth=2.5, label=r'$g(x)$')
ax.plot(x_right, y_right, color='#2E86AB', linewidth=2.5)

# ========== 新增：绘制 y=0 辅助线 ==========
ax.axhline(y=-0.03, color='red', linestyle='-', linewidth=1.5, alpha=0.7, label='$y=0$ 参考线')

# 分段点显示
ax.scatter([1], [1**2],           # x ≤ 1 段的端点 (1,1)
           color='#2E86AB', s=60, zorder=8,
           facecolors='#2E86AB', edgecolors='#2E86AB', linewidth=2.5,
           label='分段点 $(1,1)$')

# 6. 坐标轴设置
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, markersize=6)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, markersize=6)

# 7. 刻度调整
x_ticks = [-2, -1, 0, 1, 2]
x_tick_labels = [r'$-2$', r'$-1$', '', r'$1$', r'$2$']
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_tick_labels, fontsize=11)

for i, tick in enumerate(ax.get_xticklabels()):
    label_text = tick.get_text()
    if label_text in [r'$-2$', r'$-1$']:
        tick.set_y(-0.1)
    elif label_text in [r'$1$', r'$2$']:
        tick.set_y(-0.02)

y_ticks = [0, 1, 2, 4, 8]
y_tick_labels = ['', r'$1$', r'$2$', r'$4$', r'$8$']
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_tick_labels, fontsize=11)

for i, tick in enumerate(ax.get_yticklabels()):
    label_text = tick.get_text()
    if label_text in [r'$1$', r'$2$', r'$4$', r'$8$']:
        tick.set_x(-0.02)

# 手动绘制 0 刻度标签
ax.text(0.2, -0.3, r'$0$', fontsize=11, ha='center', va='center', color='black')
ax.text(-0.2, 0.2, r'$0$', fontsize=11, ha='center', va='center', color='black')

# 8. 标注关键点
key_points = [
    (-2, 4, r'$(-2,4)$'),
    (0, 0, r'$(0,0)$'),
    (1, 1, r'$(1,1)$'),
    (2, 8, r'$(2,8)$'),
]
for x_p, y_p, label in key_points:
    ax.plot([x_p, x_p], [0, y_p], color='#A23B72', linestyle='--', linewidth=1.2, alpha=0.8)
    ax.plot([0, x_p], [y_p, y_p], color='#A23B72', linestyle='--', linewidth=1.2, alpha=0.8)
    ax.text(x_p + 0.1, y_p + 0.1, label, fontsize=10, ha='left', va='bottom')

# 9. 图表配置
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1, 9)
ax.set_xlabel('$x$', fontsize=14, loc='right')
ax.set_ylabel('$g(x)$', fontsize=14, loc='top', rotation=0)
ax.legend(loc='upper right', fontsize=10, frameon=True, fancybox=True)
ax.grid(False)

# 保存图片
plt.savefig('g_x_final.pdf', bbox_inches='tight', dpi=300)
plt.show()