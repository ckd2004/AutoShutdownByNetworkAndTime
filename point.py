import win32gui
import win32con
import subprocess
import pyautogui
import Permission_elevation as pe

def MyPublicWIFI():
    appsm = r"D:\\MyPublicWiFi\\MyPublicWiFi.exe"
    subprocess.run(appsm ,check=True)
    return True

def set_window_focus(window_title):
    """将指定窗口设为焦点"""
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        # 将窗口置于前台
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
        win32gui.SetForegroundWindow(hwnd)
        print(f"窗口 '{window_title}' 已设为焦点。")
        return hwnd
    else:
        print(f"未找到窗口 '{window_title}'。")
        return None
def click_in_window(window_title, x=168, y=623):
    """在窗口内点击指定坐标"""
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        # 获取窗口的左上角坐标
        rect = win32gui.GetWindowRect(hwnd)
        left, top, right, bottom = rect
        # 计算屏幕坐标
        screen_x = left + x
        screen_y = top + y
        # 点击指定坐标
        pyautogui.click(screen_x, screen_y)
        print(f"已点击窗口内的坐标 ({x}, {y})。")
    else:
        print("窗口句柄无效，无法执行点击操作。")