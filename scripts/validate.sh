#!/bin/bash
# LaTeX编译验证脚本

echo "=== LaTeX编译验证 ==="

# 检查PDF文件是否存在
if [ -f "build/main.pdf" ]; then
    echo "✅ PDF文件生成成功: build/main.pdf"
    echo "   文件大小: $(stat -c%s build/main.pdf) bytes"
else
    echo "❌ PDF文件未生成"
    exit 1
fi

# 检查编译日志中的严重错误
if grep -q "Fatal error" build/main.log; then
    echo "❌ 发现致命错误"
    grep "Fatal error" build/main.log
    exit 1
else
    echo "✅ 无致命错误"
fi

# 检查警告数量
warning_count=$(grep -c "Warning" build/main.log)
if [ "$warning_count" -gt 0 ]; then
    echo "⚠️  发现 $warning_count 个警告"
    echo "   主要警告:"
    grep "Warning" build/main.log | head -3
else
    echo "✅ 无警告"
fi

echo ""
echo "=== 验证完成 ==="