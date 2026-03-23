# API 文档

本文档详细介绍 Map Navigation App 的 API 和模块功能。

## 目录

- [map.py](#mappy) - 主应用模块
- [database_option.py](#database_optionpy) - 数据库操作
- [dis33.py](#dis33py) - 路径算法
- [Mainwce.py](#mainwcepy) - UI 组件

---

## map.py

主应用程序入口，包含主窗口和用户界面。

### 类：Ui_MainWindow

主窗口类，继承自 `QtWidgets.QMainWindow`。

#### 方法

**__init__()**
- 初始化主窗口
- 设置 UI 和窗口属性

**setupUi(KevaCoin)**
- 设置主窗口 UI
- 参数：
  - `KevaCoin`: 主窗口对象

**retranslateUi(KevaCoin)**
- 设置界面文本和翻译
- 参数：
  - `KevaCoin`: 主窗口对象

---

## database_option.py

数据库操作模块，处理 SQLite 数据库连接和用户数据。

### 类：Database

数据库操作类。

#### 方法

**__init__(db_name)**
- 初始化数据库连接
- 参数：
  - `db_name`: 数据库文件名

**create_table()**
- 创建用户表
- 表结构：
  - `id`: TEXT PRIMARY KEY
  - `password`: TEXT

**insert_user(user_id, password)**
- 插入新用户
- 参数：
  - `user_id`: 用户ID
  - `password`: 密码

**check_user(user_id, password)**
- 验证用户登录
- 参数：
  - `user_id`: 用户ID
  - `password`: 密码
- 返回：Boolean

**user_exists(user_id)**
- 检查用户是否存在
- 参数：
  - `user_id`: 用户ID
- 返回：Boolean

---

## dis33.py

路径查找算法模块，实现最短路径计算。

### 类：Graph

图类，用于表示地图节点和边。

#### 方法

**__init__()**
- 初始化图结构

**add_node(node)**
- 添加节点
- 参数：
  - `node`: 节点名称

**add_edge(from_node, to_node, weight)**
- 添加边
- 参数：
  - `from_node`: 起始节点
  - `to_node`: 目标节点
  - `weight`: 权重（距离）

**dijkstra(start, end)**
- Dijkstra 最短路径算法
- 参数：
  - `start`: 起始节点
  - `end`: 目标节点
- 返回：(path, distance) 元组

**floyd_warshall()**
- Floyd-Warshall 全源最短路径算法
- 返回：距离矩阵和前驱矩阵

---

## Mainwce.py

额外的 UI 组件模块。

### 说明

包含辅助的 UI 组件和对话框类，用于扩展主界面功能。

---

## 数据流

```
用户操作 -> UI (map.py) -> 业务逻辑 -> 数据库/算法
                ^                           |
                |                           v
                +-------- 结果显示 <--------+
```

## 错误处理

### 数据库错误
- 连接失败时显示错误对话框
- 用户不存在时提示注册

### 路径计算错误
- 节点不存在时返回空路径
- 不可达时返回 None

### UI 错误
- 输入验证失败时显示提示
- 异常捕获并记录

---

## 配置

### 数据库配置
- 文件名：`user_mes.db`
- 类型：SQLite3
- 位置：应用根目录

### UI 配置
- 窗口大小：1196x796
- 背景图片：`./picture/R-C.jpg`
- 图标：`./picture/maps.ico`
