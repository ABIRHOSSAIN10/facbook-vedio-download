#cradit darkhunter141
import sys,os,wget
import  requests 
import re
os.system("rm -rf Hom.mp4")
logo="""\033[1;94m
  ______ ____     __      ________ _____ _____ ____   
 |  ____|  _ \    \ \    / /  ____|  __ \_   _/ __ \  
 | |__  | |_) |____\ \  / /| |__  | |  | || || |  | | 
 |  __| |  _ <______\ \/ / |  __| | |  | || || |  | | 
 | |    | |_) |      \  /  | |____| |__| || || |__| | 
 |_|    |____/        \/   |______|_____/_____\____/  
                                                       
                  Author:Abir hossain                                                  
"""
os.system("clear")
print()
print(logo)
gonten = os.path.join('Hom.mp4')
local = '\x1b[2K'
helaw=input("\033[1;92m FB Video Link: \033[1;93m ")
os.system("clear")
print(logo)
print("\033[1;93m[1] SD vedio")
print()
print("\033[1;93m[2] HD vedio")
print()
sop=input("\033[1;91mEnter option :")
if sop=='1':
    try:
        him = helaw
        Ak = requests.get(him)
        sdvideo_url = re.search('sd_src:"(.+?)"', Ak.text)[1]
    except requests.ConnectionError as e:
        print("Connection Error.")
    except TypeError:
        print("Video May Private or hd not avilable")  
    else:
        vala = sdvideo_url.replace('sd_src:"', '')
        print("\n")
        print("\033[1;95mQuality:\033[1;96m " +vala)
        print(" Started Downloading")
        wget.download(vala, gonten)
        sys.stdout.write(local)
        os.system('mv Hom.mp4 /sdcard')
        print()
        print("vedio downloaded")
        exit()
if sop=='2':
    try:
        him = helaw
        Ak = requests.get(him)
        hdvideo_url = re.search('hd_src:"(.+?)"', Ak.text)[1]
    except requests.ConnectionError as e:
        print("Connection Error.")
    except TypeError:
        print("Video Private or sd not avilable")
    else:
        jop = hdvideo_url.replace('hd_src:"', '')
        print("\n")
        print("\033[1;93mQuality:\033[1;93m " + jop)
        print("Started Downloading.....")
        wget.download(jop, gonten)
        sys.stdout.write(local)
        os.system('mv Hom.mp4 /sdcard')
        print()
        print("vedio downloaded")
        exit()
else:
    print("inviled")