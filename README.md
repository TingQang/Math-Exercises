# 考研数学核心笔记 README.md

个人整理的考研数学复习笔记，全面覆盖高等数学、线性代数、概率论与数理统计三大核心模块。基于 LaTeX 构建，通过精细化配置实现专业排版、考点突出、高效编译等功能，适配考研复习全程的知识点梳理与查阅需求。

## 📚 项目核心特点

- **结构化梳理**：按学科模块拆分章节，文件组织清晰，覆盖考研数学全考点，便于分阶段复习与快速检索

- **专业排版体系**：基于 XeLaTeX 适配中文排版，数学公式规范美观，自定义多类主题环境与快捷命令，视觉层级分明

- **考点精准标记**：预设红/蓝/橙等主题色，通过专用命令标记考点、重点、难点，聚焦复习核心

- **自动化编译**：配置 VS Code + LaTeX Workshop 一键编译，自动管理输出目录与临时文件，提升写作效率

- **高度可定制**：支持自定义颜色方案、页面样式、定理环境，适配个性化笔记需求

## 🛠️ 编译环境配置

### 必需软件

1. TeX 发行版：MiKTeX 25.12+（Windows）/ TeX Live 2024+（跨平台）（需包含 XeLaTeX、biber、latexmk）

2. 编辑器：VS Code + LaTeX Workshop 扩展（推荐，已预设自动化配置）

### 环境验证

安装完成后，打开 VS Code 终端（Ctrl+`），输入以下命令验证环境可用性：

```bash

xelatex --version  # 验证 XeLaTeX 引擎
latexmk --version  # 验证自动化编译工具
biber --version    # 验证参考文献处理工具
```

## 🚀 快速开始

### 方法一：VS Code 一键编译（推荐）

1. 打开项目根目录，定位到核心编译入口 `main.tex`

2. 保存文件（Ctrl+S），自动触发编译（预设 `onSave`自动编译）

3. 编译完成后，通过快捷键 `Ctrl+Alt+V` 打开内置 PDF 预览

4. 双向同步：双击 PDF 内容可跳转至对应 LaTeX 源码，源码定位后可通过右键菜单跳转至 PDF

### 方法二：命令行编译（备用）

```bash

# 一键编译（输出至 build 目录）
latexmk -xelatex -synctex=1 -interaction=nonstopmode -file-line-error -shell-escape -outdir=./build main.tex

# 清理编译临时文件
latexmk -c -outdir=./build main.tex

# 彻底清理（含 PDF 输出）
latexmk -C -outdir=./build main.tex
```

### 方法三：手动分步编译（调试用）

```bash

# 1. 首次编译生成辅助文件
xelatex -synctex=1 -interaction=nonstopmode -file-line-error -shell-escape -output-directory=./build main.tex

# 2. 处理参考文献
biber --output-directory=./build main

# 3. 二次编译更新引用与目录
xelatex -synctex=1 -interaction=nonstopmode -file-line-error -shell-escape -output-directory=./build main.tex

# 4. 三次编译确保所有引用生效
xelatex -synctex=1 -interaction=nonstopmode -file-line-error -shell-escape -output-directory=./build main.tex
```

## 📂 项目结构说明

```plaintext

