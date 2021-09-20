import os 

from rich.prompt import Prompt
from rich import style
from rich.console import Console

console = Console()

def status_of_firewall():
	cmd=f'sudo firewall-cmd --state'
	res=os.popen(cmd).read()
	console.print(f'firewall status is {res}', style='italic #7C53E7')


def set_rule_allow():
	ip_add=input('Enter a ip address:- ')
	cmd=f'sudo ufw allow from {ip_add}'
	res=os.popen(cmd).read()
	console.print(f'Rule added {res}',style='bold italic #FF00FF')

def set_rule_deny(): 
        ip_add=input('Enter a ip address:- ')
        cmd=f'sudo ufw deny from {ip_add}' 
        res=os.popen(cmd).read() 
        console.print(f'Rule added {res}',style='bold italic green')

def set_rule_in_allow(): 
        subnet_add=input('Enter a ip address:- ')
        interface_name=input('Enter a interface name:- ')
        cmd=f'sudo ufw allow in on {interface_name} from {subnet_add}' 
        res=os.popen(cmd).read()
        console.print(f'Rule added {res}',style='bold italic #FF00FF')   

def set_rule_out_deny(): 
        subnet_add=input('Enter a subnet address:- ')
        interface_name=input('Enter a interface name:- ')
        cmd=f'sudo ufw deny out on {interface_name} from {subnet_add}'
        res=os.popen(cmd).read()
        console.print(f'Rule added {res}',style='bold italic #FF00FF')   

def set_rule_from_to_allow():
    ip_add=input('Enter a ip address:- ')
    port_num=int(input('Enter a port number:-'))
    cmd=f'sudo ufw allow from {ip_add} to any port {port_num}'
    res=os.popen(cmd).read()
    console.print(f'Rule added {res}',style='bold italic #FF00FF')   

def set_rule_protocol_in_allow():
        port_num=int(input('Enter a port number:-'))
        cmd=f'sudo ufw allow in from any  to any proto tcp port {port_num}' 
        res=os.popen(cmd).read() 
        console.print(f'Rule added {res}',style='bold italic #FF00FF') 

def set_rule_protocol_out_allow():
        port_num=int(input('Enter a port number:-'))
        cmd=f'sudo ufw allow out from any  to any proto tcp port {port_num}'
        res=os.popen(cmd).read() 
        console.print(f'Rule added {res}',style='bold italic #FF00FF') 

def delete_rule():
	cmd=f'sudo ufw status numbered '
	res1=os.popen(cmd).read()
	console.print(f'--------------status of all rules-------------',style='bold italic red' )
	console.print(f'{res1}',style='bold #CAEF74')
	index_number=int(input('Enter a index number:- '))
	cmd2=f'sudo ufw delete {index_number}'
	res2=os.popen(cmd2).read() 
	console.print(f' rule is deleted  successfully',style='bold italic red' )

def reload_rules():
	cmd=f'sudo firewall-cmd --reload'
	res=os.popen(cmd).read()
	console.print(f'Rules are reload successfully {res}',style='bold #CAEF74')




