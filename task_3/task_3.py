import sys, re
from colorama import Fore, Style
from pathlib import Path

def print_path(directory, level):        
    for path in directory.iterdir(): 
        path_to_print = level*"    " + ((str(path).split('\\'))[::-1])[0]     
        if path.is_dir():    
            print(f"{Fore.RED}{path_to_print}/")
            print_path(path, level+1)
        else:
            print(f"{Fore.GREEN}{path_to_print}")
print(f"{Fore.RED}{sys.argv[1]}/")
directory = Path(sys.argv[1])
print_path(directory, 0)
print(Style.RESET_ALL)