Math-Notes/
├── main.tex                  # 唯一编译入口：整合章节、配置路径、设置文档结构
├── preamble.tex              # 核心配置文件：宏包引入、自定义环境/命令/样式
├── references.bib            # 参考文献库：适配 GB7714-2015 国标格式
├── chapters/                 # 章节内容目录（按学科模块拆分）
│   ├── 00_preface.tex        # 前言：复习规划、笔记使用说明
│   ├── ch00.tex              # 序言：考研数学整体概述
│   ├── ch01.tex              # 第1章：极限与连续
│   ├── ch02.tex              # 第2章：一元函数微分学
│   ├── ch03.tex              # 第3章：一元函数积分学
│   ├── ch04.tex              # 第4章：无穷级数
│   ├── ch05.tex              # 第5章：多元函数微积分
│   ├── ch06.tex              # 第6章：多元函数积分学
│   ├── ch07.tex              # 第7章：无穷级数（进阶/补充）
│   ├── ch08.tex              # 第8章：微分方程
│   ├── ch09.tex              # 第9章：线性代数
│   ├── ch10.tex              # 第10章：概率论与数理统计
│   └── ch99.tex              # 附录：公式汇总、常用结论、易错点整理
├── figures/                  # 图片资源目录
│   ├── common/               # 通用图片（如公式示意图、框架图）
│   └── 各章节专属图片目录（按需创建）
├── build/                    # 编译输出目录（自动生成）
│   ├── main.pdf              # 最终生成的 PDF 笔记
│   └── 编译过程产生的辅助文件（.aux、.log、.synctex.gz 等）
├── .vscode/
│   └── settings.json         # VS Code 自动化配置：编译规则、预览设置、同步配置
└── README.md                 # 项目说明文档：环境配置、使用指南、结构说明
```

## ✍️ 核心功能与使用规范

### 1. 自定义环境使用（重点）

预设 12 类专用环境，覆盖定理、例题、习题、总结等场景，统一排版风格：

```latex

# 定理类环境（带自动编号，可交叉引用）
\begin{definition}{极限的严格定义}{def:limit-strict}
$\lim_{x\to a}f(x)=L$ 的定义：$\forall \epsilon>0, \exists \delta>0$，当 $0<|x-a|<\delta$ 时，$|f(x)-L|<\epsilon$。
\end{definition}

\begin{theorem}{拉格朗日中值定理}{thm:lagrange}
若函数 $f(x)$ 在 $[a,b]$ 连续、$(a,b)$ 可导，则 $\exists \xi\in(a,b)$，使得 $f(b)-f(a)=f'(\xi)(b-a)$。
\end{theorem}

# 例题与习题环境
\begin{example}
求极限 $\lim_{x\to0}\frac{\sin x}{x}$。
\begin{solution}
由重要极限公式，原式 $=1$。
\end{solution}
\end{example}

\begin{exercise}
求函数 $f(x)=x^3-3x^2+2x$ 的单调区间与极值。
\end{exercise}

# 总结与注意事项
\begin{summary}
本章核心考点：1. 极限的计算方法；2. 连续性的判定；3. 间断点的分类
\end{summary}

