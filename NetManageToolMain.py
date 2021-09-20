from network_manage_tool import *

from rich.prompt import Prompt
from rich import style
from rich.console import Console

console = Console()

def main():
       console.print('----------------------network management tool project--------------------',style='bold #CAEF74')
       console.print('1. Assign IP address',style='bold #CAEF74')
       console.print('2. Delete IP address',style='bold red')
       console.print('3. Display IP address',style='bold green')
       console.print('4. Display all interfaces',style='bold blue')
       console.print('5. Configure routing',style='bold green')
       console.print('6. Turn Off interface',style='bold red')
       console.print('7. Turn on interface',style='bold #CAEF74')
       console.print('8. Add ARP entry ',style='bold green')
       console.print('9. Delete ARP Entry',style='bold red')
       console.print('10.Restart Network',style='bold #CAEF74')
       console.print('11.Change hostname',style='bold blue')
       console.print('12.Add DNS server entry',style='bold red')


while True:
        main()
        ch =int(input('Enter your  choice:'))
        if  ch ==1:
                assign_ip_add()
        elif ch==2:
                delete_ip_add()
        elif ch==3:
                display_ip_add()
        elif ch ==4 :
                display_all_interfaces()
        elif ch ==5:
                configure_routing()
        elif ch ==6:
                turn_off_interface()
        elif ch ==7:
                turn_on_interface()
        elif ch ==8:
                add_ARP_entry()
        elif ch ==9:
                delete_arp_entry()
        elif ch ==10:
                Restart_network()
        elif ch ==11:
                Change_hostname()
        elif ch ==12:
                add_dns_server()
        elif ch == 13:
                console.print(f'----------------------------Exit-----------------',style='bold italic red')
                break
        else:
                console.print('wrong choce!***please enter valiad number',style='bold #CAEF74')
