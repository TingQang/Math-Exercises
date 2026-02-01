#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复章节主文件中的小节导入语句，使用正确的相对路径
"""

import os
import re

# 项目根目录
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# 内容目录
CONTENT_DIR = os.path.join(PROJECT_ROOT, 'content')

def fix_section_imports():
    """修复所有章节主文件中的小节导入语句"""
    # 收集所有章节文件夹
    chapter_folders = []
    for item in os.listdir(CONTENT_DIR):
        item_path = os.path.join(CONTENT_DIR, item)
        if os.path.isdir(item_path) and item.startswith('ch'):
            chapter_folders.append(item)
    
    # 按章节号排序
    chapter_folders.sort()
    
    for chapter_folder in chapter_folders:
        # 章节主文件路径
        chapter_main_file = os.path.join(CONTENT_DIR, chapter_folder, f'{chapter_folder}.tex')
        
        if not os.path.exists(chapter_main_file):
            print(f"警告：{chapter_main_file} 不存在")
            continue
        
        # 读取章节主文件内容
        with open(chapter_main_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 修复小节导入语句
        # 原来的导入语句：\input{section_XX.tex}
        # 新的导入语句：\input{content/chXX/section_XX.tex}
        updated_content = content
        section_pattern = re.compile(r'(\\input\{)(section_\d+\.tex)(\})')
        
        def replace_section_import(match):
            section_file = match.group(2)
            return f'\\input{{content/{chapter_folder}/{section_file}}}'
        
        updated_content = section_pattern.sub(replace_section_import, updated_content)
        
        # 保存修复后的章节主文件
        with open(chapter_main_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"已修复 {chapter_main_file} 中的小节导入语句")
    
    print(f"共修复了 {len(chapter_folders)} 个章节主文件")

def main():
    """主函数"""
    print("开始修复章节主文件中的小节导入语句...")
    fix_section_imports()
    print("修复完成！")

if __name__ == '__main__':
    main()
