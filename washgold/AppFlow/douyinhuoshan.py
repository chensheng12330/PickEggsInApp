#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 抖音火山
import sys as oSys
import base as oUtils
from app_list import oAppMoveList
from element import Element

oEmt = Element() # 初始化工具

iDefMin = 5
iDefMax = 10
iVideoTime = 30
sDefApp = oAppMoveList['douyinhuoshan']

oUtils.callApp(sDefApp)
oUtils.setSleep(20)

