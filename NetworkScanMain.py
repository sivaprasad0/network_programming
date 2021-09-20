from  network_scan_tool_project import *

from rich.prompt import Prompt
from rich import style
from rich.console import Console

console = Console()

def main():
        console.print(f'-----------------network scanner tool---------------',style='bold italic green')
        console.print("1. Scan single host",style='bold italic green')
        console.print('2. Scan range',style='bold italic blue')
        console.print("3. Scan network",style='magenta')
        console.print("4. Agressive scan",style='#af00ff')
        console.print("5. Scan ARP packet",style='rgb(175,0,255)')
        console.print("6. Scan All port only",style='bold green ')
        console.print('7. scan_verbose_mode',style='bold red')
        console.print("8.Exit",style='bold red')


while True:
        main()
        ch=int(input('Enter your choice:'))
        if ch == 1 :
                scan_single_host()
        elif ch==2:
                scan_range()
        elif ch ==3:
                scan_netwrk()
        elif ch ==4:
                aggrisave_scan()
        elif ch ==5:
                scan_arp_packet()
        elif ch ==6:
                scan_all_port()
        elif ch ==7:
                scan_verbose_mode()
        elif ch ==8:
                console.print(f'--------------Exit____________',style='bold italic green')
                break
        else:
                console.print(f'wrong choice',style='bold italic red')
