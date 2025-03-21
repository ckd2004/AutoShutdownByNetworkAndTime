# AutoShutdownByNetworkAndTime

This script automatically monitors network status and system time conditions to trigger a shutdown when preset criteria are met. By ensuring the system is only active during required periods, it conserves energy and enhances overall system safety.

## Features
- Monitors network connectivity.
- Triggers shutdown based on preset time intervals.
- Offers flexible configuration of network and time criteria.

## Usage
1. Modify the network detection and time settings in the script to fit your environment.
2. Run the script in an administrator command prompt to ensure it has the necessary permissions.
3. The script continuously monitors the conditions and will execute a shutdown when all preset conditions are met.

## Important Notes
- Always back up important data to avoid losing unsaved work due to an automated shutdown.
- Ensure the script is executed with sufficient permissions; otherwise, the shutdown command might fail.
- Regularly review the network settings and time parameters to ensure proper operation.

## Changelog
- Initial version: Implemented auto-shutdown based on network status and time conditions.
- Future versions: Enhancements and optimizations based on user feedback and runtime analysis.

## Default Settings
- Permission Elevation: Requires administrator privileges.
- Process Monitoring: Before shutdown, specified programs are closed (configurable via the `process_names` list in the `main` function).
- Network Check: Uses administrative rights to check for network connectivity.
- To run the script, use the command:  
    Python main.py <check interval (s)> <network URL (default: www.baidu.com)>  
    An interval above 60 seconds will be automatically converted into minutes.
- The check interval is randomized between half the user-defined interval and the full value.
- Shutdown times are fixed at 9:30 PM (if the network is disconnected) and 10:00 PM (forced shutdown). Adjust the time-check logic in the `check_time` function as needed.

## 功能介绍
该脚本自动监控网络状态及系统时间条件，根据预设条件自动执行关机操作，确保在无用时段自动节省能源并保障系统安全。

## 主要功能
- 自动检查网络连接状态
- 根据设定的时间范围触发关机命令
- 灵活配置网络及时间条件，满足不同需求

## 使用方法
1. 根据实际网络环境与需求，修改脚本中的网络检测及时间设定参数。
2. 在具有管理员权限的命令行环境中运行脚本。
3. 脚本将持续监控条件，一旦满足预设条件，即会自动执行关机操作。

## 注意事项
- 使用前请备份重要数据，防止因自动关机导致未保存工作丢失。
- 脚本需在系统具有足够权限的情况下运行，否则可能无法成功执行关机命令。知晓在Windows上让此脚本拥有管理员权限的危害以及如何控制危险
- 定期检查网络设置及时间参数，确保功能正常运行。

## 更新日志
- 初始版本：实现基于网络状态和时间条件的自动关机功能。
- 后续版本：将根据实际运行情况进行优化提升。
## 默认配置
- Permission_elevation:此为提权脚本,运行前请确保你有足够的权限,
- pid_found:寻找程序,在关机前关闭指定程序,保存工作.配置```main```的```process_names```列表来添加或者删除程序
- is_connected:来检测网络是否连接(管理员权限)
- 此脚本可以通过传入参数```Python <脚本名称:mian.py> <检查的间隔时间(s)> <检测网络连接的网址(默认为www.baidu.com)>```检查时间输入>60s会自动显示为分
- 检查时间为(输入的检查时间/2~输入的检查时间)为随机数波动
- 关机时间固定为晚上9:30(未连接网络关机),10点(强制关机).时间可以通过修改```主函数的``````check_time``` 的 ```return```里比较值来实现
