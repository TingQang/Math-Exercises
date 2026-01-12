# LaTeX项目Makefile

.PHONY: all clean pdf biber validate help

# 默认目标
all: clean pdf biber pdf pdf

# 清理编译文件
clean:
	@echo "清理编译文件..."
	@rm -rf build/
	@mkdir -p build
	@rm -f *.aux *.bbl *.bcf *.blg *.fdb_latexmk *.fls *.lof *.log *.lot *.out *.run.xml *.toc *.xdv

# 编译PDF
pdf:
	@echo "编译PDF..."
	@pdflatex -interaction=nonstopmode -output-directory=build main.tex

# 处理参考文献
biber:
	@echo "处理参考文献..."
	@biber build/main

# 验证编译结果
validate:
	@echo "验证编译结果..."
	@./scripts/validate.sh

# 帮助信息
help:
	@echo "LaTeX项目构建命令:"
	@echo "  make all      - 完整编译（清理+编译+参考文献+最终编译）"
	@echo "  make clean    - 清理编译文件"
	@echo "  make pdf      - 编译PDF"
	@echo "  make biber    - 处理参考文献"
	@echo "  make validate - 验证编译结果"
	@echo "  make help     - 显示此帮助信息"