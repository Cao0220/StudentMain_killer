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
import msvcrt
import sys

def searchFile(Path, File):
    global back_path
    #获取当前路径下地所有文件
    allFile=os.listdir(Path)
    #对于每一个文件
    for eachFile in allFile:
        #若文件为一个文件夹
        if os.path.isdir(Path+os.sep+eachFile):
            #递归查找
            searchFile(Path+os.sep+eachFile, File)
        #如果是需要被查找的文件
        elif eachFile==File:
            #输出路径
            back_path=Path

def gan_3(pid):
    print("已进入娱乐模式……\n按 Ctrl+E 以退出\n按 Esc 以暂停\n*^____^*\n")
    c=0
    global back_path

    while True:
        time.sleep(0.5)
        b=os.system("pssuspend64.exe"+" "+str(pid))
        print("正在挂起",end="\r")
        if b==0 :
            print("挂起成功，约60秒后恢复",end="\r")
            print("                                ",end="\r")
            for i in range(6000):
                if msvcrt.kbhit():
                    # print(msvcrt.getch())
                    ch=msvcrt.getch()
                    if ch == b'\x1b': 
                        b=os.system("pssuspend64.exe"+" "+str(pid)+' -r')
                        while msvcrt.getch() != b'\x1b': 
                            b=os.system("pssuspend64.exe"+" "+str(pid)+' -r')
                            print('请按 Esc 以恢复')
                    if ch == b'\x05': 
                        b=os.system("pssuspend64.exe"+" "+str(pid)+' -r')
                        return 0
                    b=os.system("pssuspend64.exe"+" "+str(pid))
                
                print("██ "*(i//600), end = '')
                print("█ "*(i//300-2*(i//600)), format(i/60,".2f"),"%|",format(60-i//10/10,".1f"),"s lift" "\r", end = '')
                time.sleep(0.01)
            print('██ '*10+'                          ',end="\r")
        
        b=os.system("pssuspend64.exe"+" "+str(pid)+' -r')
        print("正在恢复",end="\r")

        os.system("taskkill -f -im StudentMain.exe")
        print("正在重置",end="\r")
        # os.system('"C:\Program Files (x86)\Mythware\极域电子教室软件 v4.0 2016 豪华版\StudentMain.exe"')
        os.system('start "" "'+back_path+'"')
        return 1
        
        # if msvcrt.kbhit():
        #     print(msvcrt.getch())
        #     if msvcrt.getch()== b'\x1b': 
        #         return(0)

def gan(oid,name):
    pids = psutil.process_iter()
    print("[" + name + "]'s pid is:")
    b=1
    for pid in pids:
        if(pid.name() == name):
            print(pid.pid)
            b=1
            if oid=="1" :
                b=os.system("pssuspend64.exe"+" "+str(pid.pid))
            elif oid=="2" :
                b=os.system("pssuspend64.exe"+" "+str(pid.pid)+' -r')
            elif oid=="3" :
                b=gan_3(pid.pid)
            elif oid=="4" :
                b=os.system("taskkill -f -im StudentMain.exe")
            elif oid=="5" :
                b=os.system('start "" "'+back_path+'"')
            #time.sleep(5)
    return b

def install_psutil(n):
    try:
        import psutil
    except: #ModuleNotFoundError
        print("psutil is not installed!")
        temp=os.system('py -m pip install psutil -i https://pypi.mirrors.ustc.edu.cn/simple/')
        # temp=os.system('start cmd /K py -m pip install psutil -i https://pypi.mirrors.ustc.edu.cn/simple/')
        if temp!=0 : print("执行失败")
        if temp==0 : 
            print("安装完成:)")
            os.execv(__file__, sys.argv)
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
''')

    a=input(
'''
请输入命令代码：
    1. 挂起
    2. 取消挂起
    3. 娱乐模式
    4. 杀掉
    5. 启动
    6. 退出
''')

    if a not in ["1","2","3","4","5"] :
        input("请按任意键以退出……")
        exit()

    back_path=""
    searchFile('C:\Program Files (x86)\Mythware', 'StudentMain.exe')
    back_path+="\StudentMain.exe"

    back_id=-1
    print('若出现弹窗，请点击运行\\同意')
    if a=='5':
        os.system('start "" "'+back_path+'"')
        continue

    while back_id!=0:
        back_id=gan(a,"StudentMain.exe")

input("请按任意键以退出……")