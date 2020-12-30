#!/bin/bash
#设置手机屏幕亮度: 0~255  ./setBgl 100

#先设置为手动模式
adb shell settings put system screen_brightness_mode 0

#设置屏亮度
adb shell settings put system screen_brightness $1