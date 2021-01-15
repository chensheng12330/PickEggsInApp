#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import base as oUtils
import toutao as ttAPP

'''
进行今日头条的文章阅读，开宝箱操作.
'''
def main():

    #设置当前的设备为 (a790be09) ->137设备.
    oUtils.gb_devices_name = "a790be09"

    tt = ttAPP.toutiao()

    count=0
    maxCount=4

    while count<maxCount:

        count += 1
        print('\n\033[1;44m----------------启动自动化---------------------\033[0m')
        
        tt.readNewsAndEatBox()

        oUtils.setSleep(1)
        
        #进入下一次循环
        print('--- 执行次数：%d, \n' % (count))
        continue

#启动开始
main()
