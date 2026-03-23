# Map Navigation Application

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)](https://riverbankcomputing.com/software/pyqt/)
[![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg)](https://www.sqlite.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A PyQt5-based map navigation application with user management, path finding, and graphical interface.

[English](#english) | [中文](#中文)

---

## 中文

### 功能特性

- **用户认证**：使用 SQLite 数据库的登录和注册系统
- **地图显示**：自定义背景的视觉地图界面
- **路径规划**：地点间的最短路径计算
- **交互式界面**：使用 PyQt5 的用户友好图形界面
- **数据存储**：用户信息存储在 SQLite 数据库中

### 项目结构

```
.
├── map.py                      # 主应用入口
├── Mainwce.py                  # 附加 UI 组件
├── database_option.py          # 数据库操作 (SQLite)
├── dis33.py                    # 路径查找算法
├── picture/                    # 图片资源
├── docs/                       # 文档目录
│   ├── API.md                  # API 文档
│   ├── ARCHITECTURE.md         # 架构设计
│   ├── USER_GUIDE.md           # 用户指南
│   ├── DEVELOPMENT.md          # 开发指南
│   └── DEPLOYMENT.md           # 部署指南
├── tests/                      # 测试目录
├── .github/                    # GitHub 配置
│   ├── workflows/              # CI/CD 工作流
│   └── ISSUE_TEMPLATE/         # Issue 模板
├── requirements.txt            # Python 依赖
├── setup.py                    # 安装配置
├── pyproject.toml              # 现代构建配置
├── Makefile                    # 构建脚本
├── CONTRIBUTING.md             # 贡献指南
├── CHANGELOG.md                # 更新日志
├── LICENSE                     # 许可证
└── README.md                   # 本文件
```

### 快速开始

#### 环境要求

- Python 3.8+
- PyQt5
- SQLite3

#### 安装

```bash
# 克隆仓库
git clone https://github.com/liangc001/Map-Navigation-App.git
cd Map-Navigation-App

# 安装依赖
pip install -r requirements.txt

# 或使用 Make
make install
```

#### 运行

```bash
python map.py
# 或
make run
```

### 文档

- [用户指南](docs/USER_GUIDE.md) - 详细使用说明
- [API 文档](docs/API.md) - 接口说明
- [架构设计](docs/ARCHITECTURE.md) - 系统设计
- [开发指南](docs/DEVELOPMENT.md) - 开发者文档
- [部署指南](docs/DEPLOYMENT.md) - 部署说明

### 技术细节

#### 数据库架构

SQLite 数据库包含以下表：
- `user_mes`: 用户登录信息 (id, password)

#### 路径算法

`dis33.py` 模块实现了最短路径算法：
- Floyd-Warshall 全源最短路径算法
- Dijkstra 单源最短路径算法

#### UI 组件

- **主窗口**: 带地图显示的主应用窗口
- **登录对话框**: 用户认证界面
- **路径搜索**: 起点和终点输入
- **结果显示**: 显示计算的路径和距离

### 贡献

欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与。

### 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解版本历史。

### 许可证

本项目使用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

---

## English

### Features

- **User Authentication**: Login and registration system with SQLite database
- **Map Display**: Visual map interface with custom backgrounds
- **Path Finding**: Shortest path calculation between locations
- **Interactive UI**: User-friendly graphical interface with PyQt5
- **Database Storage**: User information stored in SQLite database

### Quick Start

#### Requirements

- Python 3.8+
- PyQt5
- SQLite3

#### Installation

```bash
# Clone repository
git clone https://github.com/liangc001/Map-Navigation-App.git
cd Map-Navigation-App

# Install dependencies
pip install -r requirements.txt

# Or use Make
make install
```

#### Run

```bash
python map.py
# or
make run
```

### Documentation

- [User Guide](docs/USER_GUIDE.md) - Detailed usage instructions
- [API Documentation](docs/API.md) - API reference
- [Architecture](docs/ARCHITECTURE.md) - System design
- [Development Guide](docs/DEVELOPMENT.md) - Developer documentation
- [Deployment Guide](docs/DEPLOYMENT.md) - Deployment instructions

### Technical Details

#### Database Schema

SQLite database with the following tables:
- `user_mes`: User login information (id, password)

#### Path Algorithms

The `dis33.py` module implements:
- Floyd-Warshall all-pairs shortest paths
- Dijkstra single-source shortest paths

### Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

### License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

---

## Screenshots

*(Screenshots to be added)*

## Roadmap

- [x] Basic user authentication
- [x] Path finding algorithms
- [x] GUI with PyQt5
- [ ] Add more map locations
- [ ] Real map integration (OpenStreetMap)
- [ ] Route visualization
- [ ] Multiple transportation modes
- [ ] Save favorite routes
- [ ] Mobile support

## Acknowledgments

- PyQt5 Documentation
- SQLite Documentation
- Algorithm references for shortest path calculation

---

**Note**: This is a learning project created for educational purposes. The map data is simulated and not based on real geographic information.
