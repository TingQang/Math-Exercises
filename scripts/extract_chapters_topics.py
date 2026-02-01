#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
导出所有正文章节和题型到CSV文件
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

# 正文章节文件列表（ch03.tex及以后）
def get_chapter_files():
    """获取所有正文章节文件"""
    chapter_files = []
    all_files = []
    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith('.tex'):
            all_files.append(filename)
            # 只排除特定文件，不进行长度检查
            if filename not in ['ch00.tex', 'ch01.tex', 'ch02.tex', 'ch99.tex']:
                chapter_files.append(filename)
    
    print(f"所有.tex文件: {all_files}")
    print(f"正文章节文件: {chapter_files}")
    return sorted(chapter_files)

def extract_chapter_section_topic(filename):
    """从单个文件中提取章节名称、小节名称和题型"""
    file_path = os.path.join(CONTENT_DIR, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取章节名称
    chapter_match = CHAPTER_PATTERN.search(content)
    if chapter_match:
        chapter_name = chapter_match.group(1)
        print(f"从{filename}提取到章节名称: {chapter_name}")
    else:
        chapter_name = ""
        print(f"从{filename}未提取到章节名称")
    
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
            print(f"从{filename}提取到小节名称: {section_name}")
        
        # 提取题型
        topic_match = TOPIC_PATTERN.search(line)
        if topic_match:
            topic = topic_match.group(1).strip().rstrip('；').rstrip(';')
            chapter_topic_data.append({
                '文件名': filename,
                '章名': chapter_name,
                '小节名': section_name,
                '题型': topic
            })
    
    print(f"从{filename}提取到{len(chapter_topic_data)}个题型")
    return chapter_topic_data

def main():
    """主函数"""
    print("开始提取章节和题型数据...")
    
    # 获取正文章节文件
    chapter_files = get_chapter_files()
    
    # 提取所有章节和题型数据
    chapter_topic_data = []
    for filename in chapter_files:
        file_data = extract_chapter_section_topic(filename)
        chapter_topic_data.extend(file_data)
    
    # 保存到CSV文件
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['文件名', '章名', '小节名', '题型']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        # 写入表头
        writer.writeheader()
        
        # 写入数据
        for data in chapter_topic_data:
            writer.writerow(data)
    
    print(f"成功导出 {len(chapter_topic_data)} 条数据到 {OUTPUT_CSV}")

if __name__ == '__main__':
    main()