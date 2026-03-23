#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="map-navigation-app",
    version="1.0.0",
    author="liangc001",
    author_email="",
    description="A PyQt5-based map navigation application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liangc001/Map-Navigation-App",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "map-nav=map:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.png", "*.jpg", "*.ico", "*.db"],
    },
)
