import os, sys
from win32com.client import GetObject
import psutil

def main():
    print("Type 'find_keylogger' <---")

    f = findKeylogger()
    
    if f == 0:
        print("You are safe!")
    else:
        ans = input("Do you want to quit keylogger?(Y/N): ")
        if ans == 'Y':
            killkeylogger(f)
        else:
            return 0

    return 0
        

def getProcessesList():
    PROCESSES_LIST_ = []
    getObj_ = GetObject('winmgmts:')
    processes_ = getObj_.instancesOf('Win32_Process')
    for ps_ in processes_:
        PROCESSES_LIST_.append(ps_.Properties_('Name').Value)
    return PROCESSES_LIST_

def findKeylogger():
    PROCESSES_LIST_ = getProcessesList()

    for ps_ in PROCESSES_LIST_
        tmppath = os.path.abspath(ps_)
        for file in os.listdir(tmppath.parent):
            if file.endswith(".txt"):
                fp_ = open(file, 'r')
                document_ = fp_.read()

                if 'find_keylogger' in document_:
                    print("Find keylogger!")
                    return tmppath
                else:
                    return 0

                fp_.close()

                
def killkeylogger(process):

    killProcessName = process
    for ps_ in psutil.process_iter():
        for kpn in killProcessName:
            if ps_.name() == kpn:
                print ps_.kill
