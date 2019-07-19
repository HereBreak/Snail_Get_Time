#!/usr/local/bin/python
# coding=utf-8

import uiautomator2 as u2
from time import sleep
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# 领时长弹窗
def if_daily_popup_exist(driver):
    if driver(resourceId="com.netease.snailread:id/daily_get_free").exists():
        return True
    else:
        return False


# 活动弹窗
def if_activity_popup_exist(driver):
    if driver(resourceId="com.netease.snailread:id/gift_container").exists():
        return True
    else:
        return False


# 捕获是否超过设备领取限制的toast 捕获不到？需要用到图像识别，后续结合OpenCV再看
# def if_toast_exist(driver,toastmessage,timeout=30,poll_frequency=0.5):
#     try:
#         toast_ele = ("xpath", ".//*[contains((@text,'%s')]" % toastmessage)
#         toast_text = WebDriverWait(driver, timeout, poll_frequency).until(
#             expected_conditions.presence_of_element_located(toast_ele))
#         return toast_text.text
#     except:
#         return False


# 获取设备ID
def get_devices_name():
    # 执行adb devices，获取连接设备id列表
    output = os.popen("adb devices")
    # 按行读取执行结果
    list_name = output.readlines()
    # 执行结果有两行，将第二行以空格拆分成两个字符串,返回第一个字符串
    device_name = list_name[1].split('\t')
    return device_name[0]


# 测试免费时长领取
def popup_get_time_test():
    # os.system("adb kill-server")
    # os.system("adb server")
    # 启atx
    os.system("python3 -m uiautomator2 clear-cache")
    os.system("python3 -m uiautomator2 init")
    # 连接设备
    d = u2.connect_adb_wifi(get_devices_name())
    # 启动蜗牛
    d.app_stop("com.netease.snailread")
    d.app_start("com.netease.snailread")
    sleep(7)
    if if_daily_popup_exist(d):
        d(resourceId="com.netease.snailread:id/daily_get_free").click()
        sleep(7)
        d.press("back")
        d(text="书桌").click()
        sleep(3)
        if if_activity_popup_exist(d):# 有活动弹窗则先消去
            d.press("back")
        sleep(1)
        if d.exists(text="120"):
            print("成功领取120分钟广告时长")
        elif d.exists(text="60"):
            print("成功领取60分钟免费时长")
        else:
            print("时长领取失败")
    else:
        os.system("python3 -m uiautomator2 screenshot screenshot.jpg")
        print("无领时长弹窗")
    d.app_stop("com.netease.snailread")


if __name__ == "__main__":
    popup_get_time_test()