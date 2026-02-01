#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新CSV文件内容，使其与重新组织后的章节结构一致
"""

import os
import re
import csv

# 项目根目录
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# 内容目录
CONTENT_DIR = os.path.join(PROJECT_ROOT, 'content')
# 输出CSV文件
OUTPUT_CSV = os.path.join(PROJECT_ROOT, 'chapter_topic_data.csv')

# 正则表达式模式
CHAPTER_PATTERN = re.compile(r'\\chapter\{(.*?)\}')
SECTION_PATTERN = re.compile(r'\\section\{(.*?)\}')
TOPIC_PATTERN = re.compile(r'\\pt\{(.*?)\}')

# 特殊文件，不需要处理
SPECIAL_FILES = ['ch00.tex', 'ch99.tex']

def get_chapter_title(file_path):
    """从文件中提取章节标题"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = CHAPTER_PATTERN.search(content)
    if match:
        return match.group(1)
    return None

def extract_chapter_section_topic(filename):
    """从单个文件中提取章节名称、小节名称和题型"""
    file_path = os.path.join(CONTENT_DIR, filename)
    
    # 提取章节名称
    chapter_title = get_chapter_title(file_path)
    if not chapter_title:
        print(f"  警告：未找到{filename}的章节标题")
        return []
    
    # 按行处理文件内容，提取小节名称和题型
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    section_name = ""
    chapter_topic_data = []
    
    for line in lines:
        # 提取小节名称
        section_match = SECTION_PATTERN.search(line)
        if section_match:
            section_name = section_match.group(1)
            print(f"  从{filename}提取到小节：{section_name}")
        
        # 提取题型
        topic_match = TOPIC_PATTERN.search(line)
        if topic_match:
            topic = topic_match.group(1).strip().rstrip('；').rstrip(';')
            chapter_topic_data.append({
                '文件名': filename,
                '章名': chapter_title,
                '小节名': section_name,
                '题型': topic
            })
            print(f"    提取到题型：{topic}")
    
    return chapter_topic_data

def main():
    """主函数"""
    print("开始更新CSV文件...")
    
    # 收集所有章节文件
    chapter_files = []
    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith('.tex') and filename not in SPECIAL_FILES:
            chapter_files.append(filename)
    
    # 按文件名排序
    chapter_files.sort()
    print(f"找到{len(chapter_files)}个章节文件")
    
    # 提取所有章节和题型数据
    all_data = []
    for filename in chapter_files:
        print(f"处理文件：{filename}")
        file_data = extract_chapter_section_topic(filename)
        all_data.extend(file_data)
    
    # 保存到CSV文件
    print(f"共提取到{len(all_data)}条数据，保存到{OUTPUT_CSV}")
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['文件名', '章名', '小节名', '题型']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        # 写入表头
        writer.writeheader()
        
        # 写入数据
        for data in all_data:
            writer.writerow(data)
    
    print("CSV文件更新完成！")

if __name__ == '__main__':
    main()