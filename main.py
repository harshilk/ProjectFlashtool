import subprocess
import tkinter as tk
import tkinter.font as tkFont
import webbrowser
import os.path
from pathlib import Path
from shutil import copyfile

ver = '2.5'

class HomePage:
    def __init__(self, root):
        #pyinstaller --onefile -w -F -i "C:/Users/Admin/Downloads/flash.ico" main.py
        # setting title
        root.title("Flashtool // realme 7 Pro")
        root.configure(background='#000000')
        #root.iconbitmap("C:/Users/hkosa/Downloads/flash.ico")
        # setting window size
        width = 900
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        TKLabel_578 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=58)
        TKLabel_578["font"] = ft
        TKLabel_578.configure(background="#000000")
        TKLabel_578.configure(foreground="#ffd700")
        TKLabel_578["justify"] = "center"
        TKLabel_578["text"] = "Realme 7 Pro Flashtool"
        TKLabel_578.place(x=0, y=20, width=900, height=80)

        TKLabel_801 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKLabel_801["font"] = ft
        TKLabel_801.configure(background="#000000")
        TKLabel_801.configure(foreground="#ffd700")
        TKLabel_801["justify"] = "center"
        TKLabel_801["text"] = " by Harshil Kosambi   "
        TKLabel_801.place(x=0, y=110, width=900, height=25)

        version = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=10)
        version["font"] = ft
        version.configure(background="#000000")
        version.configure(foreground="#b7b7b7")
        version["justify"] = "center"
        version["text"] = "V"+ver
        version.place(x=20, y=460, width=50, height=30)

        TKLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKLabel_885["font"] = ft
        TKLabel_885["justify"] = "center"
        TKLabel_885.configure(background="#000000")
        TKLabel_885.configure(foreground="#ffd700")

        TKLabel_885["text"] = "Please select any option to Continue"
        TKLabel_885.place(x=0, y=130, width=900, height=25)

        TKButton_532 = tk.Button(root)
        TKButton_532["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_532["font"] = ft
        TKButton_532.bd=0
        TKButton_532["fg"] = "#000000"
        TKButton_532["justify"] = "center"
        TKButton_532["text"] = "Download Firmware"
        TKButton_532.place(x=150, y=210, width=150, height=35)
        TKButton_532["command"] = self.TKButton_532_command

        TKButton_537 = tk.Button(root)
        TKButton_537["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_537["font"] = ft
        TKButton_537["fg"] = "#000000"
        TKButton_537["justify"] = "center"
        TKButton_537["text"] = "Custom Recovery"
        TKButton_537.place(x=150, y=270, width=150, height=35)
        TKButton_537["command"] = self.TKButton_537_command

        TKButton_729 = tk.Button(root)
        TKButton_729["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_729["font"] = ft
        TKButton_729["fg"] = "#000000"
        TKButton_729["justify"] = "center"
        TKButton_729["text"] = "Stock Recovery"
        TKButton_729.place(x=150, y=330, width=150, height=35)
        TKButton_729["command"] = self.TKButton_729_command

        TKButton_207 = tk.Button(root)
        TKButton_207["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_207["font"] = ft
        TKButton_207["fg"] = "#000000"
        TKButton_207["justify"] = "center"
        TKButton_207["text"] = "Root"
        TKButton_207.place(x=380, y=210, width=150, height=35)
        TKButton_207["command"] = self.TKButton_207_command

        TKButton_297 = tk.Button(root)
        TKButton_297["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_297["font"] = ft
        TKButton_297["fg"] = "#000000"
        TKButton_297["justify"] = "center"
        TKButton_297["text"] = "Unlock Bootloader"
        TKButton_297.place(x=380, y=270, width=150, height=35)
        TKButton_297["command"] = self.TKButton_297_command

        TKButton_87 = tk.Button(root)
        TKButton_87["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_87["font"] = ft
        TKButton_87["fg"] = "#000000"
        TKButton_87["justify"] = "center"
        TKButton_87["text"] = "Change Region"
        TKButton_87.place(x=380, y=330, width=150, height=35)
        TKButton_87["command"] = self.TKButton_87_command

        TKButton_942 = tk.Button(root)
        TKButton_942["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_942["font"] = ft
        TKButton_942["fg"] = "#000000"
        TKButton_942["justify"] = "center"
        TKButton_942["text"] = "Unbrick"
        TKButton_942.place(x=600, y=210, width=150, height=35)
        TKButton_942["command"] = self.TKButton_942_command

        TKButton_973 = tk.Button(root)
        TKButton_973["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_973["font"] = ft
        TKButton_973["fg"] = "#000000"
        TKButton_973["justify"] = "center"
        TKButton_973["text"] = "Stock Boot"
        TKButton_973.place(x=600, y=270, width=150, height=35)
        TKButton_973["command"] = self.TKButton_973_command

        TKButton_886 = tk.Button(root)
        TKButton_886["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_886["font"] = ft
        TKButton_886["fg"] = "#000000"
        TKButton_886["justify"] = "center"
        TKButton_886["text"] = "Reboot"
        TKButton_886.place(x=600, y=330, width=150, height=35)
        TKButton_886["command"] = self.TKButton_886_command




        TKButton_253 = tk.Button(root)
        TKButton_253["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_253["font"] = ft
        TKButton_253["fg"] = "#000000"
        TKButton_253["justify"] = "center"
        TKButton_253["text"] = "Check for updates"
        TKButton_253.place(x=700, y=440, width=150, height=35)
        TKButton_253["command"] = self.TKButton_253_command

    # Download firmware
    def TKButton_532_command(self):
        print("Download firmware")
        clear_frame()
        app = download_firmware(root)

    # Custom Recovery
    def TKButton_537_command(self):
        clear_frame()
        app = recovery(root)

    # Stock Recovery
    def TKButton_729_command(self):
        clear_frame()
        app = stock_recovery(root)

    #  Root
    def TKButton_207_command(self):

        clear_frame()
        app = root_page(root)

    #  Unlock Bootloader
    def TKButton_297_command(self):
        clear_frame()
        app = unlock(root)
       # os.system('cmd /k "@echo off && cd C:/flashtool/temp/flash && fastboot flashing unlock && fastboot reboot && echo Unlocked Successfully && PAUSE"')

    # chnage region
    def TKButton_87_command(self):
        os.system('cmd /c "@echo off && echo will be added in future updates && PAUSE"')
    # Unbrick
    def TKButton_942_command(self):
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
    def TKButton_973_command(self):
        clear_frame()
        app = boot(root)



    # Reboot
    def TKButton_886_command(self):
        os.system('cmd /c "@echo off && cd C:/flashtool/temp/flash && fastboot reboot && echo REBOOTED && PAUSE"')

    # updates
    def TKButton_253_command(self):

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

        TKLabel_578 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=58)
        TKLabel_578["font"] = ft
        TKLabel_578.configure(background="#000000")
        TKLabel_578.configure(foreground="#ffd700")
        TKLabel_578["justify"] = "center"
        TKLabel_578["text"] = "Download Firmware"
        TKLabel_578.place(x=0, y=20, width=900, height=79)

        TKLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKLabel_885["font"] = ft
        TKLabel_885.configure(background="#000000")
        TKLabel_885.configure(foreground="#ffd700")
        TKLabel_885["justify"] = "center"
        TKLabel_885["text"] = "Please select any option to Continue"
        TKLabel_885.place(x=0, y=130, width=900, height=25)

        TKButton_532 = tk.Button(root)
        TKButton_532["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_532["font"] = ft
        TKButton_532["fg"] = "#000000"
        TKButton_532["justify"] = "center"
        TKButton_532["text"] = "A37"
        TKButton_532.place(x=200, y=210, width=120, height=25)
        TKButton_532["command"] = self.TKButton_532_command

        TKButton_537 = tk.Button(root)
        TKButton_537["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_537["font"] = ft
        TKButton_537["fg"] = "#000000"
        TKButton_537["justify"] = "center"
        TKButton_537["text"] = "C20"
        TKButton_537.place(x=200, y=270, width=120, height=25)
        TKButton_537["command"] = self.TKButton_537_command

        TKButton_207 = tk.Button(root)
        TKButton_207["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_207["font"] = ft
        TKButton_207["fg"] = "#000000"
        TKButton_207["justify"] = "center"
        TKButton_207["text"] = "A39"
        TKButton_207.place(x=400, y=210, width=120, height=25)
        TKButton_207["command"] = self.TKButton_207_command

        TKButton_297 = tk.Button(root)
        TKButton_297["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_297["font"] = ft
        TKButton_297["fg"] = "#000000"
        TKButton_297["justify"] = "center"
        TKButton_297["text"] = "C22"
        TKButton_297.place(x=400, y=270, width=120, height=25)
        TKButton_297["command"] = self.TKButton_297_command

        TKButton_942 = tk.Button(root)
        TKButton_942["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_942["font"] = ft
        TKButton_942["fg"] = "#000000"
        TKButton_942["justify"] = "center"
        TKButton_942["text"] = "A41"
        TKButton_942.place(x=600, y=210, width=120, height=25)
        TKButton_942["command"] = self.TKButton_942_command

        TKButton_973 = tk.Button(root)
        TKButton_973["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_973["font"] = ft
        TKButton_973["fg"] = "#000000"
        TKButton_973["justify"] = "center"
        TKButton_973["text"] = "C23"
        TKButton_973.place(x=600, y=270, width=120, height=25)
        TKButton_973["command"] = self.TKButton_973_command

        TKButton_969 = tk.Button(root)
        TKButton_969["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_969["font"] = ft
        TKButton_969["fg"] = "#000000"
        TKButton_969["justify"] = "center"
        TKButton_969["text"] = "C24"
        TKButton_969.place(x=200, y=330, width=120, height=25)
        TKButton_969["command"] = self.TKButton_969_command

        TKButton_965 = tk.Button(root)
        TKButton_965["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_965["font"] = ft
        TKButton_965["fg"] = "#000000"
        TKButton_965["justify"] = "center"
        TKButton_965["text"] = "C25"
        TKButton_965.place(x=400, y=330, width=120, height=25)
        TKButton_965["command"] = self.TKButton_965_command

        TKButton_999 = tk.Button(root)
        TKButton_999["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_999["font"] = ft
        TKButton_999["fg"] = "#000000"
        TKButton_999["justify"] = "center"
        TKButton_999["text"] = "C26"
        TKButton_999.place(x=600, y=330, width=120, height=25)
        TKButton_999["command"] = self.TKButton_999_command

        TKButton_253 = tk.Button(root)
        TKButton_253["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_253["font"] = ft
        TKButton_253["fg"] = "#000000"
        TKButton_253["justify"] = "center"
        TKButton_253["text"] = "Go Back"
        TKButton_253.place(x=710, y=440, width=120, height=25)
        TKButton_253["command"] = self.TKButton_253_command


    # A37
    def TKButton_532_command(self):
        print("A37")
        webbrowser.open('https://download.c.realme.com/osupdate/RMX2170PU_11_OTA_0370_all_hricOIvzNDU1.ozip')

    # C20
    def TKButton_537_command(self):
        print("C19")
        webbrowser.open('https://drive.google.com/file/d/17GRd9Q9nLT_15AMUaXU3BfH5srYfgKar/view')

        #  A39

    def TKButton_207_command(self):
        print("A39")
        webbrowser.open('https://download.c.realme.com/osupdate/RMX2170PU_11_OTA_0390_all_GiyoeetxrwZG.ozip')

    #  C20
    def TKButton_297_command(self):
        print("C20")
        webbrowser.open('https://drive.google.com/file/d/1PgHtmwPoaHDE6AF8xXJ94_udGvw6TupO/view')

    # A41
    def TKButton_942_command(self):
        print("A41")
        webbrowser.open('https://download.c.realme.com/osupdate/RMX2170PU_11_OTA_0410_all_I1IugkGtNk13.ozip')

    # C23
    def TKButton_973_command(self):
        print("C23")
        webbrowser.open('https://drive.google.com/file/d/17JWsOdLnB3phZDR3H3zqGX9jY1p--PNT/view')

    # C24
    def TKButton_969_command(self):
        print("C24")
        webbrowser.open('https://drive.google.com/file/d/1KcYxA_NKv_WePsuYsTE3qHEUvril8Kcn/view')

    # C25
    def TKButton_965_command(self):
        print("C25")
        webbrowser.open('https://drive.google.com/file/d/12zGpPPtYvLN6r9vqlSkqiqOYREWNvHCM/view?usp=drivesdk')

    # C26
    def TKButton_999_command(self):
        print("C26")
        webbrowser.open('https://drive.google.com/u/0/uc?id=1mhJudyrILOJGXyZ-RSd78w-nMnWma6XM&export=download')

    # update
    def TKButton_253_command(self):
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

        TKLabel_578 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=58)
        TKLabel_578["font"] = ft
        TKLabel_578.configure(background="#000000")
        TKLabel_578.configure(foreground="#ffd700")
        TKLabel_578["justify"] = "center"
        TKLabel_578["text"] = "Stock Boot"
        TKLabel_578.place(x=0, y=20, width=900, height=79)

        TKLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKLabel_885["font"] = ft
        TKLabel_885.configure(background="#000000")
        TKLabel_885.configure(foreground="#ffd700")
        TKLabel_885["justify"] = "center"
        TKLabel_885["text"] = "Please select any option to Continue \nnote need to press button again after files get downloaded to flash"
        TKLabel_885.place(x=0, y=130, width=900, height=35)

        TKButton_532 = tk.Button(root)
        TKButton_532["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_532["font"] = ft
        TKButton_532["fg"] = "#000000"
        TKButton_532["justify"] = "center"
        TKButton_532["text"] = "A37"
        TKButton_532.place(x=200, y=210, width=120, height=25)
        TKButton_532["command"] = self.TKButton_532_command

        TKButton_537 = tk.Button(root)
        TKButton_537["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_537["font"] = ft
        TKButton_537["fg"] = "#000000"
        TKButton_537["justify"] = "center"
        TKButton_537["text"] = "C20"
        TKButton_537.place(x=200, y=270, width=120, height=25)
        TKButton_537["command"] = self.TKButton_537_command

        TKButton_207 = tk.Button(root)
        TKButton_207["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_207["font"] = ft
        TKButton_207["fg"] = "#000000"
        TKButton_207["justify"] = "center"
        TKButton_207["text"] = "A39"
        TKButton_207.place(x=400, y=210, width=120, height=25)
        TKButton_207["command"] = self.TKButton_207_command

        TKButton_297 = tk.Button(root)
        TKButton_297["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_297["font"] = ft
        TKButton_297["fg"] = "#000000"
        TKButton_297["justify"] = "center"
        TKButton_297["text"] = "C22"
        TKButton_297.place(x=400, y=270, width=120, height=25)
        TKButton_297["command"] = self.TKButton_297_command

        TKButton_942 = tk.Button(root)
        TKButton_942["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_942["font"] = ft
        TKButton_942["fg"] = "#000000"
        TKButton_942["justify"] = "center"
        TKButton_942["text"] = "A41"
        TKButton_942.place(x=600, y=210, width=120, height=25)
        TKButton_942["command"] = self.TKButton_942_command

        TKButton_973 = tk.Button(root)
        TKButton_973["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_973["font"] = ft
        TKButton_973["fg"] = "#000000"
        TKButton_973["justify"] = "center"
        TKButton_973["text"] = "C23"
        TKButton_973.place(x=600, y=270, width=120, height=25)
        TKButton_973["command"] = self.TKButton_973_command

        TKButton_428 = tk.Button(root)
        TKButton_428["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_428["font"] = ft
        TKButton_428["fg"] = "#000000"
        TKButton_428["justify"] = "center"
        TKButton_428["text"] = "C24"
        TKButton_428.place(x=200, y=330, width=120, height=25)
        TKButton_428["command"] = self.TKButton_428_command

        TKButton_449 = tk.Button(root)
        TKButton_449["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_449["font"] = ft
        TKButton_449["fg"] = "#000000"
        TKButton_449["justify"] = "center"
        TKButton_449["text"] = "C25"
        TKButton_449.place(x=400, y=330, width=120, height=25)
        TKButton_449["command"] = self.TKButton_449_command

        TKButton_477= tk.Button(root)
        TKButton_477["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_477["font"] = ft
        TKButton_477["fg"] = "#000000"
        TKButton_477["justify"] = "center"
        TKButton_477["text"] = "C26"
        TKButton_477.place(x=600, y=330, width=120, height=25)
        TKButton_477["command"] = self.TKButton_477_command

        TKButton_253 = tk.Button(root)
        TKButton_253["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_253["font"] = ft
        TKButton_253["fg"] = "#000000"
        TKButton_253["justify"] = "center"
        TKButton_253["text"] = "Go Back"
        TKButton_253.place(x=710, y=440, width=120, height=25)
        TKButton_253["command"] = self.TKButton_253_command

    # A37
    def TKButton_532_command(self):

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
    def TKButton_537_command(self):
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
    def TKButton_207_command(self):
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
    def TKButton_297_command(self):
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
    def TKButton_942_command(self):
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


    # C24

    def TKButton_428_command(self):

        if not os.path.isfile('C:/flashtool/boot/c24/boot_c24.img') and not os.path.isfile(
                'C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/boot/c24").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/boot/c24/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://www98.zippyshare.com/d/RNl5SVhm/46147/boot_c24.img"')
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c24/boot_c24.img", "a11.img",
                    "boot_c24.img")

        elif not os.path.isfile('C:/flashtool/boot/c24/boot_c24.img'):
            Path("C:/flashtool/boot/c24").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/boot/c24/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://www98.zippyshare.com/d/RNl5SVhm/46147/boot_c24.img"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c24/boot_c24.img", "a11.img",
                    "boot_c24.img")

        elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c24/boot_c24.img", "a11.img",
                    "boot_c24.img")

        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c24/boot_c24.img", "a11.img",
                    "boot_c24.img")

    # C23
    def TKButton_973_command(self):

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

    #C25
    def TKButton_449_command(self):

        if not os.path.isfile('C:/flashtool/boot/c25/boot_c25.img') and not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/boot/c25").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system('cmd /c "cd C:/flashtool/boot/c25/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://iweb.dl.sourceforge.net/project/ofoxrecovery/boot_c25.img"')
            os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c25/boot_c25.img", "a11.img",
                    "boot_c25.img")

        elif not os.path.isfile('C:/flashtool/boot/c25/boot_c25.img'):
            Path("C:/flashtool/boot/c25").mkdir(parents=True, exist_ok=True)
            os.system('cmd /c "cd C:/flashtool/boot/c25/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://iweb.dl.sourceforge.net/project/ofoxrecovery/boot_c25.img"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c25/boot_c25.img", "a11.img",
                    "boot_c25.img")

        elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c25/boot_c25.img", "a11.img",
                    "boot_c25.img")

        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c25/boot_c25.img", "a11.img",
                    "boot_c25.img")

    # C26
    def TKButton_477_command(self):

        if not os.path.isfile('C:/flashtool/boot/c26/boot_c26.img') and not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
               Path("C:/flashtool/boot/c26").mkdir(parents=True, exist_ok=True)
               Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
               os.system('cmd /c "cd C:/flashtool/boot/c26/ && C:/flashtool/bin/curl/bin/curl.exe -L -k -O https://master.dl.sourceforge.net/project/ofoxrecovery/boot_c26.img"')
               os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
               flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c26/boot_c26.img", "a11.img",
                            "boot_c26.img")

        elif not os.path.isfile('C:/flashtool/boot/c26/boot_c26.img'):
                    Path("C:/flashtool/boot/c26").mkdir(parents=True, exist_ok=True)
                    os.system(
                        'cmd /c "cd C:/flashtool/boot/c26/ && C:/flashtool/bin/curl/bin/curl.exe -L -k -O https://master.dl.sourceforge.net/project/ofoxrecovery/boot_c26.img"')
                    flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c26/boot_c26.img", "a11.img",
                            "boot_c26.img")

        elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
                    Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                    os.system(
                        'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
                    flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c26/boot_c26.img", "a11.img",
                            "boot_c26.img")

        else:
                    subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
                    os.system('cmd /c "PAUSE"')
                    flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/boot/c26/boot_c26.img", "a11.img",
                            "boot_c26.img")

    # go back
    def TKButton_253_command(self):
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

        TKLabel_578 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=58)
        TKLabel_578["font"] = ft
        TKLabel_578.configure(background="#000000")
        TKLabel_578.configure(foreground="#ffd700")
        TKLabel_578["justify"] = "center"
        TKLabel_578["text"] = "Rooting"
        TKLabel_578.place(x=0, y=20, width=900, height=90)

        TKLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKLabel_885["font"] = ft
        TKLabel_885.configure(background="#000000")
        TKLabel_885.configure(foreground="#ffd700")
        TKLabel_885["justify"] = "center"
        TKLabel_885["text"] = "Please select any option to Continue \nnote need to press button again after files get downloaded to flash"
        TKLabel_885.place(x=0, y=130, width=900, height=35)

        TKButton_532 = tk.Button(root)
        TKButton_532["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_532["font"] = ft
        TKButton_532["fg"] = "#000000"
        TKButton_532["justify"] = "center"
        TKButton_532["text"] = "A37"
        TKButton_532.place(x=100, y=210, width=120, height=25)
        TKButton_532["command"] = self.TKButton_532_command

        TKButton_537 = tk.Button(root)
        TKButton_537["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_537["font"] = ft
        TKButton_537["fg"] = "#000000"
        TKButton_537["justify"] = "center"
        TKButton_537["text"] = "C20"
        TKButton_537.place(x=700, y=210, width=120, height=25)
        TKButton_537["command"] = self.TKButton_537_command

        TKButton_207 = tk.Button(root)
        TKButton_207["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_207["font"] = ft
        TKButton_207["fg"] = "#000000"
        TKButton_207["justify"] = "center"
        TKButton_207["text"] = "A39"
        TKButton_207.place(x=300, y=210, width=120, height=25)
        TKButton_207["command"] = self.TKButton_207_command

        TKButton_297 = tk.Button(root)
        TKButton_297["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_297["font"] = ft
        TKButton_297["fg"] = "#000000"
        TKButton_297["justify"] = "center"
        TKButton_297["text"] = "C22"
        TKButton_297.place(x=100, y=270, width=120, height=25)
        TKButton_297["command"] = self.TKButton_297_command

        TKButton_942 = tk.Button(root)
        TKButton_942["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_942["font"] = ft
        TKButton_942["fg"] = "#000000"
        TKButton_942["justify"] = "center"
        TKButton_942["text"] = "A41"
        TKButton_942.place(x=500, y=210, width=120, height=25)
        TKButton_942["command"] = self.TKButton_942_command

        TKButton_973 = tk.Button(root)
        TKButton_973["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_973["font"] = ft
        TKButton_973["fg"] = "#000000"
        TKButton_973["justify"] = "center"
        TKButton_973["text"] = "C23"
        TKButton_973.place(x=300, y=270, width=120, height=25)
        TKButton_973["command"] = self.TKButton_973_command

        C24BUTTON = tk.Button(root)
        C24BUTTON["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        C24BUTTON["font"] = ft
        C24BUTTON["fg"] = "#000000"
        C24BUTTON["justify"] = "center"
        C24BUTTON["text"] = "C24"
        C24BUTTON.place(x=500, y=270, width=120, height=25)
        C24BUTTON["command"] = self.C24BUTTON_command

        TKButton_227 = tk.Button(root)
        TKButton_227["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_227["font"] = ft
        TKButton_227["fg"] = "#000000"
        TKButton_227["justify"] = "center"
        TKButton_227["text"] = "C25"
        TKButton_227.place(x=700, y=270, width=120, height=25)
        TKButton_227["command"] = self.TKButton_227_command

        TKButton_221 = tk.Button(root)
        TKButton_221["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_221["font"] = ft
        TKButton_221["fg"] = "#000000"
        TKButton_221["justify"] = "center"
        TKButton_221["text"] = "C26"
        TKButton_221.place(x=100, y=330, width=120, height=25)
        TKButton_221["command"] = self.TKButton_221_command


        TKButton_238 = tk.Button(root)
        TKButton_238["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_238["font"] = ft
        TKButton_238["fg"] = "#000000"
        TKButton_238["justify"] = "center"
        TKButton_238["text"] = "C27"
        TKButton_238.place(x=300, y=330, width=120, height=25)
        TKButton_238["command"] = self.TKButton_238_command

        TKButton_239 = tk.Button(root)
        TKButton_239["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_239["font"] = ft
        TKButton_239["fg"] = "#000000"
        TKButton_239["justify"] = "center"
        TKButton_239["text"] = "Go Back"
        TKButton_239.place(x=710, y=440, width=120, height=25)
        TKButton_239["command"] = self.TKButton_239_command



    # A37
    def TKButton_532_command(self):

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
    def TKButton_537_command(self):
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
    def TKButton_207_command(self):
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
    def TKButton_297_command(self):
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
    def TKButton_942_command(self):
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
    def TKButton_973_command(self):

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

    # C25
    def TKButton_227_command(self):

            if not os.path.isfile('C:/flashtool/root/c25/patched_c25.img') and not os.path.isfile(
                    'C:/flashtool/vbmeta/a11.img'):
                Path("C:/flashtool/root/c25").mkdir(parents=True, exist_ok=True)
                Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                os.system('cmd /c "cd C:/flashtool/root/c25/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/patched_c25.img"')
                os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
                os.system('cmd /c "PAUSE"')
                flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c25/patched_c25.img", "a11.img",
                        "patched_c25.img")

            elif not os.path.isfile('C:/flashtool/root/c25/patched_c25.img'):
                Path("C:/flashtool/root/c25").mkdir(parents=True, exist_ok=True)
                os.system('cmd /c "cd C:/flashtool/root/c25/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/patched_c25.img"')
                os.system('cmd /c "PAUSE"')
                flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c25/patched_c25.img", "a11.img",
                        "patched_c25.img")

            elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
                Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
                os.system('cmd /c "PAUSE"')
                flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c25/patched_c25.img", "a11.img",
                        "patched_c25.img")

            else:
                subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
                os.system('cmd /c "PAUSE"')
                flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c25/patched_c25.img", "a11.img",
                        "patched_c25.img")

            # C24

    def C24BUTTON_command(self):

        if not os.path.isfile('C:/flashtool/root/c24/patched_c24.img') and not os.path.isfile(
                'C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/root/c24").mkdir(parents=True, exist_ok=True)
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/root/c24/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/patched_c24.img"')
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c24/patched_c24.img", "a11.img",
                    "patched_c24.img")

        elif not os.path.isfile('C:/flashtool/root/c24/patched_c24.img'):
            Path("C:/flashtool/root/c24").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/root/c24/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/patched_c24.img"')
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c24/patched_c24.img", "a11.img",
                    "patched_c24.img")

        elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
            Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
            os.system(
                'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c24/patched_c24.img", "a11.img",
                    "patched_c24.img")

        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c24/patched_c24.img", "a11.img",
                    "patched_c24.img")

    # C26
    def TKButton_221_command(self):

     if not os.path.isfile('C:/flashtool/root/c26/patched_c26.img') and not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
        Path("C:/flashtool/root/c26").mkdir(parents=True, exist_ok=True)
        Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
        os.system('cmd /c "cd C:/flashtool/root/c26/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/patched_c26.img"')
        os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
        os.system('cmd /c "PAUSE"')
        flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c26/patched_c26.img", "a11.img",
                            "patched_c26.img")
     elif not os.path.isfile('C:/flashtool/root/c26/patched_c26.img'):
        Path("C:/flashtool/root/c26").mkdir(parents=True, exist_ok=True)
        os.system('cmd /c "cd C:/flashtool/root/c26/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/patched_c26.img"')
        os.system('cmd /c "PAUSE"')
        flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c26/patched_c26.img", "a11.img",
                            "patched_c26.img")
     elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
        Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
        os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
        os.system('cmd /c "PAUSE"')
        flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c26/patched_c26.img", "a11.img",
                "patched_c26.img")
     else:
        subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
        os.system('cmd /c "PAUSE"')
        flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c26/patched_c26.img", "a11.img",
                            "patched_c26.img")

    # C27

    def TKButton_238_command(self):

         if not os.path.isfile('C:/flashtool/root/c26/patched_c27.img') and not os.path.isfile(
                 'C:/flashtool/vbmeta/a11.img'):
             Path("C:/flashtool/root/c27").mkdir(parents=True, exist_ok=True)
             Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
             os.system(
                 'cmd /c "cd C:/flashtool/root/c26/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/patched_c27.img"')
             os.system(
                 'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
             os.system('cmd /c "PAUSE"')
             flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c27/patched_c27.img", "a11.img",
                     "patched_c27.img")
         elif not os.path.isfile('C:/flashtool/root/c27/patched_c27.img'):
             Path("C:/flashtool/root/c27").mkdir(parents=True, exist_ok=True)
             os.system(
                 'cmd /c "cd C:/flashtool/root/c27/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/patched_c27.img"')
             os.system('cmd /c "PAUSE"')
             flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c27/patched_c27.img", "a11.img",
                     "patched_c27.img")
         elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
             Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
             os.system(
                 'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
             os.system('cmd /c "PAUSE"')
             flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c27/patched_c27.img", "a11.img",
                     "patched_c27.img")
         else:
             subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
             os.system('cmd /c "PAUSE"')
             flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/root/c27/patched_c27.img", "a11.img",
                     "patched_c27.img")

    # go back
    def TKButton_239_command(self):
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

        TKLabel_578 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=58)
        TKLabel_578["font"] = ft
        TKLabel_578.configure(background="#000000")
        TKLabel_578.configure(foreground="#ffd700")
        TKLabel_578["justify"] = "center"
        TKLabel_578["text"] = "Custom Recovery"
        TKLabel_578.place(x=0, y=20, width=900, height=79)

        TKLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKLabel_885["font"] = ft
        TKLabel_885.configure(background="#000000")
        TKLabel_885.configure(foreground="#ffd700")
        TKLabel_885["justify"] = "center"
        TKLabel_885["text"] = "Please select any option to Continue"
        TKLabel_885.place(x=0, y=130, width=900, height=25)

        TKButton_532 = tk.Button(root)
        TKButton_532["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_532["font"] = ft
        TKButton_532["fg"] = "#000000"
        TKButton_532["justify"] = "center"
        TKButton_532["text"] = "Android 10"
        TKButton_532.place(x=150, y=210, width=120, height=25)
        TKButton_532["command"] = self.TKButton_532_command

        TKButton_537 = tk.Button(root)
        TKButton_537["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_537["font"] = ft
        TKButton_537["fg"] = "#000000"
        TKButton_537["justify"] = "center"
        TKButton_537["text"] = "Android 11 OFOX C25/C26"
        TKButton_537.place(x=450, y=210, width=170, height=25)
        TKButton_537["command"] = self.TKButton_537_command

        TKButton_569 = tk.Button(root)
        TKButton_569["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_569["font"] = ft
        TKButton_569["fg"] = "#000000"
        TKButton_569["justify"] = "center"
        TKButton_569["text"] = "Android 11 TWRP"
        TKButton_569.place(x=300, y=210, width=120, height=25)
        TKButton_569["command"] = self.TKButton_569_command

        TKButton_555 = tk.Button(root)
        TKButton_555["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_555["font"] = ft
        TKButton_555["fg"] = "#000000"
        TKButton_555["justify"] = "center"
        TKButton_555["text"] = "Android 11 OFOX C20"
        TKButton_555.place(x=650, y=210, width=170, height=25)
        TKButton_555["command"] = self.TKButton_555_command

        TKButton_585 = tk.Button(root)
        TKButton_585["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_585["font"] = ft
        TKButton_585["fg"] = "#000000"
        TKButton_585["justify"] = "center"
        TKButton_585["text"] = "Android 12 TWRP"
        TKButton_585.place(x=150, y=270, width=120, height=25)
        TKButton_585["command"] = self.TKButton_585_command

        TKButton_253 = tk.Button(root)
        TKButton_253["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_253["font"] = ft
        TKButton_253["fg"] = "#000000"
        TKButton_253["justify"] = "center"
        TKButton_253["text"] = "Go Back"
        TKButton_253.place(x=710, y=440, width=120, height=25)
        TKButton_253["command"] = self.TKButton_253_command

        # Android 10

    def TKButton_532_command(self):
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

    #OFOX v1
    def TKButton_537_command(self):
     if not os.path.isfile('C:/flashtool/recovery/ofox11-v1.img') and not os.path.isfile(
                    'C:/flashtool/vbmeta/a11.img'):
                Path("C:/flashtool/recovery").mkdir(parents=True, exist_ok=True)
                Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                os.system('cmd /c "PAUSE"')
                os.system('cmd /c "cd C:/flashtool/recovery/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://altushost-swe.dl.sourceforge.net/project/ofoxrecovery/ofox11-v1.img"')
                os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
                os.system('cmd /c "PAUSE"')
                re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/ofox11-v1.img", "a11.img",
                           "ofox11-v1.img")
     elif not os.path.isfile('C:/flashtool/recovery/ofox11-v1.img'):
                Path("C:/flashtool/recovery").mkdir(parents=True, exist_ok=True)

                os.system('cmd /c "cd C:/flashtool/recovery && C:/flashtool/bin/curl/bin/curl.exe -L -O https://altushost-swe.dl.sourceforge.net/project/ofoxrecovery/ofox11-v1.img"')
                os.system('cmd /c "PAUSE"')
                re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/ofox11-v1.img", "a11.img",
                           "ofox11-v1.img")
     elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
                Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
                os.system('cmd /c "PAUSE"')
                re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/ofox11-v1.img", "a11.img",
                           "ofox11-v1.img")
     else:
                subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
                os.system('cmd /c "PAUSE"')
                re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/ofox11-v1.img", "a11.img",
                           "ofox11-v1.img")

   #TWRP
    def TKButton_569_command(self):
     if not os.path.isfile('C:/flashtool/recovery/twrp11.img') and not os.path.isfile(
                    'C:/flashtool/vbmeta/a11.img'):
                Path("C:/flashtool/recovery").mkdir(parents=True, exist_ok=True)
                Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                os.system('cmd /c "PAUSE"')
                os.system(
                    'cmd /c "cd C:/flashtool/recovery/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://liquidtelecom.dl.sourceforge.net/project/ofoxrecovery/twrp11.img"')
                os.system(
                    'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
                os.system('cmd /c "PAUSE"')
                re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/twrp11.img", "a11.img",
                           "twrp11.img.img")
     elif not os.path.isfile('C:/flashtool/recovery/twrp11.img'):
                Path("C:/flashtool/recovery").mkdir(parents=True, exist_ok=True)

                os.system(
                    'cmd /c "cd C:/flashtool/recovery && C:/flashtool/bin/curl/bin/curl.exe -L -O https://liquidtelecom.dl.sourceforge.net/project/ofoxrecovery/twrp11.img"')
                os.system('cmd /c "PAUSE"')
                re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/twrp11.img", "a11.img",
                           "twrp11.img")
     elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
                Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                os.system(
                    'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
                os.system('cmd /c "PAUSE"')
                re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/twrp11.img", "a11.img",
                           "twrp11.img")
     else:
                subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
                os.system('cmd /c "PAUSE"')
                re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/twrp11.img", "a11.img",
                           "twrp11.img")

    # OFOX c20
    def TKButton_555_command(self):
         if not os.path.isfile('C:/flashtool/recovery/ofox11.img') and not os.path.isfile(
                 'C:/flashtool/vbmeta/a11.img'):
             Path("C:/flashtool/recovery").mkdir(parents=True, exist_ok=True)
             Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
             os.system('cmd /c "PAUSE"')
             os.system('cmd /c "cd C:/flashtool/recovery/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://iweb.dl.sourceforge.net/project/ofoxrecovery/ofox11.img"')
             os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
             os.system('cmd /c "PAUSE"')
             re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/ofox11.img", "a11.img",
                        "ofox11.img")
         elif not os.path.isfile('C:/flashtool/recovery/ofox11.img'):
             Path("C:/flashtool/recovery").mkdir(parents=True, exist_ok=True)
             os.system('cmd /c "cd C:/flashtool/recovery && C:/flashtool/bin/curl/bin/curl.exe -L -O https://iweb.dl.sourceforge.net/project/ofoxrecovery/ofox11.img"')
             os.system('cmd /c "PAUSE"')
             re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/ofox11.img", "a11.img",
                        "ofox11.img")
         elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
             Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
             os.system('cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
             os.system('cmd /c "PAUSE"')
             re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/ofox11.img", "a11.img",
                        "ofox11.img")
         else:
             subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
             os.system('cmd /c "PAUSE"')
             re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/ofox11.img", "a11.img",
                        "ofox11.img")


   # OFOX c20

    def TKButton_585_command(self):
             if not os.path.isfile('C:/flashtool/recovery/TWRP-3.5.2_1112-BETA-RMX2170.img') and not os.path.isfile(
                     'C:/flashtool/vbmeta/a11.img'):
                 Path("C:/flashtool/recovery").mkdir(parents=True, exist_ok=True)
                 Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                 os.system('cmd /c "PAUSE"')
                 os.system(
                     'cmd /c "cd C:/flashtool/recovery/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://master.dl.sourceforge.net/project/ofoxrecovery/TWRP-3.5.2_1112-BETA-RMX2170.img?"')
                 os.system(
                     'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
                 os.system('cmd /c "PAUSE"')
                 re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/TWRP-3.5.2_1112-BETA-RMX2170.img", "a11.img",
                            "TWRP-3.5.2_1112-BETA-RMX2170.img")
             elif not os.path.isfile('C:/flashtool/recovery/TWRP-3.5.2_1112-BETA-RMX2170.img'):
                 Path("C:/flashtool/recovery").mkdir(parents=True, exist_ok=True)
                 os.system(
                     'cmd /c "cd C:/flashtool/recovery && C:/flashtool/bin/curl/bin/curl.exe -L -O https://master.dl.sourceforge.net/project/ofoxrecovery/TWRP-3.5.2_1112-BETA-RMX2170.img"')
                 os.system('cmd /c "PAUSE"')
                 re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/TWRP-3.5.2_1112-BETA-RMX2170.img", "a11.img",
                            "TWRP-3.5.2_1112-BETA-RMX2170.img")
             elif not os.path.isfile('C:/flashtool/vbmeta/a11.img'):
                 Path("C:/flashtool/vbmeta").mkdir(parents=True, exist_ok=True)
                 os.system(
                     'cmd /c "cd C:/flashtool/vbmeta/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/a11.img"')
                 os.system('cmd /c "PAUSE"')
                 re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/TWRP-3.5.2_1112-BETA-RMX2170.img", "a11.img",
                            "TWRP-3.5.2_1112-BETA-RMX2170.img")
             else:
                 subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
                 os.system('cmd /c "PAUSE"')
                 re_flasher("C:/flashtool/vbmeta/a11.img", "C:/flashtool/recovery/TWRP-3.5.2_1112-BETA-RMX2170.img", "a11.img",
                            "TWRP-3.5.2_1112-BETA-RMX2170.img")

        #  go back
    def TKButton_253_command(self):
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

        TKLabel_578 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=58)
        TKLabel_578["font"] = ft
        TKLabel_578.configure(background="#000000")
        TKLabel_578.configure(foreground="#ffd700")
        TKLabel_578["justify"] = "center"
        TKLabel_578["text"] = "Stock Recovery"
        TKLabel_578.place(x=0, y=20, width=900, height=79)

        TKLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKLabel_885["font"] = ft
        TKLabel_885.configure(background="#000000")
        TKLabel_885.configure(foreground="#ffd700")
        TKLabel_885["justify"] = "center"
        TKLabel_885["text"] = "Please select any option to Continue"
        TKLabel_885.place(x=0, y=130, width=900, height=25)

        TKButton_532 = tk.Button(root)
        TKButton_532["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_532["font"] = ft
        TKButton_532["fg"] = "#000000"
        TKButton_532["justify"] = "center"
        TKButton_532["text"] = "RUI 1"
        TKButton_532.place(x=280, y=210, width=120, height=25)
        TKButton_532["command"] = self.TKButton_532_command

        TKButton_537 = tk.Button(root)
        TKButton_537["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_537["font"] = ft
        TKButton_537["fg"] = "#000000"
        TKButton_537["justify"] = "center"
        TKButton_537["text"] = "RUI 2"
        TKButton_537.place(x=480, y=210, width=120, height=25)
        TKButton_537["command"] = self.TKButton_537_command

        TKButton_253 = tk.Button(root)
        TKButton_253["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_253["font"] = ft
        TKButton_253["fg"] = "#000000"
        TKButton_253["justify"] = "center"
        TKButton_253["text"] = "Go Back"
        TKButton_253.place(x=710, y=440, width=120, height=25)
        TKButton_253["command"] = self.TKButton_253_command

    # Android 10
    def TKButton_532_command(self):
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
    def TKButton_537_command(self):
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
    def TKButton_253_command(self):
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

        TKLabel_578 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=58)
        TKLabel_578["font"] = ft
        TKLabel_578.configure(background="#000000")
        TKLabel_578.configure(foreground="#ffd700")
        TKLabel_578["justify"] = "center"
        TKLabel_578["text"] = "Unlock Bootloader"
        TKLabel_578.place(x=0, y=20, width=900, height=79)

        TKLabel_885 = tk.Label(root)
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKLabel_885["font"] = ft
        TKLabel_885.configure(background="#000000")
        TKLabel_885.configure(foreground="#ffd700")
        TKLabel_885["justify"] = "center"
        TKLabel_885["text"] = "Please select any Deep testing then do unlock"
        TKLabel_885.place(x=0, y=130, width=900, height=25)

        TKButton_532 = tk.Button(root)
        TKButton_532["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_532["font"] = ft
        TKButton_532["fg"] = "#000000"
        TKButton_532["justify"] = "center"
        TKButton_532["text"] = "RUI 1"
        TKButton_532.place(x=200, y=210, width=120, height=25)
        TKButton_532["command"] = self.TKButton_532_command



        TKButton_537 = tk.Button(root)
        TKButton_537["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_537["font"] = ft
        TKButton_537["fg"] = "#000000"
        TKButton_537["justify"] = "center"
        TKButton_537["text"] = "RUI 2"
        TKButton_537.place(x=400, y=210, width=120, height=25)
        TKButton_537["command"] = self.TKButton_537_command


        TKButton_253 = tk.Button(root)
        TKButton_253["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_253["font"] = ft
        TKButton_253["fg"] = "#000000"
        TKButton_253["justify"] = "center"
        TKButton_253["text"] = "Go Back"
        TKButton_253.place(x=710, y=440, width=120, height=25)
        TKButton_253["command"] = self.TKButton_253_command

        TKButton_942 = tk.Button(root)
        TKButton_942["bg"] = "#ffd700"
        ft = tkFont.Font(family='Ubuntu', size=10)
        TKButton_942["font"] = ft
        TKButton_942["fg"] = "#000000"
        TKButton_942["justify"] = "center"
        TKButton_942["text"] = "Unlock Fastboot"
        TKButton_942.place(x=600, y=210, width=120, height=25)
        TKButton_942["command"] = self.TKButton_942_command

        # RUI 1

    def TKButton_532_command(self):
        if not os.path.isfile('C:/flashtool/temp/flash/rui1.apk'):
            os.system(
                'cmd /c "cd C:/flashtool/temp/flash/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/rui1.apk"')
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            os.system('cmd /c "@echo off && cd C:/flashtool/temp/flash/ && adb install rui1.apk && echo flashing done"')

        # Android 11

    def TKButton_537_command(self):
        if not os.path.isfile('C:/flashtool/temp/flash/rui2.apk'):
            os.system(
                'cmd /c "cd C:/flashtool/temp/flash/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/rui2.apk"')
        else:
            subprocess.call([r'C:/flashtool/bin/already_downloaded.bat'])
            os.system('cmd /c "PAUSE"')
            os.system('cmd /c "@echo off && cd C:/flashtool/temp/flash/ && adb install rui2.apk && echo flashing done"')

        #  go back
    def TKButton_253_command(self):
        print("go back")
        clear_frame()
        app = HomePage(root)

        # unbl
    def TKButton_942_command(self):
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

def debloater(pkgname:str):
    f = open("C:/flashtool/temp/flash/debloat.bat", "w+")
    f.write('@echo off\ncd C:/flashtool/temp/flash/\nadb devices\nadb shell pm uninstall -k --user 0 ' + str(pkgname) + '\necho Uninstalled Successfully\nPAUSE')
    f.close()
    subprocess.call([r'C:/flashtool/temp/flash/debloat.bat'])





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
