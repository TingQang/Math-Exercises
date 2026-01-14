# 使用latexmk进行编译，与VSCode settings.json保持一致
.PHONY: all clean cleanall

all:
	latexmk -xelatex -synctex=1 -interaction=nonstopmode -file-line-error -shell-escape -outdir=./build main.tex

# 清理中间文件，保留PDF
clean:
	latexmk -c -outdir=./build main.tex

# 清理所有编译产物，包括PDF
cleanall:
	latexmk -C -outdir=./build main.tex
	rm -f ./build/main.pdf
	rm -f ./build/main.synctex.gz