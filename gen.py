from dhooks import Webhook
import random
import colorama
import time
import string
from colorama import Fore, init
init(convert=True)
text = """ _______ _____  _____ _____  _      ______          
|__   __|  __ \|_   _|  __ \| |    |  ____|   /\    
   | |  | |__) | | | | |__) | |    | |__     /  \   
   | |  |  _  /  | | |  ___/| |    |  __|   / /\ \  
   | |  | | \ \ _| |_| |    | |____| |____ / ____ \ 
   |_|  |_|  \_\_____|_|    |______|______/_/    \_\
   """
bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET', 'BLUE', 'GREEN', 'RED']
codes = vars(colorama.Fore)
colors = [codes[color] for color in codes if color not in bad_colors]
colored_lines = [random.choice(colors) + line for line in text.split('\n')]
print('\n'.join(colored_lines))
time.sleep(1)
hook = Webhook(input("\nInput your webhook link: "))
print(Fore.LIGHTYELLOW_EX + "")
cb = input("The codes will be classic or boost? c/b: ")
num = int(input("How many codes to send?: "))
if cb == ("c"):
        for i in range(num):
            code = "".join(random.choices(
                            string.ascii_uppercase + string.digits + string.ascii_lowercase,
                            k = 16
                        ))
            nitro = f"https://discord.gift/{code}"
            hook.send(nitro)
            print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"Sended -> {nitro}\n")

            
else:
        if cb == ("b"):
            for i in range(num):
                code = "".join(random.choices(
                                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                                k = 24
                            ))
                nitro = f"https://discord.gift/{code}"
                hook.send(nitro)
                print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + f"Sended -> {nitro}\n")
                
print("All the codes has been sended\n")
input("Press Enter for exit...")
        
    
    
    
    