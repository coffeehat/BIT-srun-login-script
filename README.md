fork自：https://github.com/coffeehat/BIT-srun-login-script

另有支持多平台（包括openwrt）的golang版本，请见：https://github.com/Mmx233/BitSrunLoginGo

经过几个参数修改，已经可以实现中国科学院大学雁栖湖校区的上网认证（深澜）。  P.S.没改几个地方，还不如readme改的多😂

# 概述

中国科学院大学雁栖湖校区深澜校园网登录python脚本，可用于任何支持python的设备的网络命令行登录或命令行登录。

详细文档见原作者（存疑）：[深澜校园网登录的分析与python实现-北京理工大学版](https://zhuanlan.zhihu.com/p/122556315)

# 文件说明

|文件|说明|
|:-:|:-:|
|BitSrunLogin/|深澜登录函数包|
|demo.py|登录示例脚本|
|always_online.py|在线监测脚本，如果监测到掉线则自动重连|

always_online.py可采用`nohup`命令挂在后台：
``` bash
nohup python always_online.py &
```
