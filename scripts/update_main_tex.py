#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新主文档main.tex中的章节导入语句，指向章节文件夹中的章节主文件
"""

import os
import re

# 项目根目录
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# 主文档路径
MAIN_TEX_PATH = os.path.join(PROJECT_ROOT, 'main.tex')
# 内容目录
CONTENT_DIR = os.path.join(PROJECT_ROOT, 'content')

# 特殊文件，不需要处理
SPECIAL_FILES = ['ch00.tex', 'ch99.tex']

def update_main_tex_imports():
    """更新主文档中的章节导入语句"""
    # 读取主文档内容
    with open(MAIN_TEX_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 收集所有章节文件夹
    chapter_folders = []
    for item in os.listdir(CONTENT_DIR):
        item_path = os.path.join(CONTENT_DIR, item)
        if os.path.isdir(item_path) and item.startswith('ch') and item not in SPECIAL_FILES:
            chapter_folders.append(item)
    
    # 按章节号排序
    chapter_folders.sort()
    
    # 特殊文件名称（不包含.tex）
    special_names = [f.replace('.tex', '') for f in SPECIAL_FILES]
    
    # 更新导入语句
    updated_lines = []
    for line in lines:
        # 检查是否是章节导入语句
        if '\input{content/' in line:
            # 提取章节名称
            for chapter_folder in chapter_folders:
                if f'\input{{content/{chapter_folder}}}' in line or f'\input{{content/{chapter_folder}/' in line:
                    # 更新为新的导入路径
                    new_line = f'\input{{content/{chapter_folder}/{chapter_folder}}}\n'
                    updated_lines.append(new_line)
                    break
            else:
                # 检查是否是特殊文件
                is_special = False
                for special_name in special_names:
                    if f'\input{{content/{special_name}}}' in line:
                        # 保持特殊文件的导入语句不变
                        updated_lines.append(line)
                        is_special = True
                        break
                if not is_special:
                    # 其他导入语句保持不变
                    updated_lines.append(line)
        else:
            # 非导入语句保持不变
            updated_lines.append(line)
    
    # 保存更新后的主文档
    with open(MAIN_TEX_PATH, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)
    
    print(f"已更新主文档 {MAIN_TEX_PATH}")
    print(f"处理了 {len(chapter_folders)} 个章节文件夹")

def main():
    """主函数"""
    print("开始更新主文档中的章节导入语句...")
    update_main_tex_imports()
    print("更新完成！")

if __name__ == '__main__':
    main()
