#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 快手
import sys as oSys
import base as oUtils
import random as osRandom # 随机数

#宝箱坐标：eggX,eggY
def eatBox(eggX,eggY):
    oUtils.setSleep(2)
    #点击宝箱
    eggX = oUtils.getRandom(eggX-5, eggX+5)
    eggY = oUtils.getRandom(eggY-5, eggY+5)
    
    print('>>> 执行点击宝箱操作,坐标: (%d,%d) ' %(eggX, eggY))
    oUtils.tap(eggX,eggY)

    #等待动画
    oUtils.setSleep(3)

#视频广告坐标：adX,adY,  needBack:是否结束时返回上级页面 0:NO, >0 YES
def eatAD(adX,adY,needBack):

    oUtils.setSleep(1)
    #看广告,点击位置
    adX = oUtils.getRandom(adX-5, adX+5)
    adY = oUtils.getRandom(adY-5, adY+5)

    print('>>> 执行点击观看广告操作,坐标: (%d,%d) ' %(adX, adY))
    oUtils.tap(adX,adY)


    #等待广告看完
    print('>>> 等待广告看完')
    oUtils.setSleep(22)

    #循环8次后将会提示需要再次查看广告
    #TODO  待处理

    #返回到上级页面
    if needBack:
        oUtils.backKey()
    
    #等待动画完成
    oUtils.setSleep(2)

    print('>>> 完成点击宝箱操作')
    return