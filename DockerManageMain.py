from Docker_manage import * 
from rich.prompt import Prompt
from rich import style
from rich.console import Console
console = Console()

def main():
        console.print('------------------------------Docker management---------------------------',style='bold italic red')
        console.print('1.Status of containers',style='bold red')
        console.print('2.Download new Image',style='bold green')
        console.print('3.Run container',style='#7C53E7')
        console.print('4.Delete Container',style='bold red')
        console.print('5.Network details of container',style='bold green')
        console.print('6.Modify Network details of contaniner'style='#7C53E7')
        console.print('7.exit',style='bold red')

while True :
	main()
	ch=int(input('Enter your choice: '))
	if ch == 1:
		stats_docker()
	elif ch == 2 :
		download_docker_image()
	elif ch == 3 :
		run_container()
	elif ch == 4:
		delete_container()
	elif ch == 5:
		network_details()
	elif ch == 6:
		modify_network_details()
	elif ch == 7:
		console.print('------------------Exit----------------',style='bold green')
		break
	else:
		console.print('wrong options',style='bold #F908E6 ')
