.PHONY: help install run clean test lint format build dist

help:
	@echo "Map Navigation App - 可用的命令:"
	@echo "  make install    安装依赖"
	@echo "  make run        运行应用"
	@echo "  make test       运行测试"
	@echo "  make clean      清理临时文件"
	@echo "  make build      构建应用"
	@echo "  make lint       代码检查"
	@echo "  make format     代码格式化"

install:
	pip install -r requirements.txt

run:
	python map.py

test:
	@echo "运行测试..."
	python -m pytest tests/ -v || echo "测试目录不存在，请先创建测试"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	rm -rf build/ dist/ *.egg-info/ 2>/dev/null || true
	@echo "清理完成"

build:
	python setup.py build

dist:
	python setup.py sdist bdist_wheel

lint:
	@which flake8 > /dev/null 2>&1 && flake8 . --max-line-length=100 || echo "请先安装 flake8: pip install flake8"

format:
	@which black > /dev/null 2>&1 && black . || echo "请先安装 black: pip install black"

setup:
	python -m venv venv
	@echo "虚拟环境已创建，请激活后运行: make install"
