import os
try:
    from colorama import Fore, Back

except ModuleNotFoundError:
    os.system("pip instll colorama")


from colors import w , ran , y , c 
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
 ▄███▄▄▄▄██▀ ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀  </> Instagram : @Sunnam01ram 
▀▀███▀▀▀▀▀   ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀    </> Instagram : @Sprogram00
▀███████████ ███    ███ ███    ███   ███    █▄  ▀███████████  </> Github: sunnamsriram1
  ███    ███ ███    ███ ███    ███   ███    ███   ███    ███ 
  ███    ███  ▀██████▀   ▀██████▀    ██████████   ███    ███ 
  ███    ███                                      ███    ███ 
  
                                    </>Author:Sunnam Sriram
  """

from random import choice


for i in logo:
    col = choice([Fore.RED , Fore.GREEN , Fore.CYAN , Fore.LIGHTWHITE_EX , Fore.MAGENTA , Fore.BLUE])

    print(col + i , end="")
