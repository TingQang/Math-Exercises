from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np

# ===================== 1. 基础配置 =====================
# 替换为你的图片本地路径（建议把图片放在代码同目录）
img_path = "v2-6f78aad86a41f11856a9ca52bda2050a_1440w.jpg"  
# 字体路径（Windows默认微软雅黑，Mac/Linux替换对应字体）
font_path = "C:/Windows/Fonts/msyh.ttc"  

# ===================== 2. 打开并初始化图片 =====================
img = Image.open(img_path).convert("RGB")
draw = ImageDraw.Draw(img)

# 定义字体（缩小字号，适配伞面大小）
font_small = ImageFont.truetype(font_path, 16)  # 伞上文字用更小字号
font_mid = ImageFont.truetype(font_path, 22)    # 中字体（阶段注释）
font_big = ImageFont.truetype(font_path, 26)    # 大字体（标题）

# 定义颜色（低饱和度，不抢画面）
color_white = (255, 255, 255)    # 白色（主文字）
color_green = (46, 139, 87)      # 草绿色（成长注释）
color_gold = (255, 215, 0)       # 金色（高分/标题）
color_black = (0, 0, 0)          # 黑色（描边）
color_bg = (0, 0, 0, 100)        # 半透明黑色（文字背景）

# ===================== 3. 添加文字注释（完全避开人物区域） =====================
# 标题（顶部居中，加半透明背景条）
title = "数学一 · 分数成长树"
title_width = draw.textlength(title, font=font_big)
title_x = (img.width - title_width) // 2
# 绘制标题背景条（半透明，不遮挡画面）
draw.rectangle([title_x-10, 15, title_x+title_width+10, 50], fill=color_bg)
draw.text((title_x, 20), title, font=font_big, fill=color_gold, 
          stroke_width=1, stroke_fill=color_black)

# 树苗分数标注（移到树苗右侧空白处，避开人物）
# 最矮树苗 → 基础分（左下角空白）
draw.text((150, 600), "基础分 80-90", font=font_small, fill=color_white, 
          stroke_width=1, stroke_fill=color_black)
# 中间树苗 → 目标分（树苗右侧空白）
draw.text((500, 580), "目标分 110-120", font=font_small, fill=color_white, 
          stroke_width=1, stroke_fill=color_black)
# 最高树苗 → 冲刺分（右上角空白）
draw.text((700, 550), "冲刺分 130+", font=font_small, fill=color_gold, 
          stroke_width=1, stroke_fill=color_black)

# 备考阶段注释（移到画面左右两侧空白区）
# 左侧空白 → 一轮复习
draw.text((50, 250), "一轮复习 · 扎根基础", font=font_mid, fill=color_green, 
          stroke_width=1, stroke_fill=color_black)
# 右侧空白 → 二轮强化
draw.text((950, 250), "二轮强化 · 拔高提分", font=font_mid, fill=color_green, 
          stroke_width=1, stroke_fill=color_black)
# 标题下方 → 三轮冲刺（居中，不遮挡人物）
stage_text = "三轮冲刺 · 高分成型"
stage_width = draw.textlength(stage_text, font=font_mid)
stage_x = (img.width - stage_width) // 2
draw.text((stage_x, 80), stage_text, font=font_mid, fill=color_gold, 
          stroke_width=1, stroke_fill=color_black)

# ========== 核心修改：把错题本文字放在伞上 ==========
# 伞面文字（调整坐标适配伞的位置，字号更小更贴合）
umbrella_text = "错题本遮风挡雨"
umbrella_width = draw.textlength(umbrella_text, font=font_small)
umbrella_x = 200  # 伞面水平居中坐标
umbrella_y = 180  # 伞面垂直居中坐标
# 伞面文字加轻微描边，保证在伞的图案上清晰
draw.text((umbrella_x, umbrella_y), umbrella_text, font=font_small, fill=color_gold, 
          stroke_width=1, stroke_fill=color_black)

# 趣味注释（上岸祝福移到画面右下角空白）
fun_text = "上岸！数学一120+ "
fun_width = draw.textlength(fun_text, font=font_small)
fun_x = img.width - fun_width - 50  # 右下角对齐
# 绘制趣味文字背景
draw.rectangle([fun_x-10, 650, fun_x+fun_width+10, 680], fill=color_bg)
draw.text((fun_x, 655), fun_text, font=font_small, fill=color_white, 
          stroke_width=1, stroke_fill=color_black)

# ===================== 4. 保存/显示图片 =====================
save_path = "math_one_tree_optimized.jpg"
img.save(save_path, quality=95)  # 高质量保存
print(f"优化后的图片已保存至：{save_path}")

# 显示图片（无坐标轴）
plt.figure(figsize=(12, 7), dpi=100)
plt.imshow(np.array(img))
plt.axis("off")
plt.tight_layout()  # 去除边距
plt.show()