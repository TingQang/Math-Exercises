#!/bin/bash
# LaTeX项目构建脚本 (跨平台)
# 使用方法: ./build.sh [clean|pdf|biber]

set -e

if [ "$1" = "clean" ]; then
    echo "清理旧文件..."
    rm -rf build/
    mkdir -p build
    rm -f *.aux *.bbl *.bcf *.blg *.fdb_latexmk *.fls *.lof *.log *.lot *.out *.run.xml *.toc *.xdv
    echo "清理完成"
    exit 0
fi

if [ "$1" = "pdf" ]; then
    echo "编译PDF..."
    pdflatex -interaction=nonstopmode -output-directory=build main.tex
    exit 0
fi

if [ "$1" = "biber" ]; then
    echo "处理参考文献..."
    biber build/main
    exit 0
fi

# 默认构建流程
echo "清理旧文件..."
rm -rf build/
mkdir -p build
rm -f *.aux *.bbl *.bcf *.blg *.fdb_latexmk *.fls *.lof *.log *.lot *.out *.run.xml *.toc *.xdv

echo "首次编译..."
pdflatex -interaction=nonstopmode -output-directory=build main.tex

echo "处理参考文献..."
biber build/main

echo "最终编译..."
pdflatex -interaction=nonstopmode -output-directory=build main.tex
pdflatex -interaction=nonstopmode -output-directory=build main.tex

echo "构建完成！输出文件: build/main.pdf"