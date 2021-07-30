import subprocess
import tkinter as tk
import tkinter.font as tkFont
import webbrowser
import os.path
from pathlib import Path
from shutil import copyfile

ver = '2.0'

class HomePage:
    def __init__(self, root):
        #pyinstaller --onefile -w -F -i "C:/Users/Admin/Downloads/flash.ico" main.py
        # setting title
        root.title("Flashtool for Realme 7 pro")
        root.configure(background='#131313')
        #root.iconbitmap("C:/Users/hkosa/Downloads/flash.ico")
        # setting window size
        width = 900
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_578 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=58)
        GLabel_578["font"] = ft
        GLabel_578.configure(background="#131313")
        GLabel_578.configure(foreground="#00a3ff")
        GLabel_578["justify"] = "center"
        GLabel_578["text"] = "Realme 7 pro Flashtool"
        GLabel_578.place(x=0, y=20, width=900, height=80)

        GLabel_801 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=10)
        GLabel_801["font"] = ft
        GLabel_801.configure(background="#131313")
        GLabel_801.configure(foreground="#00a3ff")
        GLabel_801["justify"] = "center"
        GLabel_801["text"] = "by Harshil Kosambi"
        GLabel_801.place(x=0, y=110, width=900, height=25)

        version = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=10)
        version["font"] = ft
        version.configure(background="#131313")
        version.configure(foreground="#b7b7b7")
        version["justify"] = "center"
        version["text"] = "V"+ver
        version.place(x=20, y=460, width=50, height=30)

        GLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=10)
        GLabel_885["font"] = ft
        GLabel_885["justify"] = "center"
        GLabel_885.configure(background="#131313")
        GLabel_885.configure(foreground="#00a3ff")

        GLabel_885["text"] = "Please select any option to Continue"
        GLabel_885.place(x=0, y=130, width=900, height=25)

        GButton_532 = tk.Button(root)
        GButton_532["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_532["font"] = ft
        GButton_532.bd=0
        GButton_532["fg"] = "#131313"
        GButton_532["justify"] = "center"
        GButton_532["text"] = "Download Firmware"
        GButton_532.place(x=150, y=210, width=150, height=35)
        GButton_532["command"] = self.GButton_532_command

        GButton_537 = tk.Button(root)
        GButton_537["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_537["font"] = ft
        GButton_537["fg"] = "#131313"
        GButton_537["justify"] = "center"
        GButton_537["text"] = "Custom Recovery"
        GButton_537.place(x=150, y=270, width=150, height=35)
        GButton_537["command"] = self.GButton_537_command

        GButton_729 = tk.Button(root)
        GButton_729["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_729["font"] = ft
        GButton_729["fg"] = "#131313"
        GButton_729["justify"] = "center"
        GButton_729["text"] = "Stock Recovery"
        GButton_729.place(x=150, y=330, width=150, height=35)
        GButton_729["command"] = self.GButton_729_command

        GButton_207 = tk.Button(root)
        GButton_207["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_207["font"] = ft
        GButton_207["fg"] = "#131313"
        GButton_207["justify"] = "center"
        GButton_207["text"] = "Root"
        GButton_207.place(x=380, y=210, width=150, height=35)
        GButton_207["command"] = self.GButton_207_command

        GButton_297 = tk.Button(root)
        GButton_297["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_297["font"] = ft
        GButton_297["fg"] = "#131313"
        GButton_297["justify"] = "center"
        GButton_297["text"] = "Unlock Bootloader"
        GButton_297.place(x=380, y=270, width=150, height=35)
        GButton_297["command"] = self.GButton_297_command

        GButton_87 = tk.Button(root)
        GButton_87["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_87["font"] = ft
        GButton_87["fg"] = "#131313"
        GButton_87["justify"] = "center"
        GButton_87["text"] = "Change Region"
        GButton_87.place(x=380, y=330, width=150, height=35)
        GButton_87["command"] = self.GButton_87_command

        GButton_942 = tk.Button(root)
        GButton_942["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_942["font"] = ft
        GButton_942["fg"] = "#131313"
        GButton_942["justify"] = "center"
        GButton_942["text"] = "Unbrick"
        GButton_942.place(x=600, y=210, width=150, height=35)
        GButton_942["command"] = self.GButton_942_command

        GButton_973 = tk.Button(root)
        GButton_973["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_973["font"] = ft
        GButton_973["fg"] = "#131313"
        GButton_973["justify"] = "center"
        GButton_973["text"] = "Stock Boot"
        GButton_973.place(x=600, y=270, width=150, height=35)
        GButton_973["command"] = self.GButton_973_command

        GButton_886 = tk.Button(root)
        GButton_886["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_886["font"] = ft
        GButton_886["fg"] = "#131313"
        GButton_886["justify"] = "center"
        GButton_886["text"] = "Reboot"
        GButton_886.place(x=600, y=330, width=150, height=35)
        GButton_886["command"] = self.GButton_886_command

        GButton_253 = tk.Button(root)
        GButton_253["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_253["font"] = ft
        GButton_253["fg"] = "#131313"
        GButton_253["justify"] = "center"
        GButton_253["text"] = "Check for updates"
        GButton_253.place(x=700, y=440, width=150, height=35)
        GButton_253["command"] = self.GButton_253_command

    # Download firmware
    def GButton_532_command(self):
        print("Download firmware")
        clear_frame()
        app = download_firmware(root)

    # Custom Recovery
    def GButton_537_command(self):
        clear_frame()
        app = recovery(root)

    # Stock Recovery
    def GButton_729_command(self):
        clear_frame()
        app = stock_recovery(root)

    #  Root
    def GButton_207_command(self):

        clear_frame()
        app = root_page(root)

    #  Unlock Bootloader
    def GButton_297_command(self):
        clear_frame()
        app = unlock(root)
       # os.system('cmd /k "@echo off && cd C:/flashtool/temp/flash && fastboot flashing unlock && fastboot reboot && echo Unlocked Successfully && PAUSE"')

    # chnage region
    def GButton_87_command(self):
        os.system('cmd /c "@echo off && echo will be added in future updates && PAUSE"')
    # Unbrick
    def GButton_942_command(self):
        if len(os.listdir('C:/flashtool/firmware')) == 0:
            subprocess.call([r'C:/flashtool/firmware/super.bat'])

        else:
            if os.path.isfile('C:/flashtool/firmware/super.img') and os.path.isfile('C:/flashtool/firmware/flash.bat') :
                    f = open("C:/flashtool/temp/flash/flash.bat", "w+")
                    f.write(
                        '@echo off\necho Process will take sometime so sit back and relax...\ncd C:/flashtool/temp/flash\nfastboot flash super C:/flashtool/firmware/super.img\necho Flashing Successful\nFlash custom recovery android 11 and flash any stock.ozip, format data and reboot\nPAUSE')
                    f.close()
                    subprocess.call([r'C:/flashtool/temp/flash/flash.bat'])
            else:
                subprocess.call([r'C:/flashtool/firmware/super.bat'])

    # Stock Boot
    def GButton_973_command(self):
        clear_frame()
        app = boot(root)

    # Reboot
    def GButton_886_command(self):
        os.system('cmd /c "@echo off && cd C:/flashtool/temp/flash && fastboot reboot && echo REBOOTED && PAUSE"')

    # updates
    def GButton_253_command(self):

        if not os.path.isfile('C:/flashtool/temp/v.txt'):
            Path("C:/flashtool/temp/").mkdir(parents=True, exist_ok=True)
            os.system('cmd /c "cd C:/flashtool/temp/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/v.txt"')
            updater_script()

        else:
            os.system('cmd /c "cd C:/flashtool/temp/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/v.txt"')
            updater_script()

def updater_script():
    lat = open('C:/flashtool/temp/v.txt', 'r').read()
    pre = open('C:/flashtool/bin/v', 'r').read()

    a= int(lat)
    b=int(pre)
    print(a)
    print(b)
    if a>b:
       os.startfile('C:/flashtool/bin/updater.exe')
       root.destroy()
    else:
       os.system('cmd /c "@echo off && echo Already Latest.... press anything to continue && pause >null""')

class download_firmware:
    def __init__(self, root):
        # setting title
        root.title("Flashtool")
        # setting window size
        width = 900
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_578 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=58)
        GLabel_578["font"] = ft
        GLabel_578.configure(background="#131313")
        GLabel_578.configure(foreground="#00a3ff")
        GLabel_578["justify"] = "center"
        GLabel_578["text"] = "Download Firmware"
        GLabel_578.place(x=0, y=20, width=900, height=79)

        GLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=10)
        GLabel_885["font"] = ft
        GLabel_885.configure(background="#131313")
        GLabel_885.configure(foreground="#00a3ff")
        GLabel_885["justify"] = "center"
        GLabel_885["text"] = "Please select any option to Continue"
        GLabel_885.place(x=0, y=130, width=900, height=25)

        GButton_532 = tk.Button(root)
        GButton_532["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_532["font"] = ft
        GButton_532["fg"] = "#131313"
        GButton_532["justify"] = "center"
        GButton_532["text"] = "A37"
        GButton_532.place(x=200, y=210, width=120, height=25)
        GButton_532["command"] = self.GButton_532_command

        GButton_537 = tk.Button(root)
        GButton_537["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_537["font"] = ft
        GButton_537["fg"] = "#131313"
        GButton_537["justify"] = "center"
        GButton_537["text"] = "C20"
        GButton_537.place(x=200, y=270, width=120, height=25)
        GButton_537["command"] = self.GButton_537_command

        GButton_207 = tk.Button(root)
        GButton_207["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_207["font"] = ft
        GButton_207["fg"] = "#131313"
        GButton_207["justify"] = "center"
        GButton_207["text"] = "A39"
        GButton_207.place(x=400, y=210, width=120, height=25)
        GButton_207["command"] = self.GButton_207_command

        GButton_297 = tk.Button(root)
        GButton_297["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_297["font"] = ft
        GButton_297["fg"] = "#131313"
        GButton_297["justify"] = "center"
        GButton_297["text"] = "C22"
        GButton_297.place(x=400, y=270, width=120, height=25)
        GButton_297["command"] = self.GButton_297_command

        GButton_942 = tk.Button(root)
        GButton_942["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_942["font"] = ft
        GButton_942["fg"] = "#131313"
        GButton_942["justify"] = "center"
        GButton_942["text"] = "A41"
        GButton_942.place(x=600, y=210, width=120, height=25)
        GButton_942["command"] = self.GButton_942_command

        GButton_973 = tk.Button(root)
        GButton_973["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_973["font"] = ft
        GButton_973["fg"] = "#131313"
        GButton_973["justify"] = "center"
        GButton_973["text"] = "C23"
        GButton_973.place(x=600, y=270, width=120, height=25)
        GButton_973["command"] = self.GButton_973_command

        GButton_253 = tk.Button(root)
        GButton_253["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_253["font"] = ft
        GButton_253["fg"] = "#131313"
        GButton_253["justify"] = "center"
        GButton_253["text"] = "Go Back"
        GButton_253.place(x=710, y=440, width=120, height=25)
        GButton_253["command"] = self.GButton_253_command

    # A37
    def GButton_532_command(self):
        print("A37")
        webbrowser.open('https://download.c.realme.com/osupdate/RMX2170PU_11_OTA_0370_all_hricOIvzNDU1.ozip')

    # C20
    def GButton_537_command(self):
        print("C19")
        webbrowser.open('https://drive.google.com/file/d/17GRd9Q9nLT_15AMUaXU3BfH5srYfgKar/view')

        #  A39

    def GButton_207_command(self):
        print("A39")
        webbrowser.open('https://download.c.realme.com/osupdate/RMX2170PU_11_OTA_0390_all_GiyoeetxrwZG.ozip')

    #  C20
    def GButton_297_command(self):
        print("C20")
        webbrowser.open('https://drive.google.com/file/d/1PgHtmwPoaHDE6AF8xXJ94_udGvw6TupO/view')

    # A41
    def GButton_942_command(self):
        print("A41")
        webbrowser.open('https://download.c.realme.com/osupdate/RMX2170PU_11_OTA_0410_all_I1IugkGtNk13.ozip')

    # C23
    def GButton_973_command(self):
        print("C22")
        webbrowser.open('https://drive.google.com/file/d/17JWsOdLnB3phZDR3H3zqGX9jY1p--PNT/view')

    # updates
    def GButton_253_command(self):
        print("go back")
        clear_frame()
        app = HomePage(root)

class boot:
    def __init__(self, root):
        # setting title
        root.title("Flashtool")
        # setting window size
        width = 900
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_578 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=58)
        GLabel_578["font"] = ft
        GLabel_578.configure(background="#131313")
        GLabel_578.configure(foreground="#00a3ff")
        GLabel_578["justify"] = "center"
        GLabel_578["text"] = "Stock Boot"
        GLabel_578.place(x=0, y=20, width=900, height=79)

        GLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=10)
        GLabel_885["font"] = ft
        GLabel_885.configure(background="#131313")
        GLabel_885.configure(foreground="#00a3ff")
        GLabel_885["justify"] = "center"
        GLabel_885["text"] = "Please select any option to Continue \nnote need to press button again after files get downloaded to flash"
        GLabel_885.place(x=0, y=130, width=900, height=35)

        GButton_532 = tk.Button(root)
        GButton_532["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_532["font"] = ft
        GButton_532["fg"] = "#131313"
        GButton_532["justify"] = "center"
        GButton_532["text"] = "A37"
        GButton_532.place(x=200, y=210, width=120, height=25)
        GButton_532["command"] = self.GButton_532_command

        GButton_537 = tk.Button(root)
        GButton_537["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_537["font"] = ft
        GButton_537["fg"] = "#131313"
        GButton_537["justify"] = "center"
        GButton_537["text"] = "C20"
        GButton_537.place(x=200, y=270, width=120, height=25)
        GButton_537["command"] = self.GButton_537_command

        GButton_207 = tk.Button(root)
        GButton_207["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_207["font"] = ft
        GButton_207["fg"] = "#131313"
        GButton_207["justify"] = "center"
        GButton_207["text"] = "A39"
        GButton_207.place(x=400, y=210, width=120, height=25)
        GButton_207["command"] = self.GButton_207_command

        GButton_297 = tk.Button(root)
        GButton_297["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_297["font"] = ft
        GButton_297["fg"] = "#131313"
        GButton_297["justify"] = "center"
        GButton_297["text"] = "C22"
        GButton_297.place(x=400, y=270, width=120, height=25)
        GButton_297["command"] = self.GButton_297_command

        GButton_942 = tk.Button(root)
        GButton_942["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_942["font"] = ft
        GButton_942["fg"] = "#131313"
        GButton_942["justify"] = "center"
        GButton_942["text"] = "A41"
        GButton_942.place(x=600, y=210, width=120, height=25)
        GButton_942["command"] = self.GButton_942_command

        GButton_973 = tk.Button(root)
        GButton_973["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_973["font"] = ft
        GButton_973["fg"] = "#131313"
        GButton_973["justify"] = "center"
        GButton_973["text"] = "C23"
        GButton_973.place(x=600, y=270, width=120, height=25)
        GButton_973["command"] = self.GButton_973_command

        GButton_253 = tk.Button(root)
        GButton_253["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_253["font"] = ft
        GButton_253["fg"] = "#131313"
        GButton_253["justify"] = "center"
        GButton_253["text"] = "Go Back"
        GButton_253.place(x=710, y=440, width=120, height=25)
        GButton_253["command"] = self.GButton_253_command

    # A37
    def GButton_532_command(self):

        if not os.path.isfile('C:/flashtool/boot/a37/boota37.img') and not os.path.isfile(
                'C:/flashtool/vbmeta/a10.img'):
            Path("C:/flashtool/boot/a37").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)

            os.system(
                'cmd /c "cd C:/flashtool/boot/a37/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/boota37.img"')
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')

            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/boot/a37/boota37.img", "a10.img",
                    "boota37.img")
        elif not os.path.isfile('C:/flashtool/boot/a37/boota37.img'):
            Path("C:/flashtool/boot/a37").mkdir(parents=True, exist_ok=True)

            os.system(
                'cmd /c "cd C:/flashtool/boot/a37/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/boota37.img"')

            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/boot/a37/boota37.img", "a10.img",
                    "boota37.img")
        elif not os.path.isfile('C:/flashtool/vbmeta/a10.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')

            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/boot/a37/boota37.img", "a10.img",
                    "boota37.img")
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])

            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/boot/a37/boota37.img", "a10.img",
                    "boota37.img")
    # C20
    def GButton_537_command(self):
        if not os.path.isfile('C:/flashtool/boot/c20/bootc20.img') and not os.path.isfile(
                'C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/boot/c20").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)

            os.system(
                'cmd /c "cd C:/flashtool/boot/c20/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/bootc20.img"')
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')

            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c20/bootc20.img", "a11.img",
                    "bootc20.img")
        elif not os.path.isfile('C:/flashtool/boot/c20/bootc20.img'):
            Path("C:/flashtool/boot/c20").mkdir(parents=True, exist_ok=True)

            os.system(
                'cmd /c "cd C:/flashtool/boot/c20/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/bootc20.img"')

            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c20/bootc20.img", "a11.img",
                    "bootc20.img")
        elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')

            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c20/bootc20.img", "a11.img",
                    "bootc20.img")
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])

            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c20/bootc20.img", "a11.img",
                    "boot20.img")

    #  A39
    def GButton_207_command(self):
        if not os.path.isfile('C:/flashtool/boot/a39/boota39.img') and not os.path.isfile(
                'C:/flashtool/vbmeta/a10.img'):
            Path("C:/flashtool/boot/a39").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)

            os.system(
                'cmd /c "cd C:/flashtool/boot/a39/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/boota39.img"')
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')

            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/boot/a39/boota39.img", "a10.img",
                    "boota39.img")
        elif not os.path.isfile('C:/flashtool/boot/a39/boota39.img'):
            Path("C:/flashtool/boot/a39").mkdir(parents=True, exist_ok=True)

            os.system(
                'cmd /c "cd C:/flashtool/boot/a39/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/boota39.img"')

            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/boot/a39/boota39.img", "a10.img",
                    "boota39.img")
        elif not os.path.isfile('C:/flashtool/vbmeta/a10.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')
            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/boot/a39/boota39.img", "a10.img",
                    "boota39.img")
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/boot/a39/boota39.img", "a10.img",
                    "boota39.img")

    #  C22
    def GButton_297_command(self):
        if not os.path.isfile('C:/flashtool/boot/c22/bootc22.img') and not os.path.isfile(
                'C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/boot/c22").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/boot/c22/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/bootc22.img"')
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c22/bootc22.img", "a11.img",
                    "bootc22.img")
        elif not os.path.isfile('C:/flashtool/boot/c22/bootc22.img'):
            Path("C:/flashtool/boot/c22").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/boot/c22/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/bootc22.img"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c22/bootc22.img", "a11.img",
                    "bootc22.img")
        elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/bootc22.img"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c22/bootc22.img", "a11.img", "bootc22.img")
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            flasher( "C:/flashtool/vbmeta/a11.img","C:/flashtool/boot/c22/boot.img", "a11.img", "bootc22.img")

    # A41
    def GButton_942_command(self):
            if not os.path.isfile('C:/flashtool/boot/a41/boota41.img') and not os.path.isfile(
                    'C:/flashtool/vbmeta/a10.img'):
                Path("C:/flashtool/boot/a41").mkdir(parents=True, exist_ok=True)
                Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                os.system(
                    'cmd /c "cd C:/flashtool/boot/a41/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/boota41.img"')
                os.system(
                    'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')

                flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/boot/a41/boota41.img", "a10.img",
                        "boota41.img")
            elif not os.path.isfile('C:/flashtool/boot/a41/boota41.img'):
                Path("C:/flashtool/boot/a41").mkdir(parents=True, exist_ok=True)

                os.system(
                    'cmd /c "cd C:/flashtool/boot/a41/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/boota41.img"')
                os.system('cmd /c "PAUSE"')
                flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/boot/a41/boota41.img", "a10.img",
                        "boota41.img")
            elif not os.path.isfile('C:/flashtool/vbmeta/a10.img'):
                Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                os.system(
                    'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')
                os.system('cmd /c "PAUSE"')
                flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/boot/a41/boota41.img", "a10.img",
                        "boota41.img")
            else:
                subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
                flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/boot/a41/boota41.img", "a10.img",
                        "boota41.img")

    # C23
    def GButton_973_command(self):

        if not os.path.isfile('C:/flashtool/boot/c23/bootc23.img') and not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
                Path("C:/flashtool/boot/c23").mkdir(parents=True, exist_ok=True)
                Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                os.system('cmd /c "cd C:/flashtool/boot/c23/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/bootc23.img"')
                os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
                flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c23/bootc23.img", "a11.img",
                        "bootc23.img")

        elif not os.path.isfile('C:/flashtool/boot/c23/bootc23.img'):
                Path("C:/flashtool/boot/c23").mkdir(parents=True, exist_ok=True)
                os.system('cmd /c "cd C:/flashtool/boot/c23/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/bootc23.img"')
                flasher("C:/flashtool/vbmeta/a11.img","C:/flashtool/boot/c23/bootc23.img", "a11.img", "bootc23.img")

        elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
                 Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                 os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
                 flasher("C:/flashtool/vbmeta/a11.img","C:/flashtool/boot/c23/bootc23.img", "a11.img", "bootc23.img")

        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a11.img","C:/flashtool/boot/c23/bootc23.img", "a11.img", "bootc23.img")



    # go back
    def GButton_253_command(self):
        print("go back")
        clear_frame()
        app = HomePage(root)

