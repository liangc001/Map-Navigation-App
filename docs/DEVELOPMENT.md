# 开发指南

本文档面向项目开发者。

## 开发环境

### 推荐工具

- **IDE**: PyCharm, VS Code
- **Python**: 3.8+
- **版本控制**: Git
- **虚拟环境**: venv, conda

### VS Code 配置

创建 `.vscode/settings.json`：

```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true,
        "**/.venv": true
    }
}
```

### PyCharm 配置

1. File → Settings → Project → Python Interpreter
2. 添加虚拟环境
3. 配置代码检查：Editor → Inspections

## 代码规范

### Python 规范

- 遵循 PEP 8
- 使用类型注解
- 编写文档字符串

示例：

```python
def calculate_distance(start: str, end: str) -> float:
    """
    计算两点之间的距离。

    Args:
        start: 起点名称
        end: 终点名称

    Returns:
        距离值（公里）

    Raises:
        ValueError: 当节点不存在时
    """
    pass
```

### Git 提交规范

```
<type>(<scope>): <subject>

<body>

<footer>
```

类型：
- `feat`: 新功能
- `fix`: 修复
- `docs`: 文档
- `style`: 格式
- `refactor`: 重构
- `test`: 测试
- `chore`: 构建

## 模块开发

### 添加新功能

1. 在适当模块中实现功能
2. 添加单元测试
3. 更新文档
4. 提交代码

### 添加新算法

1. 在 `dis33.py` 中实现
2. 继承 `Graph` 类或添加新方法
3. 添加性能测试
4. 在 UI 中添加选项

### UI 开发

使用 Qt Designer：

```bash
pip install pyqt5-tools
pyqt5-tools designer  # 启动设计器
```

转换 UI 文件：

```bash
pyuic5 -x main.ui -o main_ui.py
```

## 调试

### 日志

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("调试信息")
logger.info("一般信息")
logger.warning("警告")
logger.error("错误")
```

### 调试器

使用 pdb：

```python
import pdb
pdb.set_trace()
```

或使用 IDE 的调试功能。

## 性能优化

### Profiling

```python
import cProfile
import pstats

cProfile.run('function_to_profile()', 'output.prof')
p = pstats.Stats('output.prof')
p.sort_stats('cumulative').print_stats(10)
```

### 内存分析

```python
from memory_profiler import profile

@profile
def my_function():
    pass
```

## 发布流程

1. 更新版本号
2. 更新 CHANGELOG.md
3. 创建 Git 标签
4. 构建分发包
5. 上传到 PyPI（如适用）

```bash
# 创建标签
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin v1.0.0

# 构建
python -m build

# 上传（可选）
python -m twine upload dist/*
```

## 持续集成

查看 `.github/workflows/ci.yml` 了解 CI 配置。

## 代码审查

### 审查清单

- [ ] 代码符合规范
- [ ] 有适当的注释
- [ ] 包含测试
- [ ] 文档已更新
- [ ] 没有安全漏洞
- [ ] 性能可接受

## 资源

- [PyQt5 文档](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [Python 文档](https://docs.python.org/zh-cn/3/)
- [SQLite 文档](https://www.sqlite.org/docs.html)
