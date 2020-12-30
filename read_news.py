#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys as oSys
import base as oUtils
import random as osRandom # 随机数

#点击上下文章列表
def tapNewsList(offsetY):
    iRanY = oUtils.getRandom(500, 520) - offsetY
    oUtils.setSleep(1)
    oUtils.tap(500,iRanY)
    oUtils.setSleep(1)
    return

#移动文章列表
def moveNextNewsList():
    oUtils.setSleep(1)
    oUtils.move(500,870,500,230,2000)
    oUtils.setSleep(2)
    return

def moveLastNewsList():
    oUtils.setSleep(1)
    oUtils.move(500,226,500,874,2000)
    oUtils.setSleep(2)
    return

#查阅文章，上下滑动
def readNews(beginY):
    #5秒休息一次，10分钟反向滑动

    #向上移动8分钟，向下移动2分钟，共10分钟.
    
    moveCout = 8*60
    moveNum  = 0
    
    coEggX = 500
    coEggY = beginY

    #向上滑动
    while moveCout>1:
        
        adX = oUtils.getRandom(coEggX-20, coEggX+20)
        adY = oUtils.getRandom(coEggY-5, coEggY+5)
        adL = oUtils.getRandom(45, 70)
        oUtils.move(adX,adY,adX,adY-adL,800)
        oUtils.setSleep(5)
        moveCout -= 5
        moveNum += 1
        print(">>> 文章阅读中，->向上移动次数 (%d)..." % (moveNum))

    #向下滑动
    moveNum = 0
    moveCout = 2*60   
    while moveCout>1:
        adX = oUtils.getRandom(coEggX-20, coEggX+20)
        adY = oUtils.getRandom(coEggY-5, coEggY+5)
        adL = oUtils.getRandom(45, 70)
        oUtils.move(adX,adY-adL,adX,adY,800)
        oUtils.setSleep(5)
        moveCout -= 5
        moveNum += 1
        print(">>> 文章阅读中，<-向下移动次数 (%d)..." % (moveNum))


def main():
    while 1:
        oUtils.setSleep(1)
        tapNewsList(0)
        oUtils.setSleep(1)
        readNews(940)
        oUtils.setSleep(1)
        oUtils.backKey()
        oUtils.setSleep(2)
        moveNextNewsList()

#执行            
def test_1():
    moveNextNewsList()


#test_1()
        

        
