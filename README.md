# 大模型技术栈思维导图

这是一个交互式的思维导图项目，用于展示大模型（LLM）相关的技术栈，包括基础技术体系、RAG、LangChain、AI Agent 等内容。

## 特性

- 📊 交互式思维导图展示
- 🔍 实时搜索功能
- 📱 响应式设计，支持移动端
- 🎨 优雅的视觉效果
- 🔗 丰富的外部资源链接

## 在线预览

访问 [https://[your-username].github.io/llm-mindmap/](https://[your-username].github.io/llm-mindmap/) 查看在线演示。

## 本地运行

1. 克隆仓库：
```bash
git clone https://github.com/[your-username]/llm-mindmap.git
```

2. 进入项目目录：
```bash
cd llm-mindmap
```

3. 使用任意 HTTP 服务器运行，例如 Python 的 `http.server`：
```bash
python3 -m http.server
```

4. 在浏览器中访问 `http://localhost:8000`

## 技术栈

- HTML5
- CSS3
- JavaScript
- D3.js
- Markmap

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

# 游戏说明

## 运行要求
- Python 3.x
- 现代浏览器（Chrome、Firefox、Safari等）

## 如何运行
1. 确保已安装Python 3
2. 打开终端，进入游戏目录
3. 运行以下命令启动服务器：
   ```bash
   chmod +x start_server.sh
   ./start_server.sh
   ```
4. 在浏览器中访问：http://localhost:8000

## 游戏控制
- 鼠标移动：控制核心位置
- 空格键：激活护盾
- F键：冻结投射物
- D键：双倍分数
- I键：无敌模式
- ESC键：返回主菜单

## 游戏模式
- 简单模式：单个核心，基础速度
- 中等模式：两个核心，速度提升20%
- 困难模式：三个核心，速度提升50%

## 故障排除
如果遇到问题：
1. 确保端口8000未被占用
2. 检查浏览器控制台是否有错误信息
3. 尝试清除浏览器缓存
4. 确保所有文件都在同一目录下

# 核心防御游戏

一个基于HTML5和JavaScript的防御类游戏。

## 游戏特点

- 三种难度模式：简单、中等、困难
- 实时分数统计
- 最高分排行榜
- 多种道具系统
- 动态难度调整

## 游戏规则

1. 使用鼠标控制核心移动
2. 躲避红色投射物（扣分）
3. 收集其他颜色的投射物（得分）
4. 使用道具增强防御能力：
   - 空格键：护盾
   - F键：冻结
   - D键：双倍分数
   - I键：无敌

## 技术栈

- HTML5
- CSS3
- JavaScript
- Canvas API

## 如何运行

1. 克隆仓库
```bash
git clone https://github.com/yourusername/BallGame.git
```

2. 打开index.html开始游戏

## 文件结构

- `Start.html`: 游戏开始页面
- `Playing.html`: 游戏主页面
- `Gameover.html`: 游戏结算页面
- `Help.html`: 游戏帮助页面
- `BG.png`: 游戏背景图片

## 贡献

欢迎提交Issue和Pull Request！

## 许可证

MIT License 