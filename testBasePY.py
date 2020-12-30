#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import base as oUtils
import unittest

class MyclassTest(unittest.TestCase):
    def setUp(self) -> None:
        '''
        测试之前的准备工作
        :return:
        '''
        

    def tearDown(self) -> None:
        '''
        测试之后的收尾
        如关闭数据库
        :return:
        '''
        pass

    def test_add(self):
        ret = 9
        self.assertEqual(ret,9)  

    def test_sub(self):
        ret = 1
        self.assertEqual(ret,-1)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_add'))
    suite.addTest(MyclassTest('test_sub'))

    runner = unittest.TextTestRunner()
    runner.run(suite)