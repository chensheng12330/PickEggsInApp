#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os as osOs # 内置shell交互
from os import popen as osPopen # 管道处理
from os import system as osSystem # 管道处理
import random as osRandom # 随机数
from time import sleep as osSleep
import re as osRe

#全局变量：设备号
gb_devices_name = ""

# 随机函数
def getRandom(iMin, iMax):
  return osRandom.randint(iMin, iMax)

# 延时
def setSleep(iMin, iMax = 999):
  iRandom = iMin
  if iMax != 999:
    iRandom = getRandom(iMin, iMax)
  osSleep(iRandom)

# 点击
def tap(iX, iY):
  osPopen('adb shell input tap %d %d' % (iX, iY))

# 滑动 开始x,y  结束x,y  dura:滑动时长ms
def move(iStartX, iStartY, iEndX, iEndY, dura):
  osPopen('adb shell input swipe %d %d %d %d %d' % (iStartX, iStartY, iEndX, iEndY, dura))

# 调用app
def callApp(sVal):
  osPopen('adb shell am start -D -S -n %s' % sVal)

# 调用app
def closeApp(sVal):
  osPopen('adb shell am force-stop %s' % sVal)

def vmSize():
  sVmSize = osPopen('adb shell wm size').read()
  aVmSize = osRe.search(r'(\d+)x(\d+)', sVmSize)
  return {'w': aVmSize.group(1), 'h': aVmSize.group(2)}

#设置屏亮度 最大值255
def screen_brightness(iLen = 255):
  osPopen('adb %s shell settings put system screen_brightness %d ' % (gb_devices_name, iLen))
  

#返回键
def backKey():
  osPopen('adb shell input keyevent 4')

#点亮主屏
def  ligtPhone():
  osPopen('adb %s shell input keyevent 224', gb_devices_name)

# 视频上滑
def swipeMoive(iLen = 50):
  i = 0
  while i < iLen:
    i += 1
    move(425, 1200, 460, 800,500) # 上滑
    iRan = getRandom(8, 25)
    print('执行次数：%d, 时长：%d' % (i, iRan)) # 打印
    setSleep(iMin = iRan) # 延时

#test 用列
def test_userDevcies():
  global gb_devices_name
  gb_devices_name = "-s e3656a1b"
  screen_brightness(100)

def test_NOuserDevcies():
  #global gb_devices_name
  #gb_devices_name = "-s e3656a1b"
  screen_brightness(100)

#test_userDevcies()
#test_NOuserDevcies()