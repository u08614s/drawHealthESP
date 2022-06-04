import socket
import time
import webbrowser,sys,subprocess
import math
import os

with open("connect2ip.txt") as f:
    ip=f.read()
    f.close()

address=0x409F000
code=""
offset=0

popen = subprocess.Popen('assemble\\build.bat',shell=True)
popen.wait()

with open("assemble\\asm",'rb') as f:
    tmp=f.read()
    f.close()
tmp=tmp.hex().upper()
time.sleep(0.1)

s=[]
for x in range(math.floor(len(tmp)/8)):
    s.append(tmp[x*8:x*8+8])
    
for x in range(len(s)):
    code=code+(format(address+offset,'08X')+" "+s[x][0:8])+"\n"
    offset=offset+4

code=code[:-1]

with open("scripts\\main",'w') as f:
    f.write(code)
    f.close()

print("接続しています...")
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,7331))
print(ip+"に接続しました")

sends=[]
with open("scripts\\Reset") as f:
    sends=f.readlines()
    f.close()
with open("scripts\\main") as f:
    sends=sends+f.readlines()
    f.close()
with open("scripts\\Run") as f:
    sends=sends+f.readlines()
    f.close()
for x in range(len(sends)):
    if(sends[x]!="\n"):
        s.send(bytes.fromhex('03'))
        s.send(bytes.fromhex(sends[x].replace("\n","")))
s.close()
print("送信が完了したので切断しました")
print("5秒後に終了します")
time.sleep(5)
