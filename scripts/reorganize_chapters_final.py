#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重新组织章节文件，使其与李永乐考研复习全书的章节顺序一致
"""

import os
import shutil
import re

# 项目根目录
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# 内容目录
CONTENT_DIR = os.path.join(PROJECT_ROOT, 'content')

# 李永乐复习全书的章节顺序
# 格式：(文件名, 章节标题)
CHAPTER_ORDER = [
    # 高等数学部分
    ('ch01.tex', '函数、极限、连续'),
    ('ch02.tex', '一元函数微分学'),
    ('ch03.tex', '一元函数积分学'),
    ('ch04.tex', '向量代数和空间解析几何'),
    ('ch05.tex', '多元函数微分学'),
    ('ch06.tex', '多元函数积分学'),
    ('ch07.tex', '无穷级数'),
    ('ch08.tex', '常微分方程'),
    
    # 线性代数部分
    ('ch09.tex', '行列式'),
    ('ch10.tex', '矩阵'),
    ('ch11.tex', '向量'),
    ('ch12.tex', '线性方程组'),
    ('ch13.tex', '矩阵的特征值和特征向量'),
    ('ch14.tex', '二次型'),
    
    # 概率论与数理统计部分
    ('ch15.tex', '随机事件和概率'),
    ('ch16.tex', '随机变量及其分布'),
    ('ch17.tex', '多维随机变量及其分布'),
    ('ch18.tex', '随机变量的数字特征'),
    ('ch19.tex', '大数定律和中心极限定理'),
    ('ch20.tex', '数理统计的基本概念'),
    ('ch21.tex', '参数估计'),
    ('ch22.tex', '假设检验'),
]

# 特殊文件，不需要重新组织
SPECIAL_FILES = ['ch00.tex', 'ch99.tex']

def get_chapter_title(file_path):
    """从文件中提取章节标题"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'\\chapter\{(.*?)\}', content)
    if match:
        return match.group(1)
    return None

def reorganize_chapters():
    """重新组织章节文件"""
    print("开始重新组织章节文件...")
    
    # 1. 创建临时目录
    temp_dir = os.path.join(PROJECT_ROOT, 'temp_chapters')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # 2. 复制特殊文件到临时目录
    print("复制特殊文件到临时目录...")
    for special_file in SPECIAL_FILES:
        special_path = os.path.join(CONTENT_DIR, special_file)
        if os.path.exists(special_path):
            temp_path = os.path.join(temp_dir, special_file)
            shutil.copy2(special_path, temp_path)
            print(f"  复制 {special_file} 到 {temp_path}")
    
    # 3. 收集所有章节文件及其标题
    print("收集所有章节文件及其标题...")
    chapter_files = {}
    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith('.tex') and filename not in SPECIAL_FILES:
            file_path = os.path.join(CONTENT_DIR, filename)
            title = get_chapter_title(file_path)
            if title:
                chapter_files[title] = filename
                print(f"  {filename}: {title}")
    
    # 4. 按照李永乐复习全书的顺序，将文件复制到临时目录
    print("按照李永乐复习全书的顺序组织文件...")
    for new_file, expected_title in CHAPTER_ORDER:
        if expected_title in chapter_files:
            old_file = chapter_files[expected_title]
            old_path = os.path.join(CONTENT_DIR, old_file)
            new_path = os.path.join(temp_dir, new_file)
            shutil.copy2(old_path, new_path)
            print(f"  复制 {old_file}({expected_title}) 到 {new_file}")
        else:
            print(f"  警告：未找到章节 '{expected_title}'")
    
    # 5. 清空原content目录
    print("清空原content目录...")
    for filename in os.listdir(CONTENT_DIR):
        file_path = os.path.join(CONTENT_DIR, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"  删除 {filename}")
    
    # 6. 将临时目录中的文件复制回content目录
    print("将临时目录中的文件复制回content目录...")
    for filename in os.listdir(temp_dir):
        temp_path = os.path.join(temp_dir, filename)
        new_path = os.path.join(CONTENT_DIR, filename)
        shutil.copy2(temp_path, new_path)
        print(f"  复制 {filename} 到 {new_path}")
    
    # 7. 清理临时目录
    print("清理临时目录...")
    shutil.rmtree(temp_dir)
    
    print("章节文件重新组织完成！")

if __name__ == '__main__':
    reorganize_chapters()