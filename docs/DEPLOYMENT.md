# 部署指南

本文档介绍如何部署 Map Navigation App。

## 本地部署

### 方法一：直接运行

1. 确保已安装 Python 3.8+
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行应用：
   ```bash
   python map.py
   ```

### 方法二：使用虚拟环境

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 运行应用
python map.py
```

## 打包为可执行文件

### 使用 PyInstaller

1. 安装 PyInstaller：
   ```bash
   pip install pyinstaller
   ```

2. 创建 spec 文件：
   ```bash
   pyinstaller --name="MapNavigation" \
               --windowed \
               --icon=picture/maps.ico \
               --add-data "picture:picture" \
               map.py
   ```

3. 构建可执行文件：
   ```bash
   pyinstaller MapNavigation.spec
   ```

4. 输出在 `dist/` 目录

### 使用 cx_Freeze

```bash
pip install cx_Freeze
python setup.py build
```

## 分发

### 创建安装包

#### Windows

使用 Inno Setup 或 NSIS 创建安装程序。

#### macOS

```bash
# 创建应用包
pyinstaller --windowed --onefile map.py

# 创建 dmg
create-dmg dist/MapNavigation.app
```

#### Linux

```bash
# 创建 deb 包
dpkg-deb --build package/

# 或使用 AppImage
```

## Docker 部署（可选）

### Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "map.py"]
```

### 构建镜像

```bash
docker build -t map-navigation-app .
```

### 运行容器

```bash
docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY map-navigation-app
```

## 配置

### 环境变量

| 变量名 | 描述 | 默认值 |
|--------|------|--------|
| `MAP_DB_PATH` | 数据库路径 | `user_mes.db` |
| `MAP_DEBUG` | 调试模式 | `False` |
| `MAP_THEME` | UI 主题 | `default` |

### 配置文件

可以创建 `config.ini` 文件：

```ini
[database]
path = user_mes.db

[ui]
theme = default
language = zh_CN

[map]
default_zoom = 1.0
```

## 故障排除

### 数据库锁定

如果遇到数据库锁定错误：

```bash
# 检查是否有其他进程占用
lsof user_mes.db

# 杀死占用进程
kill -9 <PID>
```

### UI 显示问题

```bash
# 设置环境变量
export QT_QPA_PLATFORM=xcb  # Linux
# 或
export QT_QPA_PLATFORM=cocoa  # macOS
```

## 更新

### 备份数据

在更新前备份数据库：

```bash
cp user_mes.db user_mes.db.backup
```

### 更新步骤

1. 拉取最新代码：
   ```bash
   git pull origin main
   ```

2. 更新依赖：
   ```bash
   pip install -r requirements.txt --upgrade
   ```

3. 运行测试：
   ```bash
   make test
   ```

4. 启动应用