\begin{attention}
洛必达法则仅适用于 $\frac{0}{0}$ 或 $\frac{\infty}{\infty}$ 型未定式，使用前需先判定类型！
\end{attention}
```

### 2. 考研专用快捷命令

以下是在 `preamble.tex` 中预设的自定义快捷命令（仅在 LaTeX 编译环境中生效，Markdown 预览仅展示命令定义），覆盖数集、微分、积分、矩阵、考点标记等场景，简化数学符号输入：

|命令分类|自定义快捷命令|作用说明|LaTeX 中使用示例|等价原生 LaTeX 代码（Markdown 可渲染）|最终编译效果描述|
|---|---|---|---|---|---|
|**数集与基础符号**|`\R`|实数集|`$\R$`|`$\mathbb{R}$`|粗体大写 R（实数集符号）|
||`\N`|自然数集|`$\N$`|`$\mathbb{N}$`|粗体大写 N（自然数集符号）|
||`\Z`|整数集|`$\Z$`|`$\mathbb{Z}$`|粗体大写 Z（整数集符号）|
||`\Q`|有理数集|`$\Q$`|`$\mathbb{Q}$`|粗体大写 Q（有理数集符号）|
||`\C`|复数集|`$\C$`|`$\mathbb{C}$`|粗体大写 C（复数集符号）|
||`\P`|概率|`$\P(A)$`|`$\mathbb{P}(A)$`|粗体大写 P（概率符号）|
||`\E`|期望|`$\E(X)$`|`$\mathbb{E}(X)$`|粗体大写 E（期望符号）|
|**微分与导数**|`\ddme`|微分符号（直立体）|`$\ddme x$`|`$\mathrm{d}x$`|直立体 d x（微分符号）|
||`\pd`|偏导符号|`$\pd f/\pd x$`|`$\partial f/\partial x$`|偏导符号 ∂f/∂x|
||`\pder{}{}`|偏导数（带分子分母）|`$\pder{f}{x}$`|`$\frac{\partial f}{\partial x}$`|分式形式的偏导数 ∂f/∂x|
||`\gradme`|梯度|`$\gradme f$`|`$\nabla f$`|梯度符号 ∇f|
||`\diver`|散度|`$\diver \vec{F}$`|`$\operatorname{div} \vec{F}$`|散度符号 div F⃗|
|**极限与积分**|`\limn`|极限（n→∞）|`$\limn a_n$`|`$\lim\limits_{n\to\infty} a_n$`|下标 n→∞ 的极限 limₙ→∞ aₙ|
||`\limx`|极限（x→∞）|`$\limx f(x)$`|`$\lim\limits_{x\to\infty} f(x)$`|下标 x→∞ 的极限 limₓ→∞ f(x)|
||`\limxa`|极限（x→a）|`$\limxa f(x)$`|`$\lim\limits_{x\to a} f(x)$`|下标 x→a 的极限 limₓ→a f(x)|
||`\intab`|定积分（a到b）|`$\intab f(x)\dx$`|`$\int_{a}^{b} f(x)\,\mathrm{d}x$`|下限 a 上限 b 的定积分|
||`\iintD`|二重积分（区域D）|`$\iintD f(x,y)\ddme x\ddme y$`|`$\iint\limits_{D} f(x,y)\mathrm{d}x\mathrm{d}y$`|区域 D 上的二重积分|
||`\ointC`|曲线积分（路径C）|`$\ointC P\ddme x+Q\ddme y$`|`$\oint\limits_{C} P\mathrm{d}x+Q\mathrm{d}y$`|路径 C 上的曲线积分|
||`\dx`|积分微元（x）|`$\int x^2\dx$`|`$\int x^2\,\mathrm{d}x$`|积分微元 dx（带空格）|
||`\dy`|积分微元（y）|`$\int y^2\dy$`|`$\int y^2\,\mathrm{d}y$`|积分微元 dy（带空格）|
|`\dt`|积分微元（t）|`$\int t^2\dt$`|`$\int t^2\,\mathrm{d}t$`|积分微元 dt（带空格）||
|**矩阵与向量**|`\mat{}`|圆括号矩阵|`$\mat{1&2\\3&4}$`|`$\begin{pmatrix} 1&2\\3&4 \end{pmatrix}$`|圆括号包裹的矩阵|
||`\bmat{}`|方括号矩阵|`$\bmat{1&2\\3&4}$`|`$\begin{bmatrix} 1&2\\3&4 \end{bmatrix}$`|方括号包裹的矩阵|
||`\absme{}`|绝对值|`$\absme{x-1}$`|`$\left| x-1 \right|$`|自适应大小的绝对值 |x-1||
||`\normme{}`|范数|`$\normme{\vec{v}}$`|`$\left\| \vec{v} \right\|$`|自适应大小的范数 ‖v⃗‖|
|**概率与统计**|`\Var`|方差|`$\Var(X)$`|`$\operatorname{Var}(X)$`|方差符号 Var(X)|
||`\Cov`|协方差|`$\Cov(X,Y)$`|`$\operatorname{Cov}(X,Y)$`|协方差符号 Cov(X,Y)|
|**快捷输入**|`\const`|常数|`$C=\const$`|`$C=\text{const}$`|英文 const（常数）|
||`\dt`|积分微元（t）|`$\int t^2\dt$`|`$\int t^2\,\mathrm{d}t$`|积分微元 dt（带空格）|
|**考点标记**|`\keypoint{}`|考点标记（红色）|`\keypoint{极限计算}`|`\textbf{\textcolor{kaoyan-red}{【考点】极限计算}}`|红色加粗的【考点】极限计算|
||`\important{}`|重点标记（蓝色）|`\important{中值定理应用}`|`\textbf{\textcolor{kaoyan-blue}{【重点】中值定理应用}}`|蓝色加粗的【重点】中值定理应用|
||`\difficulty{}`|难度标记（橙色）|`\difficulty{三重积分计算}`|`\textbf{\textcolor{kaoyan-orange}{【难度】三重积分计算}}`|橙色加粗的【难度】三重积分计算|
||`\formula{}`|公式突出（蓝色）|`\formula{\lim_{x\to0}\frac{\sin x}{x}=1}`|`\textcolor{kaoyan-blue}{$\lim_{x\to0}\frac{\sin x}{x}=1$}`|蓝色高亮的公式块|
### 关键说明

1. **生效范围**：上述自定义命令仅在 LaTeX 编译环境中生效（.tex 文件），Markdown 预览无法识别，因此表格中补充了「等价原生 LaTeX 代码」，可直接在 Markdown 中渲染；

2. **使用方式**：在 .tex 文件中直接写自定义命令（如 `$\pder{f}{x}$`）即可，无需写冗长的原生代码；

3. **颜色依赖**：考点标记类命令依赖 `preamble.tex` 中定义的颜色（`kaoyan-red`/`kaoyan-blue` 等），需确保颜色定义已提前配置；

4. **编译验证**：所有命令已在 XeLaTeX 环境中验证，可正常编译输出，无语法错误。

### 3. 章节写作规范

- 每章一个独立 .tex 文件，存放于 `chapters/` 目录，命名格式：`chXX.tex`（如 `ch01.tex`）

- 章节文件开头需添加 `%!TEX root = ../main.tex`，确保单独编译时能正确定位根文件

- 使用预设环境与快捷命令，保持全文档格式一致性（如定理编号、公式样式、考点标记）

- 图片存放于 `figures/` 目录，按章节分类管理，引用时直接使用文件名（路径已在 `main.tex` 中配置）

## 🔧 个性化配置指南

所有自定义配置集中在`preamble.tex` 中，可根据个人需求修改：

### 1. 颜色方案修改

考研专用颜色已预设，可调整 RGB 值自定义：

```latex

