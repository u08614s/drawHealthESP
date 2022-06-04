import socket
import time
import webbrowser,sys,subprocess
import math
import os

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

sends=[]
with open("scripts\\Reset") as f:
    sends=f.readlines()
    f.close
with open("scripts\\main") as f:
    sends=sends+f.readlines()
    f.close
with open("scripts\\Run") as f:
    sends=sends+f.readlines()
    f.close
ss=""
for x in range(len(sends)):
    ss=ss+sends[x]+"\n"
print(ss.replace("\n\n","\n"))
input()
