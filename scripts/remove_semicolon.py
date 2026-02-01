#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
删除所有章节文件中题型末尾的分号
"""

import os
import re

# 项目根目录
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# 内容目录
CONTENT_DIR = os.path.join(PROJECT_ROOT, 'content')

# 正则表达式模式：匹配\pt{...}命令，捕获括号内的内容
PT_PATTERN = re.compile(r'(\\pt\{)(.*?)(\})')

# 特殊文件，不需要处理
SPECIAL_FILES = ['ch00.tex', 'ch99.tex']

def remove_semicolon_in_file(filename):
    """删除单个文件中题型末尾的分号"""
    file_path = os.path.join(CONTENT_DIR, filename)
    
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 统计替换次数
    replacement_count = 0
    
    # 定义替换函数
    def replace_func(match):
        nonlocal replacement_count
        prefix = match.group(1)  # \pt{
        topic = match.group(2)    # 题型内容
        suffix = match.group(3)  # }
        
        # 去除题型末尾的分号（中英文）
        new_topic = topic.rstrip('；').rstrip(';')
        
        if new_topic != topic:
            replacement_count += 1
            print(f"  替换{filename}中的题型：'{topic}' -> '{new_topic}'")
        
        return f"{prefix}{new_topic}{suffix}"
    
    # 执行替换
    new_content = PT_PATTERN.sub(replace_func, content)
    
    # 保存文件
    if replacement_count > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    return replacement_count

def main():
    """主函数"""
    print("开始删除题型末尾的分号...")
    
    # 收集所有章节文件
    chapter_files = []
    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith('.tex') and filename not in SPECIAL_FILES:
            chapter_files.append(filename)
    
    # 按文件名排序
    chapter_files.sort()
    print(f"找到{len(chapter_files)}个章节文件")
    
    # 遍历文件，删除分号
    total_replacements = 0
    for filename in chapter_files:
        print(f"处理文件：{filename}")
        count = remove_semicolon_in_file(filename)
        total_replacements += count
        print(f"  替换了{count}个题型")
    
    print(f"\n处理完成！共替换了{total_replacements}个题型")
    print("请记得运行update_csv.py更新CSV文件")

if __name__ == '__main__':
    main()