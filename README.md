# Startup guide

**every command is with root privilages**

1. Start Controller:

ryu-manager main.py

2. Start mininet with remote controller
3. setup virtual interfaces

python3 veth-setup.py

4. start snort on h3
5. start alert realy on h3

python3 pingrelay.py

6. start http server and/or tcpdump on h2
7. start attack on h4 

hping3 -p 80 --flood 10.0.0.2