class root_page:
    def __init__(self, root):
        # setting title
        root.title("Flashtool")
        # setting window size
        width = 900
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_578 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=58)
        GLabel_578["font"] = ft
        GLabel_578.configure(background="#131313")
        GLabel_578.configure(foreground="#00a3ff")
        GLabel_578["justify"] = "center"
        GLabel_578["text"] = "Rooting"
        GLabel_578.place(x=0, y=20, width=900, height=79)

        GLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=10)
        GLabel_885["font"] = ft
        GLabel_885.configure(background="#131313")
        GLabel_885.configure(foreground="#00a3ff")
        GLabel_885["justify"] = "center"
        GLabel_885["text"] = "Please select any option to Continue \nnote need to press button again after files get downloaded to flash"
        GLabel_885.place(x=0, y=130, width=900, height=35)

        GButton_532 = tk.Button(root)
        GButton_532["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_532["font"] = ft
        GButton_532["fg"] = "#131313"
        GButton_532["justify"] = "center"
        GButton_532["text"] = "A37"
        GButton_532.place(x=200, y=210, width=120, height=25)
        GButton_532["command"] = self.GButton_532_command

        GButton_537 = tk.Button(root)
        GButton_537["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_537["font"] = ft
        GButton_537["fg"] = "#131313"
        GButton_537["justify"] = "center"
        GButton_537["text"] = "C20"
        GButton_537.place(x=200, y=270, width=120, height=25)
        GButton_537["command"] = self.GButton_537_command

        GButton_207 = tk.Button(root)
        GButton_207["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_207["font"] = ft
        GButton_207["fg"] = "#131313"
        GButton_207["justify"] = "center"
        GButton_207["text"] = "A39"
        GButton_207.place(x=400, y=210, width=120, height=25)
        GButton_207["command"] = self.GButton_207_command

        GButton_297 = tk.Button(root)
        GButton_297["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_297["font"] = ft
        GButton_297["fg"] = "#131313"
        GButton_297["justify"] = "center"
        GButton_297["text"] = "C22"
        GButton_297.place(x=400, y=270, width=120, height=25)
        GButton_297["command"] = self.GButton_297_command

        GButton_942 = tk.Button(root)
        GButton_942["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_942["font"] = ft
        GButton_942["fg"] = "#131313"
        GButton_942["justify"] = "center"
        GButton_942["text"] = "A41"
        GButton_942.place(x=600, y=210, width=120, height=25)
        GButton_942["command"] = self.GButton_942_command

        GButton_973 = tk.Button(root)
        GButton_973["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_973["font"] = ft
        GButton_973["fg"] = "#131313"
        GButton_973["justify"] = "center"
        GButton_973["text"] = "C23"
        GButton_973.place(x=600, y=270, width=120, height=25)
        GButton_973["command"] = self.GButton_973_command

        GButton_253 = tk.Button(root)
        GButton_253["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_253["font"] = ft
        GButton_253["fg"] = "#131313"
        GButton_253["justify"] = "center"
        GButton_253["text"] = "Go Back"
        GButton_253.place(x=710, y=440, width=120, height=25)
        GButton_253["command"] = self.GButton_253_command

    # A37
    def GButton_532_command(self):

        if not os.path.isfile('C:/flashtool/root/a37/patched_a37.img') and not os.path.isfile(
                'C:/flashtool/vbmeta/a10.img'):
            Path("C:/flashtool/root/a37").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system('cmd /c "PAUSE"')
            os.system(
                'cmd /c "cd C:/flashtool/root/a37/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/patched_a37.img"')
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/root/a37/patched_a37.img", "a10.img",
                    "patched_a37.img")
        elif not os.path.isfile('C:/flashtool/root/a37/patched_a37.img'):
            Path("C:/flashtool/root/a37").mkdir(parents=True, exist_ok=True)

            os.system(
                'cmd /c "cd C:/flashtool/root/a37/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/patched_a37.img"')
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/root/a37/patched_a37.img", "a10.img",
                    "patched_a37.img")
        elif not os.path.isfile('C:/flashtool/vbmeta/a10.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/root/a37/patched_a37.img", "a10.img",
                    "patched_a37.img")
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/root/a37/patched_a37.img", "a10.img",
                    "patched_a37.img")
    # C20
    def GButton_537_command(self):
        if not os.path.isfile('C:/flashtool/root/c20/patched_c20.img') and not os.path.isfile(
                'C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/root/c20").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system('cmd /c "PAUSE"')
            os.system(
                'cmd /c "cd C:/flashtool/root/c20/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/patched_c20.img"')
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c20/patched_c20.img", "a11.img",
                    "patched_c20.img")
        elif not os.path.isfile('C:/flashtool/root/c20/patched_c20.img'):
            Path("C:/flashtool/root/c20").mkdir(parents=True, exist_ok=True)

            os.system(
                'cmd /c "cd C:/flashtool/root/c20/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/patched_c20.img"')
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c20/patched_c20.img", "a11.img",
                    "patched_c20.img")
        elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c20/patched_c20.img", "a11.img",
                    "patched_c20.img")
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c20/patched_c20.img", "a11.img",
                    "patched_c20.img")

    #  A39
    def GButton_207_command(self):
        if not os.path.isfile('C:/flashtool/root/a39/patched_a39.img') and not os.path.isfile(
                'C:/flashtool/vbmeta/a10.img'):
            Path("C:/flashtool/root/a39").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system('cmd /c "PAUSE"')
            os.system(
                'cmd /c "cd C:/flashtool/root/a39/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/patched_a39.img"')
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/root/a39/patched_a39.img", "a10.img",
                    "patched_a39.img")
        elif not os.path.isfile('C:/flashtool/root/a39/patched_a39.img'):
            Path("C:/flashtool/root/a39").mkdir(parents=True, exist_ok=True)

            os.system(
                'cmd /c "cd C:/flashtool/root/a39/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/patched_a39.img"')
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/root/a39/patched_a39.img", "a10.img",
                    "patched_a39.img")
        elif not os.path.isfile('C:/flashtool/vbmeta/a10.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/root/a39/patched_a39.img", "a10.img",
                    "patched_a39.img")
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/root/a39/patched_a39.img", "a10.img",
                    "patched_a39.img")

    #  C22
    def GButton_297_command(self):
        if not os.path.isfile('C:/flashtool/root/c22/patched_c22.img') and not os.path.isfile(
                'C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/root/c22").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system('cmd /c "PAUSE"')
            os.system(
                'cmd /c "cd C:/flashtool/root/c22/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/patched_c22.img"')
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c22/patched_c22.img", "a11.img",
                    "patched_c22.img")
        elif not os.path.isfile('C:/flashtool/root/c22/patched_c22.img'):
            Path("C:/flashtool/root/c22").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/root/c22/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/patched_c22.img"')
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c22/patched_c22.img", "a11.img",
                    "patched_c22.img")
        elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c22/patched_c22.img", "a11.img", "patched_c22.img")
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            flasher( "C:/flashtool/vbmeta/a11.img","C:/flashtool/root/c22/patched_c22.img", "a11.img", "patched_c22.img")

    # A41
    def GButton_942_command(self):
            if not os.path.isfile('C:/flashtool/root/a41/patched_a41.img') and not os.path.isfile(
                    'C:/flashtool/vbmeta/a10.img'):
                Path("C:/flashtool/root/a41").mkdir(parents=True, exist_ok=True)
                Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                os.system('cmd /c "PAUSE"')
                os.system(
                    'cmd /c "cd C:/flashtool/root/a41/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/patched_a41.img"')
                os.system(
                    'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')
                os.system('cmd /c "PAUSE"')
                flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/root/a41/patched_a41.img", "a10.img",
                        "patched_a41.img")
            elif not os.path.isfile('C:/flashtool/root/a41/patched_a41.img'):
                Path("C:/flashtool/root/a41").mkdir(parents=True, exist_ok=True)

                os.system(
                    'cmd /c "cd C:/flashtool/root/a41/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/patched_a41.img"')
                os.system('cmd /c "PAUSE"')
                flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/root/a41/patched_a41.img", "a10.img",
                        "patched_a41.img")
            elif not os.path.isfile('C:/flashtool/vbmeta/a10.img'):
                Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                os.system(
                    'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')
                os.system('cmd /c "PAUSE"')
                flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/root/a41/patched_a41.img", "a10.img",
                        "patched_a41.img")
            else:
                subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
                os.system('cmd /c "PAUSE"')
                flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/root/a41/patched_a41.img", "a10.img",
                        "patched_a41.img")

    # C23
    def GButton_973_command(self):

        if not os.path.isfile('C:/flashtool/root/c23/patched_c23.img') and not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
                Path("C:/flashtool/root/c23").mkdir(parents=True, exist_ok=True)
                Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                os.system('cmd /c "cd C:/flashtool/root/c23/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/patched_c23.img"')
                os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
                os.system('cmd /c "PAUSE"')
                flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c23/patched_c23.img", "a11.img",
                        "patched_c23.img")

        elif not os.path.isfile('C:/flashtool/root/c23/patched_c23.img'):
                Path("C:/flashtool/root/c23").mkdir(parents=True, exist_ok=True)
                os.system('cmd /c "cd C:/flashtool/root/c23/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/patched_c23.img"')
                os.system('cmd /c "PAUSE"')
                flasher("C:/flashtool/vbmeta/a11.img","C:/flashtool/root/c23/patched_c23.img", "a11.img", "patched_c23.img")

        elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
                 Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                 os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
                 os.system('cmd /c "PAUSE"')
                 flasher("C:/flashtool/vbmeta/a11.img","C:/flashtool/root/c23/patched_c23.img", "a11.img", "patched_c23.img")

        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a11.img","C:/flashtool/root/c23/patched_c23.img", "a11.img", "patched_c23.img")



    # go back
    def GButton_253_command(self):
        print("go back")
        clear_frame()
        app = HomePage(root)

