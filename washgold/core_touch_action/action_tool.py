#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 常用操作动作库

# import os
# import sys
"""

print(__file__)#获取当前程序路径，注意：这里打印出来的路径为相对路径
#动态获取绝对路径
print(os.path.abspath(__file__)) #这才是当前程序绝对路径
print(os.path.dirname(os.path.abspath(__file__))) #当前程序上一级目录，其中dirname返回目录名，不要文件名
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#当前程序上上一级目录

"""
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #当前程序上上一级目录，这里为mycompany
# sys.path.append(BASE_DIR)
# sys.path.insert(0, '')

import os
import sys
from washgold.adb_cmd import base

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)




# import washgold.adb_cmd.base as oUtils
# from washgold.adb_cmd import base as oUtils
# from adb_cmd import base as oUtils
# import adb_cmd.base as oUtils
# from adb_cmd import base as oUtils
# import adb_cmd
# from .. import adb_cmd


def wait(second=1):
    """休眠，等待执行完.

    Args:
        second ([int]): [休眠时长，单位为秒.] Defaults to 1.
    """
    base.setSleep(second)
    return


def keepAlive():
    """
    触摸状态栏防止黑屏
    """
    oUtils.tap(500, 5)
    return


def tapWithRand(centX, centY, randLen=10):
    """[随机点击某个区域]

    Args:
        centX ([int]): [中心X坐标]
        centY ([int]): [中心Y坐标]
        rangLen (int, optional): [随机取值范围]. Defaults to 10.
    """
    halfRang = randLen / 2
    nTapX = oUtils.getRandom(centX - halfRang, centX + halfRang)
    nTapY = oUtils.getRandom(centY - halfRang, centY + halfRang)

    # 执行点击操作.
    oUtils.tap(nTapX, nTapY)
    return


# 随机向上滑动
def moveUpWithRand(centX, centY, randLen=10, moveLen=50, dura=700):
    """[随机向上滑动一段距离]

    Args:
        centX ([int]): [滑动开始的位置]
        centY ([type]): [滑动结束的位置]
        randLen (int, optional): [随机取值的范围]. Defaults to 10.
        moveLen (int, optional): [移动的长度]. Defaults to 50.
        dura (int, optional): [移动所需的时长,单位ms]. Defaults to 700.
    """
    halfRang = randLen / 2
    nTapX = oUtils.getRandom(centX - halfRang, centX + halfRang)
    nTapY = oUtils.getRandom(centY - halfRang, centY + halfRang)

    nMoveLen = oUtils.getRandom(moveLen, moveLen + 20)
    oUtils.move(nTapX, nTapY, nTapX, nTapY - nMoveLen, dura)
    return


# 随机向下滑动
def moveDownWithRand(centX, centY, randLen=10, moveLen=50, dura=700):
    """[随机向下滑动一段距离]

    Args:
        centX ([int]): [滑动开始的位置]
        centY ([type]): [滑动结束的位置]
        randLen (int, optional): [随机取值的范围]. Defaults to 10.
        moveLen (int, optional): [移动的长度]. Defaults to 50.
        dura (int, optional): [移动所需的时长,单位ms]. Defaults to 700.
    """
    halfRang = randLen / 2
    nTapX = oUtils.getRandom(centX - halfRang, centX + halfRang)
    nTapY = oUtils.getRandom(centY - halfRang, centY + halfRang)

    nMoveLen = oUtils.getRandom(moveLen, moveLen + 20)
    oUtils.move(nTapX, nTapY, nTapX, nTapY + nMoveLen, dura)
    return


# ………………………………………………………………………………………………
if __name__ == "__main__":
    print("pass")
    pass
