from firewall import *

from rich.prompt import Prompt
from rich import style
from rich.console import Console

console = Console()


def set_rules_main_menu():
	console.print('\t1.set rule allow',style='bold italic red')
	console.print('\t2.set rule deny',style='bold italic green')
	console.print('\t3.set rule in allow',style='bold italic blue')
	console.print('\t4.set rule out deny',style='bold #CAEF74')
	console.print('\t5.set rule from to allow',style='bold italic red')
	console.print('\t6.set rule protocol in allow ',style='bold #CAEF74')
	console.print('\t7.set rule protocol out allow',style='bold italic green')
	console.print('\t8.Back to Main Menu',style='bold italic red')

def set_rules():
	set_rules_main_menu()
	ch=int(input('Enter a you option:- '))
	if ch == 1:
                set_rule_allow()
	elif ch == 2:
		set_rule_deny()
	elif ch == 3:
		set_rule_in_allow()
	elif ch == 4:
		set_rule_out_deny()
	elif ch == 5:
		set_rule_from_to_allow()
	elif ch == 6:
		set_rule_protocol_in_allow()
	elif ch == 7:
		set_rule_protocol_out_allow()
	elif ch == 8:
		console.print(f'back to main menu',style='bold italic red')
	else:
		console.print(f'wrong choice',style='bold italic green')


def main_menu():
	console.print(f'--------------------------------FireWall Management--------------',style='bold #CAEF74')
	console.print('1.status of firewall ',style='bold italic #CAEF74')
	console.print('2.set rules ',style ='bold italic red')
	console.print('3.delete rules ',style='bold italic green')
	console.print('4.reload rules',style='bold #CAEF74')


while True:
	main_menu()
	ch=int(input('Enter your choice:-'))
	if ch == 1:
		status_of_firewall()
	elif ch == 2:
		set_rules()
	elif ch == 3:
		delete_rule()
	elif ch == 4:
		reload_rules()
	elif ch  ==5:
		console.print(f'*****************EXIT**************',style='bold green')
		break
	else:
		console.print(f'***********WRONG CHOICE*********ENTER VALID OPTION',style='bold red')


