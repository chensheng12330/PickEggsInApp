#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import base as oUtils
import action_tool as act
import tiktok


'''
针对171号码进行抖音的开宝箱操作，做广告任务.

宝箱：10分钟一次
广告任务：20分钟一次

需要全屏页面，将任务列表栏

'''
def main():

    #设置当前的设备为 (e3656a1b) ->171设备.
    oUtils.gb_devices_name = "e3656a1b"

    tok = tiktok.tiktok()

    count=0
    maxCount=100000

    print('\n\033[1;44m----------------启动抖音开宝箱，做视频广告任务--------------------\033[0m')

    while count<maxCount:

        print(">>> 开始一个20分钟的循环操作...")
        count += 1
        
        #等10分钟....
        #act.wait(11*60)
        print(">>> 1.开宝箱,点广告，领金币.")
        

        #act.wait(10*60)
        #print(">>> 3.开宝箱,点广告，领金币.")
        #tok.eatRadBagAndOpenBox()
        #act.wait(2)

        # print(">>> 2.做任务,点广告，领金币.")
        # act.tapWithRand(700,380,16)
        # #等广告看完
        # act.wait(60)
        # oUtils.backKey()
        # act.wait(3)
        # oUtils.backKey()
        # act.wait(3)
        
        
        
        
        #进入下一次循环
        print('--- 执行次数：%d, \n' % (count))
        continue

#启动开始
main()