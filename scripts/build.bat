@echo off
REM LaTeX项目构建脚本
REM 使用方法: build.bat [clean|pdf|biber]

if "%1"=="clean" goto clean
if "%1"=="pdf" goto pdf
if "%1"=="biber" goto biber

REM 默认构建流程
echo 清理旧文件...
call :clean

echo 首次编译...
pdflatex -interaction=nonstopmode -output-directory=build main.tex

echo 处理参考文献...
biber build/main

echo 最终编译...
pdflatex -interaction=nonstopmode -output-directory=build main.tex
pdflatex -interaction=nonstopmode -output-directory=build main.tex

echo 构建完成！输出文件: build/main.pdf
goto end

:clean
echo 删除编译中间文件...
del /q *.aux *.bbl *.bcf *.blg *.fdb_latexmk *.fls *.lof *.log *.lot *.out *.run.xml *.toc *.xdv 2>nul
rd /s /q build 2>nul
md build
goto end

:pdf
echo 编译PDF...
pdflatex -interaction=nonstopmode -output-directory=build main.tex
goto end

:biber
echo 处理参考文献...
biber build/main
goto end

:end