import keyboard
import ctypes
import time
from subprocess import call
import sys
from os.path import join
from os import getcwd

cfgF = open(join(getcwd(),'cfg.txt'),'r')#load cfg
cfg = dict([i.split(';') for i in cfgF.read().split('\n')])
cfgF.close()

scF = open(join(getcwd(),'shortcuts.txt'),'r')#load shortcuts
sc = dict([i.split(';') for i in scF.read().split('\n')])
scF.close()
try:
    while True:
        time.sleep(0.05)
        for i in sc.keys():
            if keyboard.is_pressed(i):
                call(sc[i])
        try:
            if keyboard.is_pressed(cfg['exitkey']):
                ctypes.windll.user32.MessageBoxW(0, "Shortcutter closed.", "Shortcutter", 16 | 4096)
                sys.exit(0)
                
        except KeyError:
            pass
        if round(time.time()) % 5 == 0:
            cfgF = open(join(getcwd(),'cfg.txt'),'r')#load cfg
            cfg = dict([i.split(';') for i in cfgF.read().split('\n')])
            cfgF.close()

            scF = open(join(getcwd(),'shortcuts.txt'),'r')#load shortcuts
            sc = dict([i.split(';') for i in scF.read().split('\n')])
            scF.close()
except:
    print(sys.exc_info())
        
