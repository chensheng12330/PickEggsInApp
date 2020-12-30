#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os as osOs # 内置shell交互
from os import popen as osPopen # 管道处理
from os import system as osSystem # 管道处理
import random as osRandom # 随机数
from time import sleep as osSleep
import re as osRe

#全局变量：设备号, 默认连接的设备只有一台，可以不用使用.
gb_devices_name = ""

#如有多设备，需要组装相应的字符串
def get_devices_str():
  cmd_dev_name = ""
  if gb_devices_name != "":
    cmd_dev_name = "-s " + gb_devices_name

  return cmd_dev_name

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
  osPopen('adb %s shell input tap %d %d' % (get_devices_str(), iX, iY))

# 滑动 开始x,y  结束x,y  dura:滑动时长ms
def move(iStartX, iStartY, iEndX, iEndY, dura):
  osPopen('adb %s shell input swipe %d %d %d %d %d' % (get_devices_str(), iStartX, iStartY, iEndX, iEndY, dura))

# 调用app
def callApp(sVal):
  osPopen('adb %s shell am start -D -S -n %s' % (get_devices_str(),sVal))

# 调用app
def closeApp(sVal):
  osPopen('adb %s shell am force-stop %s' % (get_devices_str(),sVal))

def vmSize():
  sVmSize = osPopen('adb shell wm size').read()
  aVmSize = osRe.search(r'(\d+)x(\d+)', sVmSize)
  return {'w': aVmSize.group(1), 'h': aVmSize.group(2)}

#设置屏亮度 最大值255
def screen_brightness(iLen = 255):
  osPopen('adb %s shell settings put system screen_brightness %d ' % (gb_devices_name, iLen))

#设置屏是否自动调节模式  isAuto: 1是， 0：否.
def screen_brightness_mod(isAuto = 1):
  osPopen('adb %s shell settings put system screen_brightness_mode %d' % (gb_devices_name,isAuto))

#返回键
def backKey():
  osPopen('adb %s shell input keyevent 4' % (gb_devices_name))

#点亮主屏
def  ligtPhone():
  osPopen('adb %s shell input keyevent 224' % (gb_devices_name))

'''
----------------------------------------------------------------
下面是测试用例,仅供调试时使用.
'''

#test 用列
def test_tip():
  global gb_devices_name
  gb_devices_name = "e3656a1b"
  #tap(500,300)
  move(500,600,500,300,1000)
  return

def test_userDevcies():
  global gb_devices_name
  gb_devices_name = "e3656a1b"
  screen_brightness(100)

def test_NOuserDevcies():
  #global gb_devices_name
  #gb_devices_name = "-s e3656a1b"
  screen_brightness(100)

#test_userDevcies()
#test_NOuserDevcies()
#test_tip()