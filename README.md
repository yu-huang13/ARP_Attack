#程序说明
本程序实现了ARP毒化攻击。

#文件说明
- `victimB/simple_server`：靶机B运行的http服务器代码
- `attackerA/ARP/ARP.py`：攻击机A运行的ARP毒化代码
- `attackerA/mitmproxy/attack.py`：攻击机A运行的窃听以及修改http流量的代码

#运行
##靶机B
```
cd simple_server
npm start
```

###依赖
- node.js
- express

##攻击机A
###终端1
设置IP转发以及端口映射：

```
sudo sysctl -w net.ipv4.ip_forward=1		
sudo iptables -t nat -F						
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 8080
```
启动mtimdump代理：

```
mitmdump -s attack.py -T
```


###终端2
启动ARP毒化脚本：

```
sudo python ARP.py
```

注：运行前需在ARP.py中设置攻击机网卡名、靶机B的ip、靶机C的ip。







