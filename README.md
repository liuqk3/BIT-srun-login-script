fork自https://coding.net/u/huxiaofan1223/p/jxnu_srun/git

作者已经毕业，很难再更新代码了。如果校园网有变动，并且你有好的解决方案，还请提个pr哈。非常感谢~~ o(*￣▽￣*)ブ

# 概述

北京理工大学深澜校园网登录python脚本，可用于任何支持python的设备的网络命令行登录或命令行登录。

详细文档见：[深澜校园网登录的分析与python实现-北京理工大学版](https://zhuanlan.zhihu.com/p/122556315)

# 文件说明

|文件|说明|
|:-:|:-:|
|BitSrunLogin/|深澜登录函数包|
|demo.py|登录示例脚本|
|always_online.py|在线监测脚本，如果监测到掉线则自动重连|

always_online.py可采用`nohup`命令挂在后台：
``` bash
nohup python always_online.py --username xxx --password xxx &
```
# linux 开机自启动
参考 https://zhuanlan.zhihu.com/p/523973210
1. 创建一个sh脚本，命名为`run_bit_login.sh`，其内容为：
```
nohup python3 /abs/path/to/always_online.py --username xxx --password xxx &
```
2. 设置脚本权限：
```
chmod +x run_bit_login.sh
```
3. 创建相应的服务”
```
sudo vim /lib/systemd/system/bit_auto_login.service
```
其内容为：
```
[Unit]
Description=scratch service
After=network.target network-online.target syslog.target
Wants=network.target network-online.target

[Service]
Type=simple

#launch the service, must be the abs path
ExecStart=bash /abs/path/to/run_bit_login.sh

[Install]
WantedBy=multi-user.target
```

4. 添加开机自启动：
```
systemctl enable scratch.service
```