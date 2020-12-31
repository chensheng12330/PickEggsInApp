#!/bin/bash
#设置手机屏幕亮度: 0~255  ./setBgl 135|171|158 100

#先设置为手动模式

dev_name=""

if [ $1 = "135" ]; 
then
    dev_name='-s 4857d2bc'
fi

if [ $1 = "171" ];
then 
    dev_name='-s e3656a1b'
fi

if [ $1 = "158" ]; 
then 
    dev_name='-s 8514c020'
fi

# echo $1
# echo $2
# echo $dev_name

adb $dev_name shell settings put system screen_brightness_mode 0
adb $dev_name shell settings put system screen_brightness $2
#cmdStr1="adb ".$dev_name." shell settings put system screen_brightness_mode 0"
#cmdStr2="adb ".$dev_name." shell settings put system screen_brightness ".$1

#exec(cmdStr1)
#exec(cmdStr2)
