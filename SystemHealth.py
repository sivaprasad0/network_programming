import json
import os 

from rich.prompt import Prompt
from rich import style
from rich.console import Console

console = Console()

def display_available_ram():
	d=[]
	cmd=os.popen('free -m').read()
	for i in cmd.split():
		d.append(i)
	print(d)
	console.print(f'avaiable memory *** ',d[11],style='bold red')

def display_load_avg():
    cmd = 'cat /proc/loadavg'
    res = os.popen(cmd).read()
    console.print(f'load average *** {res}', style='italic #7C53E7 ')

def hostname_details():
	cmd= 'uname -a '
	cmd1= 'uname'
	res=os.popen(cmd).read()
	res1=os.popen(cmd1).read()
	console.print(f'--------------hostname details-------------------------',style='bold red')
	console.print(f'{res}',style='bold #F908E6 ')
	console.print(f'hostname ***** {res1}',style='bold green ')

def process_count():
	cmd='ps -a | wc -l'
	res =os.popen(cmd).read()
	console.print(f'all process counted ***** {res} ',style='bold blue')

def uptime():
	cmd= 'uptime' 
	res=os.popen(cmd).read()
	console.print(f'uptime ***** {res}',style='bold #F908E6 ')


