import subprocess
import time
import Permission_elevation as pe

def is_connected(address, max_retries=3, retry_delay=2):
    pe.elevate_privileges()
    """
    检查网络连接状态，添加重试机制

    参数:
        address (str): 目标网址或IP地址（不带http://）
        max_retries (int): 最大重试次数，默认为3次
        retry_delay (int): 每次重试之间的延迟（秒），默认为2秒

    返回:
        bool: 如果连接成功返回True，否则返回False
    """
    retries = 0
    while retries < max_retries:
        try:
            # 使用ping命令检查连接
            # 参数：-c 1 表示发送1个ECHO_REQUEST，-w 5 表示超时时间为5秒
            response = subprocess.run(
                ["ping", "-c", "1", "-w", "5", address],
                stdout=subprocess.DEVNULL,  # 不输出标准输出
                stderr=subprocess.DEVNULL   # 不输出标准错误
            )
            # 如果ping命令返回码为0，表示连接成功
            if response.returncode == 0:
                return True
            else:
                # 如果返回码不为0，也视为连接失败
                return False
        except Exception as e:
            # 捕获异常，比如ping命令执行失败等
            print(f"Error occurred: {e}")
            retries += 1
            if retries < max_retries:
                time.sleep(retry_delay)
            else:
                return False
    return False
if __name__ == "__main__":
    # 测试网址
    print(is_connected("www.baidu.com"))  # True 或 False

    # 测试IP地址
    print(is_connected("8.8.8.8"))  # True 或 False