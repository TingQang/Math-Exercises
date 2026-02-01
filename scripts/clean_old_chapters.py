#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
清理旧的章节文件，保留章节文件夹
"""

import os

# 项目根目录
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# 内容目录
CONTENT_DIR = os.path.join(PROJECT_ROOT, 'content')

# 特殊文件，需要保留
SPECIAL_FILES = ['ch00.tex', 'ch99.tex']

def clean_old_chapters():
    """清理旧的章节文件"""
    # 收集所有章节文件夹
    chapter_folders = []
    for item in os.listdir(CONTENT_DIR):
        item_path = os.path.join(CONTENT_DIR, item)
        if os.path.isdir(item_path) and item.startswith('ch'):
            chapter_folders.append(item)
    
    # 按章节号排序
    chapter_folders.sort()
    
    # 收集需要删除的旧章节文件
    old_chapter_files = []
    for item in os.listdir(CONTENT_DIR):
        item_path = os.path.join(CONTENT_DIR, item)
        if os.path.isfile(item_path) and item.endswith('.tex') and item not in SPECIAL_FILES:
            # 检查是否存在对应的章节文件夹
            chapter_name = item.replace('.tex', '')
            if chapter_name in chapter_folders:
                old_chapter_files.append(item)
    
    # 删除旧章节文件
    deleted_count = 0
    for old_file in old_chapter_files:
        old_file_path = os.path.join(CONTENT_DIR, old_file)
        os.remove(old_file_path)
        print(f"已删除旧章节文件：{old_file_path}")
        deleted_count += 1
    
    print(f"\n清理完成！共删除了 {deleted_count} 个旧章节文件")

def main():
    """主函数"""
    print("开始清理旧的章节文件...")
    clean_old_chapters()
    print("清理完成！")

if __name__ == '__main__':
    main()