class recovery:
    def __init__(self, root):
        # setting title
        root.title("Flashtool")
        # setting window size
        width = 900
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_578 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=58)
        GLabel_578["font"] = ft
        GLabel_578.configure(background="#131313")
        GLabel_578.configure(foreground="#00a3ff")
        GLabel_578["justify"] = "center"
        GLabel_578["text"] = "Custom Recovery"
        GLabel_578.place(x=0, y=20, width=900, height=79)

        GLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=10)
        GLabel_885["font"] = ft
        GLabel_885.configure(background="#131313")
        GLabel_885.configure(foreground="#00a3ff")
        GLabel_885["justify"] = "center"
        GLabel_885["text"] = "Please select any option to Continue"
        GLabel_885.place(x=0, y=130, width=900, height=25)

        GButton_532 = tk.Button(root)
        GButton_532["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_532["font"] = ft
        GButton_532["fg"] = "#131313"
        GButton_532["justify"] = "center"
        GButton_532["text"] = "Android 10"
        GButton_532.place(x=200, y=210, width=120, height=25)
        GButton_532["command"] = self.GButton_532_command

        GButton_537 = tk.Button(root)
        GButton_537["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_537["font"] = ft
        GButton_537["fg"] = "#131313"
        GButton_537["justify"] = "center"
        GButton_537["text"] = "Android 11"
        GButton_537.place(x=400, y=210, width=120, height=25)
        GButton_537["command"] = self.GButton_537_command

        GButton_253 = tk.Button(root)
        GButton_253["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_253["font"] = ft
        GButton_253["fg"] = "#131313"
        GButton_253["justify"] = "center"
        GButton_253["text"] = "Go Back"
        GButton_253.place(x=710, y=440, width=120, height=25)
        GButton_253["command"] = self.GButton_253_command

        # Android 10

    def GButton_532_command(self):
        if not os.path.isfile('C:/flashtool/recovery/ofox10.img') and not os.path.isfile(
                'C:/flashtool/vbmeta/a10.img'):
            Path("C:/flashtool/recovery").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system('cmd /c "PAUSE"')
            os.system(
                'cmd /c "cd C:/flashtool/recovery/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/ofox10.img"')
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')
            os.system('cmd /c "PAUSE"')
            re_flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/recovery/ofox10.img", "a10.img",
                    "ofox10.img.img")
        elif not os.path.isfile('C:/flashtool/recovery/ofox10.img'):
            Path("C:/flashtool/recovery").mkdir(parents=True, exist_ok=True)

            os.system(
                'cmd /c "cd C:/flashtool/recovery && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/ofox10.img"')
            os.system('cmd /c "PAUSE"')
            re_flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/recovery/ofox10.img", "a10.img",
                    "ofox10.img")
        elif not os.path.isfile('C:/flashtool/vbmeta/a10.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')
            os.system('cmd /c "PAUSE"')
            re_flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/recovery/ofox10.img", "a10.img",
                    "ofox10.img")
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            re_flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/recovery/ofox10.img", "a10.img",
                    "ofox10.img")

        # Android 11

    def GButton_537_command(self):
        if not os.path.isfile('C:/flashtool/recovery/ofox11.img') and not os.path.isfile(
                'C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/recovery").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system('cmd /c "PAUSE"')
            os.system(
                'cmd /c "cd C:/flashtool/recovery/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/ofox11.img"')
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            os.system('cmd /c "PAUSE"')
            re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/ofox11.img", "a11.img",
                       "ofox11.img.img")
        elif not os.path.isfile('C:/flashtool/recovery/ofox11.img'):
            Path("C:/flashtool/recovery").mkdir(parents=True, exist_ok=True)

            os.system(
                'cmd /c "cd C:/flashtool/recovery && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/ofox11.img"')
            os.system('cmd /c "PAUSE"')
            re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/ofox11.img", "a11.img",
                       "ofox11.img")
        elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            os.system('cmd /c "PAUSE"')
            re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/ofox11.img", "a11.img",
                       "ofox11.img")
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/ofox11.img", "a11.img",
                       "ofox11.img")

        #  go back
    def GButton_253_command(self):
        print("go back")
        clear_frame()
        app = HomePage(root)

