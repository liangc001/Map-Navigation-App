# 贡献指南

感谢您对 Map Navigation App 项目的关注！我们欢迎并感谢您为项目做出贡献。

## 如何贡献

### 报告问题

如果您发现了 bug 或有功能建议，请通过 GitHub Issues 报告：

1. 检查是否已存在相关 issue
2. 创建新 issue 时请提供详细信息：
   - 问题描述
   - 复现步骤
   - 期望行为
   - 实际行为
   - 系统环境（操作系统、Python 版本等）
   - 截图（如适用）

### 提交代码

1. **Fork 仓库**
   ```bash
   git clone https://github.com/liangc001/Map-Navigation-App.git
   cd Map-Navigation-App
   ```

2. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **进行修改**
   - 遵循 PEP 8 代码规范
   - 添加适当的注释和文档
   - 确保代码可以正常运行

4. **提交更改**
   ```bash
   git add .
   git commit -m "feat: 添加新功能描述"
   ```

5. **推送到您的 Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **创建 Pull Request**
   - 描述您的更改
   - 关联相关 issue
   - 等待审核

## 代码规范

### Python 代码风格

- 遵循 [PEP 8](https://pep8.org/) 规范
- 使用 4 个空格缩进
- 最大行长度 100 字符
- 使用有意义的变量名

### 提交信息格式

使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

- `feat:` 新功能
- `fix:` 修复 bug
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建/工具相关

示例：
```
feat: 添加路径规划算法的可视化功能
fix: 修复登录时的数据库连接错误
docs: 更新 API 文档
```

## 开发环境设置

1. 创建虚拟环境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或 venv\Scripts\activate  # Windows
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 运行应用：
   ```bash
   python map.py
   ```

## 测试

- 在提交前确保应用可以正常启动
- 测试主要功能：登录、导航、路径规划
- 检查是否有明显的 UI 问题

## 许可证

通过提交代码，您同意您的贡献将在 MIT 许可证下发布。

## 联系我们

如有问题，请通过 GitHub Issues 联系。

感谢您的贡献！
