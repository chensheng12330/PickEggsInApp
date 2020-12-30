#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys as oSys
import base as oUtils
import random as osRandom # 随机数

#点击上下文章列表
def tapNewsList():
    iRanY = oUtils.getRandom(500, 520)
    oUtils.setSleep(1)
    oUtils.tap(500,iRanY)
    oUtils.setSleep(1)
    return

#移动文章列表
def moveNextNewsList():
    oUtils.setSleep(1)
    oUtils.move(500,874,500,226,2000)
    oUtils.setSleep(2)
    return

def moveLastNewsList():
    oUtils.setSleep(1)
    oUtils.move(500,226,500,874,2000)
    oUtils.setSleep(2)
    return

#查阅文章，上下滑动
def readNews():
    #5秒休息一次，10分钟反向滑动
    #向下滑动
    moveCout = 10*60
    while moveCout>1:
        coEggX = 500
        coEggY = 940
        adX = oUtils.getRandom(coEggX-5, coEggX+5)
        adY = oUtils.getRandom(coEggY-5, coEggY+5)
        adL = oUtils.getRandom(40, 65)
        oUtils.move(adX,adY,adX,adY-adL,1000)
        oUtils.setSleep(5)
        moveCout -= 5

    #向上滑动
    moveCout = 2*60   
    while moveCout>1:
        adX = oUtils.getRandom(coEggX-5, coEggX+5)
        adY = oUtils.getRandom(coEggY-5, coEggY+5)
        adL = oUtils.getRandom(40, 65)
        oUtils.move(adX,adY-adL,adX,adY,1000)
        oUtils.setSleep(5)
        moveCout -= 5


def main():
    flag = 0
    addV = -1
    while 1:
        oUtils.setSleep(1)
        tapNewsList()
        oUtils.setSleep(1)
        readNews()
        oUtils.setSleep(1)
        oUtils.backKey()
        oUtils.setSleep(2)
        moveNextNewsList()

#执行            
#main()       
        

        