class stock_recovery:
    def __init__(self, root):
        # setting title
        root.title("Flashtool")
        # setting window size
        width = 900
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_578 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=58)
        GLabel_578["font"] = ft
        GLabel_578.configure(background="#131313")
        GLabel_578.configure(foreground="#00a3ff")
        GLabel_578["justify"] = "center"
        GLabel_578["text"] = "Stock Recovery"
        GLabel_578.place(x=0, y=20, width=900, height=79)

        GLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=10)
        GLabel_885["font"] = ft
        GLabel_885.configure(background="#131313")
        GLabel_885.configure(foreground="#00a3ff")
        GLabel_885["justify"] = "center"
        GLabel_885["text"] = "Please select any option to Continue"
        GLabel_885.place(x=0, y=130, width=900, height=25)

        GButton_532 = tk.Button(root)
        GButton_532["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_532["font"] = ft
        GButton_532["fg"] = "#131313"
        GButton_532["justify"] = "center"
        GButton_532["text"] = "RUI 1"
        GButton_532.place(x=200, y=210, width=120, height=25)
        GButton_532["command"] = self.GButton_532_command

        GButton_537 = tk.Button(root)
        GButton_537["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_537["font"] = ft
        GButton_537["fg"] = "#131313"
        GButton_537["justify"] = "center"
        GButton_537["text"] = "RUI 2"
        GButton_537.place(x=400, y=210, width=120, height=25)
        GButton_537["command"] = self.GButton_537_command

        GButton_253 = tk.Button(root)
        GButton_253["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_253["font"] = ft
        GButton_253["fg"] = "#131313"
        GButton_253["justify"] = "center"
        GButton_253["text"] = "Go Back"
        GButton_253.place(x=710, y=440, width=120, height=25)
        GButton_253["command"] = self.GButton_253_command

    # Android 10
    def GButton_532_command(self):
        if not os.path.isfile('C:/flashtool/stock/recovery/sr10.img') and not os.path.isfile(
                'C:/flashtool/vbmeta/a10.img'):
            Path("C:/flashtool/stock/recovery").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/stock/recovery/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/sr10.img"')
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')
            os.system('cmd /c "PAUSE"')
            re_flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/stock/recovery/sr10.img", "a10.img",
                    "sr10.img.img")
        elif not os.path.isfile('C:/flashtool/stock/recovery/sr10.img'):
            Path("C:/flashtool/stock/recovery").mkdir(parents=True, exist_ok=True)

            os.system(
                'cmd /c "cd C:/flashtool/stock/recovery && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/sr10.img"')
            re_flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/stock/recovery/sr10.img", "a10.img",
                    "sr10.img")
        elif not os.path.isfile('C:/flashtool/vbmeta/a10.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a10.img"')
            re_flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/stock/recovery/sr10.img", "a10.img",
                    "sr10.img")
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            re_flasher("C:/flashtool/vbmeta/a10.img", "C:/flashtool/stock/recovery/sr10.img", "a10.img",
                    "sr10.img")

    # Android 11
    def GButton_537_command(self):
        if not os.path.isfile('C:/flashtool/stock/recovery/sr11.img') and not os.path.isfile(
                'C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/stock/recovery").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/stock/recovery/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/sr11.img"')
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/stock/recovery/sr11.img", "a11.img",
                       "sr11.img.img")
        elif not os.path.isfile('C:/flashtool/stock/recovery/sr11.img'):
            Path("C:/flashtool/stock/recovery").mkdir(parents=True, exist_ok=True)

            os.system(
                'cmd /c "cd C:/flashtool/stock/recovery && C:/flashtool/bin/curl/bin/curl.exe -L -O https://dump.ultramayur.workers.dev/0:/Patched_img_R7P/sr11.img"')
            re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/stock/recovery/sr11.img", "a11.img",
                       "sr11.img")
        elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/stock/recovery/sr11.img", "a11.img",
                       "sr11.img")
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/stock/recovery/sr11.img", "a11.img",
                       "sr11.img")

        #  go back
    def GButton_253_command(self):
        print("go back")
        clear_frame()
        app = HomePage(root)

