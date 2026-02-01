#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将每章的.tex文件拆分为小节文件，并为每章创建文件夹
"""

import os
import re
import shutil

# 项目根目录
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# 内容目录
CONTENT_DIR = os.path.join(PROJECT_ROOT, 'content')

# 特殊文件，不需要处理
SPECIAL_FILES = ['ch00.tex', 'ch99.tex']

def split_chapter_to_sections(chapter_file):
    """将单个章节文件拆分为小节文件"""
    chapter_path = os.path.join(CONTENT_DIR, chapter_file)
    
    # 读取章节文件内容
    with open(chapter_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取章名
    chapter_match = re.search(r'\\chapter\{(.*?)\}', content)
    if not chapter_match:
        print(f"警告：{chapter_file} 中未找到章名")
        return
    chapter_name = chapter_match.group(1)
    
    # 创建章节文件夹
    chapter_folder = os.path.join(CONTENT_DIR, chapter_file.replace('.tex', ''))
    if not os.path.exists(chapter_folder):
        os.makedirs(chapter_folder)
        print(f"创建章节文件夹：{chapter_folder}")
    
    # 分割章节内容为小节
    # 匹配所有 \section{...} 及其内容
    section_pattern = re.compile(r'(\\section\{.*?\})(.*?)(?=\\section|$)', re.DOTALL)
    sections = section_pattern.findall(content)
    
    # 保存每个小节到单独的文件
    section_files = []
    for i, (section_header, section_content) in enumerate(sections, 1):
        # 提取小节名
        section_name_match = re.search(r'\\section\{(.*?)\}', section_header)
        if section_name_match:
            section_name = section_name_match.group(1)
        else:
            section_name = f"小节{i}"
        
        # 生成小节文件名
        section_filename = f"section_{i:02d}.tex"
        section_filepath = os.path.join(chapter_folder, section_filename)
        
        # 构建小节文件内容
        section_full_content = f"{section_header}{section_content}"
        
        # 保存小节文件
        with open(section_filepath, 'w', encoding='utf-8') as f:
            f.write(section_full_content)
        
        section_files.append(section_filename)
        print(f"  保存小节：{section_filename} - {section_name}")
    
    # 创建章节主文件，用于导入所有小节
    chapter_main_file = os.path.join(chapter_folder, chapter_file)
    with open(chapter_main_file, 'w', encoding='utf-8') as f:
        # 写入章名
        f.write(f"\\chapter{{{chapter_name}}}\n\n")
        
        # 导入所有小节
        for section_file in section_files:
            f.write(f"\\input{{{section_file}}}\n")
    
    print(f"  创建章节主文件：{chapter_file}")
    
    return chapter_folder

def main():
    """主函数"""
    print("开始将章节拆分为小节...")
    
    # 收集所有章节文件
    chapter_files = []
    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith('.tex') and filename not in SPECIAL_FILES:
            chapter_files.append(filename)
    
    # 按文件名排序
    chapter_files.sort()
    print(f"找到{len(chapter_files)}个章节文件")
    
    # 遍历文件，拆分为小节
    for filename in chapter_files:
        print(f"处理文件：{filename}")
        split_chapter_to_sections(filename)
    
    print("\n处理完成！")
    print("每个章节的小节文件已保存到对应的章节文件夹中")

if __name__ == '__main__':
    main()