% 原预设颜色（位于 preamble.tex 第四部分）
\definecolor{kaoyan-blue}{RGB}{0, 102, 204}    % 主色调蓝色（章节标题、重点）
\definecolor{kaoyan-red}{RGB}{204, 51, 0}      % 重点红色（考点标记）
\definecolor{kaoyan-green}{RGB}{0, 153, 0}     % 正确/答案绿色
\definecolor{kaoyan-orange}{RGB}{255, 153, 0}  % 警告/注意橙色
\definecolor{kaoyan-gray}{RGB}{245, 245, 245}  % 背景灰色
```

### 2. 页面样式调整

修改页眉页脚、章节格式等（位于 `preamble.tex` 第十一部分）：

```latex

% 页眉页脚修改示例（调整显示内容）
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{考研数学笔记}  % 左侧页眉显示固定文本
\fancyhead[R]{\thechapter.\thesection}  % 右侧页眉显示章节号
\fancyfoot[C]{\thepage}  % 页脚显示页码

% 章节标题格式修改示例（调整字号与颜色）
\titleformat{\chapter}[display]
    {\normalfont\huge\bfseries\color{kaoyan-red}}  % 改为红色标题
    {\chaptertitlename\ \thechapter}{20pt}{\Huge}
```

### 3. 新增自定义环境

在 `preamble.tex` 第九部分添加新环境，示例：

```latex

