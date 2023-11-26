import os
import platform
from setup import colors
from setup.colors import r,g,y,c , w
from colorama import Fore , Back

GB = Back.GREEN
YB = Back.YELLOW
WB = Back.RED



logo = f"""
 ▄█     ▄███████▄                                            
███    ███    ███                                            
███▌   ███    ███                                            
███▌   ███    ███                                            
███▌ ▀█████████▀                                             
███    ███                                                   
███    ███                                                   
█▀    ▄████▀                                                 
                                                             
   ▄████████  ▄██████▄   ▄█    █▄     ▄████████    ▄████████ 
  ███    ███ ███    ███ ███    ███   ███    ███   ███    ███ 
  ███    ███ ███    ███ ███    ███   ███    █▀    ███    ███ 
 ▄███▄▄▄▄██▀ ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀  
▀▀███▀▀▀▀▀   ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀    
▀███████████ ███    ███ ███    ███   ███    █▄  ▀███████████ 
  ███    ███ ███    ███ ███    ███   ███    ███   ███    ███ 
  ███    ███  ▀██████▀   ▀██████▀    ██████████   ███    ███ 
  ███    ███                                      ███    ███ 
            {y}<{w}/{y}> {c}Author: {w}Saad Khan {r}|{g} Cyber-Dioxide    

{w}<{y}/{w}> {GB}{w}Instagram : @sunnam01ram {Back.RESET}
{w}<{y}/{w}> {YB}{w}Coding Instagram : Sprogram00 {Back.RESET}
{w}<{y}/{w}> {WB}{w}Github: sunnamsriram1 {Back.RESET}                                                                                                     
"""
c = colors
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")

def banner():
    print(c.ran + logo)



def banner2():


    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @sunnam01ram ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @Sprogram00 ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/sunnamsriram1 ", "- " * 3+c.ran + "|")
    print(c.ran + "\n"+ "|" + "*" * 60+c.ran + "|")

def clear():
    s = platform.platform()
    if "Windows" in s:
        os.system("cls")
    else:
        os.system("cls") if "Windows" in platform.platform() else os.system("clear")
