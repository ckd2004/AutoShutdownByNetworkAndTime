import ctypes
import sys
import os
import psutil
import subprocess
import shlex
from time import sleep



def is_admin():
    """检查管理员权限"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def elevate_privileges():
    """提升权限到管理员模式"""
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1
        )
        sys.exit()

def is_process_running(process_name):
    """检查进程是否正在运行"""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'].lower() == process_name.lower():
            return True
    return False

def start_program(full_command):
    """启动指定程序并返回执行状态"""
    try:
        # 分割命令为路径和参数
        parts = shlex.split(full_command)
        if not parts:
            raise ValueError("无效的命令格式")
        
        exe_path = parts[0]
        args = parts[1:]
        
        # 确保文件存在
        if not os.path.isfile(exe_path):
            raise FileNotFoundError(f"文件不存在: {exe_path}")
        
        process_name = os.path.basename(exe_path)
        
        if is_process_running(process_name):
            return "already_running"
            
        subprocess.Popen(
            [exe_path] + args,
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return "success"
        
    except Exception as e:
        return f"error: {str(e)}"

if __name__ == "__main__":
    start_program()