#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重新组织章节文件，使其与李永乐考研复习全书的章节顺序一致
"""

import os
import shutil

# 项目根目录
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# 内容目录
CONTENT_DIR = os.path.join(PROJECT_ROOT, 'content')

# 文件名与章节标题的映射关系
# 格式：(当前文件名, 新文件名, 章节标题)
FILE_MAPPING = [
    # 高等数学部分
    ('ch01.tex', 'ch01.tex', '函数、极限、连续'),
    ('ch02.tex', 'ch02.tex', '一元函数微分学'),
    ('ch03.tex', 'ch03.tex', '一元函数积分学'),
    ('ch04.tex', 'ch04.tex', '向量代数和空间解析几何'),
    ('ch05.tex', 'ch05.tex', '多元函数微分学'),
    ('ch06.tex', 'ch06.tex', '多元函数积分学'),
    ('ch07.tex', 'ch07.tex', '无穷级数'),
    ('ch08.tex', 'ch08.tex', '常微分方程'),
    
    # 线性代数部分
    ('ch08.tex', 'ch09.tex', '行列式'),  # 注意：这里的ch08.tex是之前的线性代数行列式章节
    ('ch09.tex', 'ch10.tex', '矩阵'),
    ('ch10.tex', 'ch11.tex', '向量'),
    ('ch11.tex', 'ch12.tex', '线性方程组'),
    ('ch12.tex', 'ch13.tex', '矩阵的特征值和特征向量'),
    ('ch13.tex', 'ch14.tex', '二次型'),
    
    # 概率论与数理统计部分
    ('ch14.tex', 'ch15.tex', '随机事件和概率'),
    ('ch15.tex', 'ch16.tex', '随机变量及其分布'),
    ('ch16.tex', 'ch17.tex', '多维随机变量及其分布'),
    ('ch17.tex', 'ch18.tex', '随机变量的数字特征'),
    ('ch18.tex', 'ch19.tex', '大数定律和中心极限定理'),
    ('ch19.tex', 'ch20.tex', '数理统计的基本概念'),
    ('ch20.tex', 'ch21.tex', '参数估计'),
    ('ch21.tex', 'ch22.tex', '假设检验'),
]

def reorganize_chapters():
    """重新组织章节文件"""
    print("开始重新组织章节文件...")
    
    # 创建临时目录，保存所有章节内容
    temp_dir = os.path.join(PROJECT_ROOT, 'temp_chapters')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # 1. 先将所有文件内容保存到临时目录
    print("保存所有章节内容到临时目录...")
    for old_file, new_file, chapter_title in FILE_MAPPING:
        old_path = os.path.join(CONTENT_DIR, old_file)
        if os.path.exists(old_path):
            temp_path = os.path.join(temp_dir, new_file)
            shutil.copy2(old_path, temp_path)
            print(f"  复制 {old_file} 到 {temp_path}")
    
    # 2. 更新临时文件中的章节标题
    print("更新临时文件中的章节标题...")
    for old_file, new_file, chapter_title in FILE_MAPPING:
        temp_path = os.path.join(temp_dir, new_file)
        if os.path.exists(temp_path):
            with open(temp_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 更新章节标题
            new_content = content.replace(f'\chapter{{{chapter_title}}}', f'\chapter{{{chapter_title}}}', 1)
            
            with open(temp_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  更新 {new_file} 中的章节标题为 {chapter_title}")
    
    # 3. 将临时文件复制回content目录
    print("将临时文件复制回content目录...")
    for old_file, new_file, chapter_title in FILE_MAPPING:
        temp_path = os.path.join(temp_dir, new_file)
        new_path = os.path.join(CONTENT_DIR, new_file)
        if os.path.exists(temp_path):
            shutil.copy2(temp_path, new_path)
            print(f"  复制 {temp_path} 到 {new_path}")
    
    # 4. 清理临时目录
    print("清理临时目录...")
    shutil.rmtree(temp_dir)
    
    print("章节文件重新组织完成！")

if __name__ == '__main__':
    reorganize_chapters()