class unlock:
    def __init__(self, root):
        # setting title
        root.title("Flashtool")
        # setting window size
        width = 900
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_578 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=58)
        GLabel_578["font"] = ft
        GLabel_578.configure(background="#131313")
        GLabel_578.configure(foreground="#00a3ff")
        GLabel_578["justify"] = "center"
        GLabel_578["text"] = "Unlock Bootloader"
        GLabel_578.place(x=0, y=20, width=900, height=79)

        GLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Georgia', size=10)
        GLabel_885["font"] = ft
        GLabel_885.configure(background="#131313")
        GLabel_885.configure(foreground="#00a3ff")
        GLabel_885["justify"] = "center"
        GLabel_885["text"] = "Please select any Deep testing then do unlock"
        GLabel_885.place(x=0, y=130, width=900, height=25)

        GButton_532 = tk.Button(root)
        GButton_532["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_532["font"] = ft
        GButton_532["fg"] = "#131313"
        GButton_532["justify"] = "center"
        GButton_532["text"] = "RUI 1"
        GButton_532.place(x=200, y=210, width=120, height=25)
        GButton_532["command"] = self.GButton_532_command



        GButton_537 = tk.Button(root)
        GButton_537["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_537["font"] = ft
        GButton_537["fg"] = "#131313"
        GButton_537["justify"] = "center"
        GButton_537["text"] = "RUI 2"
        GButton_537.place(x=400, y=210, width=120, height=25)
        GButton_537["command"] = self.GButton_537_command


        GButton_253 = tk.Button(root)
        GButton_253["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_253["font"] = ft
        GButton_253["fg"] = "#131313"
        GButton_253["justify"] = "center"
        GButton_253["text"] = "Go Back"
        GButton_253.place(x=710, y=440, width=120, height=25)
        GButton_253["command"] = self.GButton_253_command

        GButton_942 = tk.Button(root)
        GButton_942["bg"] = "#00a3ff"
        ft = tkFont.Font(family='Georgia', size=10)
        GButton_942["font"] = ft
        GButton_942["fg"] = "#131313"
        GButton_942["justify"] = "center"
        GButton_942["text"] = "Unlock Fastboot"
        GButton_942.place(x=600, y=210, width=120, height=25)
        GButton_942["command"] = self.GButton_942_command

        # RUI 1

    def GButton_532_command(self):
        if not os.path.isfile('C:/flashtool/temp/flash/rui1.apk'):
            os.system(
                'cmd /c "cd C:/flashtool/temp/flash/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/rui1.apk"')
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            os.system('cmd /c "@echo off && cd C:/flashtool/temp/flash/ && adb install rui1.apk && echo flashing done"')

        # Android 11

    def GButton_537_command(self):
        if not os.path.isfile('C:/flashtool/temp/flash/rui2.apk'):
            os.system(
                'cmd /c "cd C:/flashtool/temp/flash/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/rui2.apk"')
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            os.system('cmd /c "@echo off && cd C:/flashtool/temp/flash/ && adb install rui2.apk && echo flashing done"')

        #  go back
    def GButton_253_command(self):
        print("go back")
        clear_frame()
        app = HomePage(root)

        # unbl
    def GButton_942_command(self):
        os.system('cmd /c "@echo off && echo have you approved from deep testing ? if not the do that fisrt then unlock && PAUSE')
        os.system('cmd /c "@echo off && cd C:/flashtool/temp/flash/ && fastboot flashing unlock && echo Unlocking Successful! && PAUSE"')

def flasher(addvb:str, addimg:str, vbname:str, imgname:str):

    if os.path.isfile('C:/flashtool/temp/flash/' + str(vbname)) and os.path.isfile('C:/flashtool/temp/flash/' + str(imgname)):
         f = open("C:/flashtool/temp/flash/flash.bat", "w+")
         f.write('@echo off\ncd C:/flashtool/temp/flash/\nfastboot --disable-verity --disable-verification flash vbmeta '+str(vbname)+'\nfastboot flash boot '+str(imgname)+'\nfastboot reboot\nDEL *.img\necho Flashing Successful\nPAUSE')
         f.close()
         subprocess.call([r'C:/flashtool/temp/flash/flash.bat'])
    else:
        copyfile(str(addvb), 'C:/flashtool/temp/flash/' + str(vbname))
        copyfile(str(addimg), 'C:/flashtool/temp/flash/' + str(imgname))
        f = open("C:/flashtool/temp/flash/flash.bat", "w+")
        f.write(
            '@echo off\ncd C:/flashtool/temp/flash/\nfastboot --disable-verity --disable-verification flash vbmeta ' + str(
                vbname) + '\nfastboot flash boot ' + str(
                imgname) + '\nfastboot reboot\nDEL *.img\necho Flashing Successful\nPAUSE')
        f.close()
        subprocess.call([r'C:/flashtool/temp/flash/flash.bat'])

def re_flasher(addvb:str, addimg:str, vbname:str, imgname:str):

    if os.path.isfile('C:/flashtool/temp/flash/' + str(vbname)) and os.path.isfile('C:/flashtool/temp/flash/' + str(imgname)):
         f = open("C:/flashtool/temp/flash/flash.bat", "w+")
         f.write('@echo off\ncd C:/flashtool/temp/flash/\nfastboot --disable-verity --disable-verification flash vbmeta '+str(vbname)+'\nfastboot flash boot '+str(imgname)+'\nfastboot reboot\nDEL *.img\necho Flashing Successful\nPAUSE')
         f.close()
         subprocess.call([r'C:/flashtool/temp/flash/flash.bat'])
    else:
        copyfile(str(addvb), 'C:/flashtool/temp/flash/' + str(vbname))
        copyfile(str(addimg), 'C:/flas'
                              'htool/temp/flash/' + str(imgname))
        f = open("C:/flashtool/temp/flash/flash.bat", "w+")
        f.write(
            '@echo off\ncd C:/flashtool/temp/flash/\nfastboot --disable-verity --disable-verification flash vbmeta ' + str(
                vbname) + '\nfastboot flash recovery ' + str(
                imgname) + '\nfastboot reboot\nDEL *.img\necho Flashing Successful\nPAUSE')
        f.close()
        subprocess.call([r'C:/flashtool/temp/flash/flash.bat'])

def clear_frame():
    for widgets in root.winfo_children():
        widgets.destroy()

def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

if __name__ == "__main__":
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()
