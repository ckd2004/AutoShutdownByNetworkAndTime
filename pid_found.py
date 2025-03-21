import psutil

def find_pids_by_names(process_names):
    """根据进程名列表查找对应的 PID 列表"""
    pids = []
    for proc in psutil.process_iter():
        try:
            if proc.name() in process_names:
                pids.append(proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return pids if pids else False

def kill_processes_by_pids(pids):
    """根据 PID 列表结束对应的进程"""
    for pid in pids:
        try:
            proc = psutil.Process(pid)
            proc.kill()
            print(f"进程 {pid} 已被结束。")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"无法结束进程 {pid}，原因：{e}")

# 示例用法
if __name__ == "__main__":
    # 进程名列表
    process_names = ["MyPublicWiFi.exe", "March7th Launcher.exe"]
    # 查找 PID
    pids = find_pids_by_names(process_names)
    print(f"找到的 PID 列表：{pids}")
    # 结束进程
    if pids:
        #kill_processes_by_pids(pids)
        pass
    else:
        print("未找到任何匹配的进程。")