import time
import is_connected
import pid_found
import os
import datetime
from random import uniform
import argparse
import Permission_elevation as pe
#import subprocess
process_names = ["MyPublicWiFi.exe", "March7th Launcher.exe","StarRail.exe"]
title_name = "MyPublicWiFi"
SSID = "TP-LINK_8B45"


def check_time():
    """检查当前时间是否超过晚上9:30"""
    current_time = datetime.datetime.now()
    return current_time.hour > 21 or (current_time.hour == 21 and current_time.minute >= 30)

def check_time_for_shutdown():
    """检查当前时间是否超过晚上10:00"""
    current_time = datetime.datetime.now()
    return current_time.hour >= 22

def shutdown():
    """执行关机操作"""
    pe.elevate_privileges()#提权函数
    #subprocess.run("adb shell reboot -p", shell=True)#Android模拟器关机命令，用来测试能不能正常执行关机函数
    os.system("shutdown -s -t 0")

def is_shutdown(address, check_1, check_time_is):
    # 首先立即检查一次
    current_time = datetime.datetime.now()
    current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # 检查时间是否超过晚上10:00，如果是则直接关机
    if check_time_for_shutdown():
        print(f"[{current_time_str}] 当前时间超过晚上10:00，正在执行关机操作...")
        pids = pid_found.find_pids_by_names(process_names)
        if pids:
            print(f"找到以下 PID 对应的 {process_names} 进程: {pids}")
            end = pid_found.kill_processes_by_pids(pids)
            if end == False:
                print(f"未找到任何名称叫{process_names}的进程!!")
            else:
                print(f"进程名:{process_names}.pid:{pids}已成功结束!!")
        else:
            print(f"未找到名为 {process_names} 的进程。")
        shutdown()
        return

    # 检查时间和网络连接情况
    elif check_time() and not is_connected.is_connected(address):
        print(f"[{current_time_str}] 当前时间超过晚上9:30，且网络未连接，正在执行关机操作...")
        pids = pid_found.find_pids_by_names(process_names)
        if pids:
            print(f"找到以下 PID 对应的 {process_names} 进程: {pids}")
            pid_found.kill_processes_by_pids(pids)
            print(f"已尝试结束这些进程。")
        else:
            print(f"未找到名为 {process_names} 的进程。")
        shutdown()
        return

    else:
        print(f"[{current_time_str}] 当前时间：{current_time.hour}:{current_time.minute}，网络连接状态：{f'已连接{SSID}' if is_connected.is_connected(address) else '未连接'}，未满足关机条件。")

    # 然后进入循环，每隔随机时间检查一次
    while True:
        check_1 = float(check_1)
        check_time_is = float(check_time_is)
        sleep_time = uniform(check_1, check_time_is)
        time.sleep(sleep_time)

        current_time = datetime.datetime.now()
        current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

        if check_time_for_shutdown():
            print(f"[{current_time_str}] 当前时间超过晚上10:00，正在执行关机操作...")
            pids = pid_found.find_pids_by_names(process_names)
            if pids:
                print(f"找到以下 PID 对应的 {process_names} 进程: {pids}")
                end = pid_found.kill_processes_by_pids(pids)
                if end == False:
                    print(f"未找到任何名称叫{process_names}的进程!!")
                else:
                    print(f"进程名:{process_names}.pid:{pids}已成功结束!!")
            else:
                print(f"未找到名为 {process_names} 的进程。")
            shutdown()
            break

        elif check_time() and not is_connected.is_connected(address):
            print(f"[{current_time_str}] 当前时间超过晚上9:30，且网络未连接，正在执行关机操作...")
            pids = pid_found.find_pids_by_names(process_names)
            if pids:
                print(f"找到以下 PID 对应的 {process_names} 进程: {pids}")
                pid_found.kill_processes_by_pids(pids)
                print(f"已尝试结束这些进程。")
            else:
                print(f"未找到名为 {process_names} 的进程。")
            shutdown()
            break

        else:
            print(f"[{current_time_str}] 当前时间：{current_time.hour}:{current_time.minute}，网络连接状态：{f'已连接{SSID}' if is_connected.is_connected(address) else '未连接'}，未满足关机条件。")


def main():
    """主函数，支持命令行参数传入检查时间和网址"""
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="自动关机脚本")
    parser.add_argument("check_time", nargs="?", type=str, help="检查间隔时间（整数）")
    parser.add_argument("address", nargs="?", type=str, help="要检测的网址")
    args = parser.parse_args()

    # 处理检查时间参数
    if args.check_time:
        try:
            check_time_is = int(args.check_time)  # 尝试将参数转为整数
        except ValueError:
            print(f"错误：检查时间需为整数，输入 '{args.check_time}' 无效")
            check_time_is = int(input("请重新输入检查时间（整数）: "))
    else:
        check_time_is = int(input("请输入检查时间（整数）: "))

    check_1 = check_time_is / 2  # 计算随机等待时间的下限

    # 处理网址参数
    if args.address:
        address = args.address.strip()  # 直接使用传入的网址
    else:
        input_address = input("请输入检测网址（留空默认百度）: ").strip()
        address = input_address or "www.baidu.com"  # 输入为空则用默认值

    # 清屏并打印启动信息
    os.system("cls")
    if check_time_is>60:
        check_time_is=check_time_is/60
        print(f"自动关机脚本已启动，每 {check_time_is} 分钟检查一次")
    else:
        print(f"自动关机脚本已启动，每 {check_time_is} 秒检查一次")
    is_shutdown(address,check_1,check_time_is)

    
if __name__ == "__main__":
    main()