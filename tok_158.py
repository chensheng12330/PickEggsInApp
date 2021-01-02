#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import base as oUtils
import action_tool as act
import tiktok


'''
针对158号码进行抖音的视频查看，开宝箱操作.
'''
def main():

    #设置当前的设备为 (8514c020) ->158设备.
    oUtils.gb_devices_name = "8514c020"

    tok = tiktok.tiktok()

    count=0
    maxCount=100000

    print('\n\033[1;44m----------------启动抖音视频查阅自动化---------------------\033[0m')

    while count<maxCount:

        print(">>> 开始一个20分钟的循环操作...")
        count += 1
        
        #观看视频20分钟...
        tok.readVideo()
        act.wait(2)

        print(">>> 开宝箱,点广告，领金币.")
        tok.eatRadBagAndOpenBox()

        act.wait(2)
        
        #进入下一次循环
        print('--- 执行次数：%d, \n' % (count))
        continue

#启动开始
main()