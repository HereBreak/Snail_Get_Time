# coding=utf-8
import uiautomator2 as u2
from time import sleep
import os
import airtest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def get_devices_name():
    # 执行adb devices，获取连接设备id列表
    output = os.popen("adb devices")
    # 按行读取执行结果
    list_name = output.readlines()
    # 执行结果有两行，将第二行以空格拆分成两个字符串,返回第一个字符串
    device_name = list_name[1].split('\t')
    return device_name[0]


def if_popup_exist():
    if d(resourceId="com.netease.snailread:id/daily_get_free").exists():
        return True
    else:
        return False


# 捕获toast 捕获不到？
# def if_toast_exist(driver,toastmessage,timeout=30,poll_frequency=0.5):
#     try:
#         toast_ele = ("xpath", ".//*[contains((@text,'%s')]" % toastmessage)
#         toast_text = WebDriverWait(driver, timeout, poll_frequency).until(
#             expected_conditions.presence_of_element_located(toast_ele))
#         return toast_text.text
#     except:
#         return False


def get_time_test():
    # 启动蜗牛
    d.app_stop("com.netease.snailread")
    d.app_start("com.netease.snailread")
    sleep(5)
    if if_popup_exist():
        d(resourceId="com.netease.snailread:id/daily_get_free").click()
        sleep(7)
        d.press("back")
        d(text="书桌").click()
        sleep(3)
        if d.exists(text="120分钟"):
            print("成功领取120分钟广告时长")
        elif d.exists(text="60分钟"):
            print("成功领取60分钟免费时长")
        else:
            print("时长领取失败")
    else:
        print("无领时长弹窗")
    d.app_stop("com.netease.snailread")


if __name__ == "__main__":
    # 启atx
    os.system("python3 -m uiautomator2 init")
    # 连接设备
    d = u2.connect_adb_wifi(get_devices_name())
    get_time_test()