"""
测试套件

运行测试：
    python -m pytest tests/ -v
    或
    python tests/test_app.py
"""

import unittest
import sys
import os
import sqlite3

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database_option import (
    check_user_name, search_user_pass, save_data_user,
    save_data_road_user, read_manager_road, create_table
)
from dis33 import read_node, Floyd, query_path


class TestDatabase(unittest.TestCase):
    """数据库模块测试"""

    def setUp(self):
        """测试前准备"""
        # 使用内存数据库进行测试
        self.test_db = ":memory:"
        # 临时修改数据库路径
        import database_option
        self.original_dbpath = database_option.sqlite3.connect
        self.conn = sqlite3.connect(self.test_db)
        self.cur = self.conn.cursor()

        # 创建测试表
        self.cur.execute('''
            create table if not exists user_mes(
                id varchar(255),
                key_ varchar(255)
            );
        ''')
        self.cur.execute('''
            create table if not exists mes_road_manager(
                begin_ varchar(255),
                end_ varchar(255),
                direction varchar(255),
                distance int
            );
        ''')
        self.conn.commit()

    def tearDown(self):
        """测试后清理"""
        self.conn.close()

    def test_check_user_name(self):
        """测试用户名存在性检查"""
        # 先插入测试用户
        self.cur.execute("INSERT INTO user_mes (id, key_) VALUES ('test_user', 'test_pass')")
        self.conn.commit()

        # 检查存在的用户
        result = check_user_name("test_user")
        self.assertEqual(result, 1)

        # 检查不存在的用户
        result = check_user_name("non_exist_user")
        self.assertEqual(result, 0)

    def test_save_data_user(self):
        """测试用户注册"""
        # 测试新用户注册
        result = save_data_user("new_user", "new_pass")
        self.assertEqual(result, None)  # 成功时返回 None

        # 测试重复用户注册
        save_data_user("duplicate_user", "pass123")
        result = save_data_user("duplicate_user", "pass456")
        self.assertEqual(result, 0)  # 用户已存在返回 0


class TestGraph(unittest.TestCase):
    """图算法模块测试"""

    def setUp(self):
        """测试前准备"""
        # 构建测试数据
        # 清真食堂 --300m(西)--> 基础学院大门
        # 清真食堂 --50m(南)--> 清真食堂南侧路口
        self.test_data = [
            ('清真食堂', '基础学院大门', '西', 300),
            ('基础学院大门', '清真食堂', '东', 300),
            ('清真食堂', '清真食堂南侧路口', '南', 50),
            ('清真食堂南侧路口', '清真食堂', '北', 50),
            ('清真食堂', '操场', '北', 200),
            ('操场', '清真食堂', '南', 200),
            ('申一教', '基础学院大门', '西', 100),
            ('基础学院大门', '申一教', '东', 100)
        ]

    def test_read_node(self):
        """测试读取节点信息"""
        loc, cnt = read_node(self.test_data)
        # 应该识别出所有唯一的节点
        self.assertIsInstance(loc, dict)
        self.assertIsInstance(cnt, int)
        self.assertGreater(cnt, 0)
        # 检查特定节点是否存在
        self.assertIn('清真食堂', loc.values())
        self.assertIn('基础学院大门', loc.values())

    def test_query_path(self):
        """测试路径查询"""
        result = query_path(self.test_data, '清真食堂', '基础学院大门')
        # 结果应该是一个列表
        self.assertIsInstance(result, list)
        # 应该有路径信息
        self.assertGreater(len(result), 0)
        # 最后一条应该是总距离
        self.assertIn('米', result[-1])

    def test_query_same_point(self):
        """测试相同起终点的路径查询"""
        result = query_path(self.test_data, '清真食堂', '清真食堂')
        self.assertIsInstance(result, list)
        # 相同点应该返回0距离
        self.assertIn('0米', result[-1])


class TestIntegration(unittest.TestCase):
    """集成测试"""

    def test_full_workflow(self):
        """测试完整工作流程"""
        # 1. 创建数据库表
        create_table()

        # 2. 注册用户
        save_data_user("integration_user", "integration_pass")

        # 3. 检查用户存在
        exists = check_user_name("integration_user")
        self.assertEqual(exists, 1)

        # 4. 查询路径
        test_data = [
            ('A', 'B', '东', 100),
            ('B', 'C', '南', 200),
            ('A', 'C', '东南', 300)
        ]
        result = query_path(test_data, 'A', 'C')
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)


def run_tests():
    """运行所有测试"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestDatabase))
    suite.addTests(loader.loadTestsFromTestCase(TestGraph))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
