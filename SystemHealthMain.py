from system_health import *
from rich.prompt import Prompt
from rich import style
from rich.console import Console

console = Console()

def main():
	console.print('**************SYSTEM HEALTH**************',style='bold blue')
	console.print('1.Display Available RAM',style='bold green')
	console.print('2.Display Load Average',style='bold #7C53E7')
	console.print('3.Display Hostname details',style='bold blue')
	console.print('4.Display All process count',style='bold green')
	console.print('5.Display uptime',style='bold #7C53E7')
	console.print('6.Exit',style='bold #F908E6')

while True :
	main()
	ch=int(input('Enter your Choice: '))
	if   ch == 1:
		display_available_ram()
	elif ch == 2 :
		display_load_avg()
	elif ch == 3 :
		hostname_details()
	elif ch == 4:
		process_count()
	elif ch == 5:
		uptime()
	elif ch ==6 :
		console.print('**************Exit*****************',style='bold #F908E6 ')
		break
	else:
		console.print('***************Entered Wrong Option***********Please Enter Valid option',style='bold red')
