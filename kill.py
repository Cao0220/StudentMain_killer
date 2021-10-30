'''
Copyright 2021, 2021 Andy Cao

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import os
import time

def gan_3():
    print("已进入娱乐模式……\n按 Ctrl+C 或 直接关闭程序窗口 以退出\n*^____^*\n")
    while True:
        print("正在挂起",end="\r")
        b=os.system("pssuspend64.exe"+" "+str(pid.pid))
        if b==0 :
            print("挂起成功，约60秒后恢复",end="\r")
            print("                                ",end="\r")
            for i in range(6000):
                print("██ "*(i//600), end = '')
                print("█ "*(i//300-2*(i//600)), format(i/60,".2f"), "%\r", end = '')
                time.sleep(0.01)
            print('██ '*10+'                ',end="\r")
        b=os.system("pssuspend64.exe"+" "+str(pid.pid)+' -r')
        print("正在恢复",end="\r")
        time.sleep(0.1)

def gan(oid,name):
    pids = psutil.process_iter()
    print("[" + name + "]'s pid is:")
    for pid in pids:
        if(pid.name() == name):
            print(pid.pid)
            time.sleep(15)
            b=1
            if oid=="1" :
                b=os.system("pssuspend64.exe"+" "+str(pid.pid))
            elif oid=="2" :
                b=os.system("pssuspend64.exe"+" "+str(pid.pid)+' -r')
            elif oid=="3" :
                gan_3()
            elif oid=="4" :
                b=os.system("taskkill -f -im StudentMain.exe")
    return b

def install_psutil(n):
    try:
        import psutil
    except: #ModuleNotFoundError
        print("psutil is not installed!")
        temp=os.system('py -m pip install psutil -i https://pypi.mirrors.ustc.edu.cn/simple/')
        # temp=os.system('start cmd /K py -m pip install psutil -i https://pypi.mirrors.ustc.edu.cn/simple/')
        if temp!=0 : print("执行失败")
        if temp==0 :print("安装完成:)")
        if n==0: exit()
        install_psutil(n-1)

try:
    import psutil
except:
    install_psutil(3)


while True :
    os.system("cls")
    print(
'''
      O)                       O))         
     O) ))                     O))         
    O)  O))     O)) O))        O)) O))   O))
   O))   O))     O))  O))  O)) O))  O)) O)) 
  O)))))) O))    O))  O)) O)   O))    O)))  
 O))       O))   O))  O)) O)   O))    O))  
O))         O)) O)))  O))  O)) O))   O))   
                                    O))     
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$Andy's project - StudentMain_killer
'''
    )
    a=""
    a=input(
'''
请输入命令代码：
    1. 挂起
    2. 取消挂起
    3. 娱乐模式
    4. 杀掉
    5. 退出
''')
    if a not in ["1","2","3","4"] :
        exit()
    back_id=-1
    while back_id!=0:
        back_id=gan(a,"StudentMain.exe")
input("请按任意键以退出……")