% 新增「方法归纳」环境
\newtcolorbox{method}{
    colframe=kaoyan-green!70!black,
    colback=kaoyan-green!5,
    title=方法归纳,
    fonttitle=\bfseries,
    breakable
}
```

### 4. VS Code 配置调整

修改 `.vscode/settings.json` 可调整编译规则、预览方式等：

- 关闭自动编译：将 `latex-workshop.latex.autoBuild.run` 改为 `"never"`

- 更换 PDF 查看器：将 `latex-workshop.view.pdf.viewer` 改为 `"external"`，并配置外部查看器路径

- 调整输出目录：修改 `latex-workshop.latex.outDir` 为自定义路径（如 `./output`）

## ⚙️ VS Code 完整配置文件（.vscode/settings.json）

项目预设的 `.vscode/settings.json` 包含编译、预览、同步等全量配置，可直接复制使用，无需手动修改：

```json

{
    // ============ LaTeX Workshop 核心配置 ============
    "latex-workshop.latex.tools": [
        {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
                "-xelatex",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-shell-escape",
                "-outdir=./build",
                "%DOC%"
            ]
        }
    ],
    
    "latex-workshop.latex.recipes": [
        {
            "name": "latexmk",
            "tools": ["latexmk"]
        }
    ],
    
    "latex-workshop.latex.autoBuild.run": "onSave",
    "latex-workshop.latex.clean.fileTypes": [
        "*.aux", "*.bbl", "*.blg", "*.bcf", "*.run.xml",
        "*.synctex.gz", "*.log", "*.out", "*.toc",
        "*.lof", "*.lot", "*.fmt", "*.fot", "*.fdb_latexmk", "*.fls"
    ],
    
    // LaTeX PDF 预览与同步配置
    "latex-workshop.view.pdf.viewer": "tab",  // 使用内置查看器
    "latex-workshop.view.pdf.internal.synctex.keybinding": "double-click",
    "latex-workshop.view.pdf.internal.click": true,
    "latex-workshop.view.pdf.internal.dblclick": true,
    "latex-workshop.view.pdf.internal.ctrlclick": false,
    
    "latex-workshop.synctex.afterBuild.enabled": true,
    "latex-workshop.synctex.path": "synctex",
    "latex-workshop.latex.outDir": "./build",
    
    // LaTeX 性能优化
    "latex-workshop.latex.watch.files.ignore": [
        "**/build/**",
        "**/.git/**"
    ],

    // ============ Markdown All in One 配置 ============
    // 开启代码块复制按钮（核心配置）
    "markdown.extension.copy.codeButton.enabled": true,
    // 可选：设置复制按钮显示位置（top-right/top-left/bottom-right/bottom-left）
    "markdown.extension.copy.codeButton.position": "top-right",
    // 可选：复制按钮显示图标（默认 clipboard，也可设为 text 显示「复制」文字）
    "markdown.extension.copy.codeButton.iconStyle": "clipboard"
}
```

### 配置核心说明

1. **编译规则**：指定 `latexmk` 作为编译工具，使用 XeLaTeX 引擎，自动处理中文、同步文件和临时文件清理

2. **自动编译**：保存 .tex 文件时触发编译，无需手动执行命令

3. **PDF 预览**：使用 VS Code 内置标签页预览，双击实现 PDF 与源码双向跳转

4. **输出管理**：所有编译产物（PDF + 临时文件）统一放入 `./build` 目录，保持项目根目录整洁

5. **性能优化**：忽略 `build/` 和 `.git/` 目录的文件监听，减少 VS Code 资源占用

6. **Markdown 配置**：开启代码块复制功能，默认右上角显示剪贴板图标，点击即可复制代码

## 📋 核心技术细节

### 1. 核心宏包依赖

所有宏包已在 `preamble.tex` 中集中引入，按功能分类：

|功能模块|核心宏包|作用说明|
|---|---|---|
|中文支持|ctex、fontspec|实现中英混排，适配系统字体|
|数学公式|amsmath、amsthm、mathtools、bm、physics|提供专业数学符号、公式环境、粗体符号等|
|排版工具|geometry、fancyhdr、titlesec、booktabs、enumitem|控制页面布局、页眉页脚、标题样式、表格与列表格式|
|图形与颜色|graphicx、tcolorbox、tikz、xcolor|支持图片插入、彩色框环境、绘图、颜色定义|
|引用与文献|hyperref、cleveref、biblatex|实现超链接、智能引用、国标参考文献格式|
### 2. 文档结构参数

- 文档类：`book` 类，10pt 字号，单面排版（`oneside`）

- 页面尺寸：A4 纸，页边距 2.5cm（上下左右统一）

- 编号规则：公式、图片、表格编号带章节号（如 1-1 表示第1章第1图）

- 超链接：颜色链接启用，链接色为考研蓝，引用色为考研绿

## 🔍 常见问题排查

|问题现象|常见原因|解决方案|
|---|---|---|
|中文乱码或编译失败|未使用 XeLaTeX 编译，或文件编码非 UTF-8|确保编译引擎为 XeLaTeX，文件编码设为 UTF-8（VS Code 右下角可查看/修改）|
|编译无输出，提示缺少宏包|TeX 发行版未安装对应宏包|MiKTeX 会自动弹出安装提示，点击安装；TeX Live 需通过 tlmgr 安装（如 `tlmgr install tcolorbox`）|
|参考文献未显示或引用错误|未执行 biber 步骤，或参考文献格式错误|执行完整编译链（XeLaTeX → biber → XeLaTeX ×2），检查 `references.bib` 格式是否符合 GB7714-2015|
|图片无法加载|图片路径错误，或格式不支持|确保图片存放于 `figures/` 目录，引用时使用正确文件名，优先使用 PDF/PNG 格式|
|双向同步失效|编译时未启用 synctex，或查看器配置错误|确保编译参数包含 `-synctex=1`，VS Code 中开启 `latex-workshop.synctex.afterBuild.enabled`|
|代码块无复制功能|1. 未使用支持复制功能的 Markdown 预览插件；2. 插件未开启复制按钮功能；3. 预览模式未正确加载|1. 安装插件：在 VS Code 扩展面板搜索安装「Markdown All in One」或「Markdown Preview Enhanced」（二选一即可）；2. 开启复制功能（Markdown All in One 详细步骤）：① 打开 VS Code 左侧「扩展」面板（快捷键 Ctrl+Shift+X）；② 在已安装插件列表中找到「Markdown All in One」，点击插件右下角的「齿轮图标」，选择「扩展设置」；③ 在设置页面搜索框输入「Markdown All in One: Enable Copy Code Button」，找到对应设置项并勾选（勾选后代码块预览时会自动显示复制按钮）；3. 若用「Markdown Preview Enhanced」：默认自带复制功能，无需额外配置，重启预览即可；4. 重新加载预览：关闭当前预览，按 `Ctrl+Shift+V` 重新打开，确保预览窗口正常渲染，此时代码块右上角会显示「复制」按钮，点击即可复制代码内容|
## 🎯 适用场景

- 考研数学复习：系统梳理知识点，标记核心考点，构建知识框架

- 习题整理：使用例题/习题/解答环境，分类整理典型例题与真题

- 考前冲刺：通过附录汇总公式与易错点，便于快速复盘

- LaTeX 学习：作为中文数学 LaTeX 排版的实战案例，涵盖宏包使用、环境自定义、自动化编译等核心知识点

## 📄 说明

本项目为个人学习整理笔记，仅供考研复习参考使用，禁止商用。

版本信息：v2025.1（适配 2025 考研数学大纲）

作者：张庭祥

> （注：文档部分内容可能由 AI 生成）
> 
> 
> （注：文档部分内容可能由 AI 生成）