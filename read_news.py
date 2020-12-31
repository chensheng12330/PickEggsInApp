#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys as oSys
import base as oUtils
import random as osRandom  # 随机数

def tapNewsList(offsetY):
    """[点击文章列表中的某篇文章]

    Args:
        offsetY ([数字]): [文章的Y坐标值]
    """    
    iRanY = oUtils.getRandom(500, 520) - offsetY
    oUtils.setSleep(1)
    oUtils.tap(500, iRanY)
    oUtils.setSleep(1)
    return

# 移动文章列表
def moveNextNewsList(moveX=500,BegY=870,EndY=230,delay=800):
    """
    移动文章列表，使其处理顶部位置，方便行文章点击操作  
    可配合 [tapNewsList] 操作

    Args:
        moveX (int, optional): [移动的X坐标值]. Defaults to 500.
        BegY (int, optional): [移动开始的Y坐标]. Defaults to 870.
        EndY (int, optional): [移动结束的Y坐标]. Defaults to 230.
        delay (int, optional): [移动持续时长,单位ms]. Defaults to 800.
    """    
    oUtils.setSleep(1)
    oUtils.move(moveX, BegY, moveX, EndY, delay)
    oUtils.setSleep(1)
    return

def moveLastNewsList():
    oUtils.setSleep(1)
    oUtils.move(500, 226, 500, 874, 2000)
    oUtils.setSleep(2)
    return


def readNews(beginY):

    """[summary]
    """    

    '''
    #查阅文章，上下滑动  
    #10分钟一次阅读,8分钟向下滑动，2分钟向上滑动  
    #beginY: 滑动开始的位置（分屏时APP占屏只有一半）  
    '''
    # 5秒休息一次，10分钟反向滑动
    # 向上移动8分钟，向下移动2分钟，共10分钟.

    moveCout = 8*60
    moveNum = 0

    coEggX = 500
    coEggY = beginY

    # 向上滑动
    while moveCout > 1:

        adX = oUtils.getRandom(coEggX-20, coEggX+20)
        adY = oUtils.getRandom(coEggY-5, coEggY+5)
        adL = oUtils.getRandom(45, 70)
        oUtils.move(adX, adY, adX, adY-adL, 700)
        oUtils.setSleep(5)
        moveCout -= 5
        moveNum += 1
        print(">>> 文章阅读中，->向上移动次数 (%d)..." % (moveNum))

    # 向下滑动
    moveNum = 0
    moveCout = 2*60
    while moveCout > 1:
        adX = oUtils.getRandom(coEggX-20, coEggX+20)
        adY = oUtils.getRandom(coEggY-5, coEggY+5)
        adL = oUtils.getRandom(45, 70)
        oUtils.move(adX, adY-adL, adX, adY, 700)
        oUtils.setSleep(5)
        moveCout -= 5
        moveNum += 1
        print(">>> 文章阅读中，<-向下移动次数 (%d)..." % (moveNum))


def test_main():
    '''测试主流程'''

    while 1:
        oUtils.setSleep(1)
        tapNewsList(0)
        oUtils.setSleep(1)
        readNews(940)
        oUtils.setSleep(1)
        oUtils.backKey()
        oUtils.setSleep(2)
        moveNextNewsList()

# 执行


def test_1():
    '''其它'''
    moveNextNewsList()


if __name__ == "__main__":
    #test_main()
    pass
