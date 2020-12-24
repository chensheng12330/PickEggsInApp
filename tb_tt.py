#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 快手
import sys as oSys
import base as oUtils
import random as osRandom # 随机数
import taobao as TB #淘宝操作流程

#上部分头条，下部分淘宝 （10分钟一次操作）

#头条部分
def toutao():
    oUtils.setSleep(2)
    #点击宝箱
    eggX = oUtils.getRandom(900, 910)
    eggY = oUtils.getRandom(660, 670)
    oUtils.tap(eggX,eggY)
    print('>>> 执行点击宝箱操作,坐标: (%d,%d) ' %(eggX, eggY))

    #等待动画
    oUtils.setSleep(3)

    #看广告,点击位置
    adX = oUtils.getRandom(570, 580)
    adY = oUtils.getRandom(780, 790)

    print('>>> 执行点击观看广告操作,坐标: (%d,%d) ' %(adX, adY))
    oUtils.tap(adX,adY)
    

    #等待广告看完
    print('>>> 等待广告看完')
    oUtils.setSleep(25)

    
    #返回到上级页面
    oUtils.backKey()
    #等待动画完成
    oUtils.setSleep(2)

    print('>>> 完成点击宝箱操作')
    return

#淘宝部分
def taobao():
    oUtils.setSleep(1)

    #点击蛋蛋
    eggX = oUtils.getRandom(900, 910)
    eggY = oUtils.getRandom(1700, 1710)
    oUtils.tap(eggX,eggY)
    print('>>> 执行点击蛋蛋操作,坐标: (%d,%d) ' %(eggX, eggY))

    #等待动画
    oUtils.setSleep(2)

    #点击蛋蛋进行彩蛋页面
    oUtils.tap(eggX,eggY)

    #等待页面动画
    oUtils.setSleep(4)

    #点击彩蛋
    adX = oUtils.getRandom(910, 920)
    adY = oUtils.getRandom(1390, 1400)

    print('>>> 执行点击彩蛋操作,坐标: (%d,%d) ' %(adX, adY))
    oUtils.tap(adX,adY)

    oUtils.setSleep(1)

    oUtils.backKey()

    oUtils.setSleep(2)

    #完成操作
    return


def main():
    maxCount=100000
    count=0

    while count<maxCount:

        count += 1

        print('\n\033[1;44m----------------启动操作---------------------\033[0m')

        #休息到下转值 10分钟一次
        iRan = oUtils.getRandom(600, 610)

        #头条执行

        print('\033[1;35m>>> 头条夺宝\033[0m')
        toutao()

        #休息3s
        oUtils.setSleep(4)

        #淘宝执行
        print('\n\033[1;32m>>> 淘宝夺宝 \033[0m')
        taobao()

        print('--- 执行次数：%d, 休眠时长：%d' % (count, iRan)) # 打印
        print('----------------休眠中---------------------')
        #print('eggY: %d,sleepT: %d,iRan: %d' % (eggY, sleepT, iRan))
        sleepTime = iRan/4

        while iRan>6 :
            iRan -= sleepTime
            oUtils.setSleep(sleepTime)
            oUtils.tap(500,5) #防止屏黑.
            print('>>> 休眠中(%d) \n' % (iRan))


#-------------------------------------------------
#执行主程序
main()