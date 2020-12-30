#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 今日头条操作流程
import sys as oSys
import base as oUtils
import random as osRandom # 随机数
import read_news as news

class toutiao(object):

    #宝箱坐标：eggX,eggY
    def eatBox(self,eggX,eggY):
        oUtils.setSleep(2)
        #点击宝箱
        eggX = oUtils.getRandom(eggX-5, eggX+5)
        eggY = oUtils.getRandom(eggY-5, eggY+5)
        
        print('>>> 执行点击宝箱操作,坐标: (%d,%d) ' %(eggX, eggY))
        oUtils.tap(eggX,eggY)

        #等待动画
        oUtils.setSleep(3)

        print('>>> 完成点击宝箱操作')
        return

    #视频广告坐标：adX,adY,  needBack:是否结束时返回上级页面 0:NO, >0 YES
    def eatAD(self,adX,adY,needBack):

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

        print('>>> 完成视频广告操作')
        return

    #阅读文章并开箱
    def readNewsAndEatBox(self):
        #等待界面稳定
        oUtils.setSleep(1)

        print('\n\033[1;32m>>> 文章阅读 \033[0m')
        oUtils.setSleep(1)

        #点击文章列表

        print('>>> 点击文章列表')
        news.tapNewsList(0)
        #等待界面稳定
        oUtils.setSleep(2)

        #阅读新闻 10分钟一次
        print('>>> 阅读新闻,10分钟一次')
        news.readNews(600)

        oUtils.setSleep(1)

        #点击开宝箱 10分钟一次
        #--------------------------
        #点击红包到任务中心
        print('>>> 跳转到任务中心，等待6s...')
        oUtils.tap(170,140)

        #等任务中心加载出来
        oUtils.setSleep(6)

        #点击宝箱
        print('>>> 点击宝箱，开宝箱')
        self.eatBox(905,665)
        oUtils.setSleep(3)

        #看广告
        self.eatAD(575,785,1)

        #休息3s
        oUtils.setSleep(2)

        #返回到文章页面.
        oUtils.backKey()
        oUtils.setSleep(2)
        #--------------------------

        #返回到文章列表
        print('>>> 返回到文章列表.')
        oUtils.backKey()
        oUtils.setSleep(3)

        #移动到新的文章列表
        print('>>> 移动到下篇文章.')
        news.moveNextNewsList()

        return



#测试用例
def tt_test_main():
    tt = toutiao()
    tt.eatBox(55,33)
    tt.eatAD(12,43,1)
    return

#tt_test_main()