#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 抖音直播操作流程
import sys as oSys
import base as oUtils
import random as osRandom # 随机数

class tiktok(object):
    
    #视频观看，上下滑动

    #上一个视频
    def moveNextNewsList(self):
        oUtils.setSleep(1)
        oUtils.move(500,874,500,226,2000)
        oUtils.setSleep(2)
        return

    #下一个视频
    def moveLastNewsList(self):
        oUtils.setSleep(1)
        oUtils.move(500,226,500,874,2000)
        oUtils.setSleep(2)
        return

    #观看视频，上下滑动(计时时间.)
    def readNews(self):
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

    #看开宝箱坐标：eggx,eggy 
    def eatEggs(self,eggX,eggY):
        #等待界面稳定
        oUtils.setSleep(2)

        #获取点击的坐标，范围内随机值，10个像素的偏移
        eggX = oUtils.getRandom(eggX-5, eggX+5)
        eggY = oUtils.getRandom(eggY-5, eggY+5)

        #点击蛋蛋
        print('>>> 执行点击蛋蛋操作,坐标: (%d,%d) ' %(eggX, eggY))

        oUtils.tap(eggX,eggY)
        
        #等待动画完成
        oUtils.setSleep(2)

        print('>>> 完成点击直播鸡蛋操作')
        return