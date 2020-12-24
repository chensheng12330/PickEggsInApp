#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 淘宝直播操作流程
import sys as oSys
import base as oUtils
import random as osRandom # 随机数


#金币页面彩蛋坐标：coEggX,coEggY
def eatColEggs(coEggX,coEggY):
    #等待界面稳定
    oUtils.setSleep(2)

    #点击彩蛋
    adX = oUtils.getRandom(coEggX-5, coEggX+5)
    adY = oUtils.getRandom(coEggY-5, coEggY+5)

    print('>>> 执行点击彩蛋操作,坐标: (%d,%d) ' %(adX, adY))
    oUtils.tap(adX,adY)

    oUtils.setSleep(1)

    oUtils.backKey()

    oUtils.setSleep(2)

    #完成操作
    return

#看直播鸡蛋坐标：eggx,eggy 
def eatEggs(eggX,eggY):
    #等待界面稳定
    oUtils.setSleep(2)

    #获取点击的坐标，范围内随机值，10个像素的偏移
    eggX = oUtils.getRandom(eggX-5, eggX+5)
    eggY = oUtils.getRandom(eggY-5, eggY+5)

    #点击蛋蛋
    oUtils.tap(eggX,eggY)
    print('>>> 执行点击蛋蛋操作,坐标: (%d,%d) ' %(eggX, eggY))

    #等待动画完成
    oUtils.setSleep(2)
    return