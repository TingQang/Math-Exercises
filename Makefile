# LaTeX项目Makefile

.PHONY: all clean pdf xelatex biber validate help latexmk

# 默认目标
all: clean latexmk

# 清理编译文件
clean:
	@echo "清理编译文件..."
	@rm -rf build/
	@mkdir -p build
	@rm -f *.aux *.bbl *.bcf *.blg *.fdb_latexmk *.fls *.lof *.log *.lot *.out *.run.xml *.toc *.xdv

# 使用latexmk自动编译（推荐）
latexmk:
	@echo "使用latexmk编译PDF..."
	@latexmk -xelatex -synctex=1 -interaction=nonstopmode -file-line-error -shell-escape -outdir=./build main.tex

# 编译PDF（xelatex）
xelatex:
	@echo "使用xelatex编译PDF..."
	@xelatex -interaction=nonstopmode -output-directory=build main.tex

# 编译PDF（pdflatex，保留兼容）
pdf:
	@echo "使用pdflatex编译PDF..."
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
	@echo "  make all      - 完整编译（清理+latexmk自动编译）"
	@echo "  make clean    - 清理编译文件"
	@echo "  make latexmk  - 使用latexmk自动编译（推荐）"
	@echo "  make xelatex  - 使用xelatex编译PDF"
	@echo "  make pdf      - 使用pdflatex编译PDF（兼容模式）"
	@echo "  make biber    - 处理参考文献"
	@echo "  make validate - 验证编译结果"
	@echo "  make help     - 显示此帮助信息"