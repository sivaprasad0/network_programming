import os
import json

from rich.prompt import Prompt
from rich import style
from rich.console import Console

console = Console()


def stats_docker():
	cmd = 'docker  stats' # checking docker container status
	res=os.system(cmd)
	console.print(f'docker container stats *** {res}',style='bold red' )

def download_docker_image():
	image_list=os.popen('docker images').read() # download images from docker repo
	console.print(f'*********docker images*********',style='bold red')
	console.print(f'{image_list}',style='rgb(175,0,255)')
        image_nm_tag = input("Enter image_name: ")
        cmd = f'docker pull {image_nm_tag}'
        res = os.popen(cmd).read()
        console.print(f'----download_docker image--------',style='bold red')
        console.print(f'{res}',style='bold #F908E6 ')


def run_container():
        image_nm_tag = input("Enter image_name: ")  # run container
        container_name = input("Enter container name: ")
        cmd = f'docker run --name {container_name} {image_nm_tag}'
        res=os.popen('docker ps -a |head -n 2').read()
        console.print(f'---------run container is succesfully--------- ',style='bold blue')
        console.print(f'{res}',style='link https://google.com')

def delete_container():
        # delete container
        container_name = input('Enter container name ')
        cmd = f'docker rm {container_name}'
        res = os.popen(cmd).read()
        console.print(f'{res} container deleted successfully ',style='bold red')


def network_details():
    # network details of a container
    cmd = 'docker network inspect bridge'
    l = os.popen(cmd).read()
    res = json.loads(l)[0]
    for i in res['Containers'].values():
        print(f'Name => {i["Name"]} | id  => {i["macaddress"]} | ipv4 address =>{i["IPv4Address"]}')
        console.print(f'container is empty {i} ',style='bold red')

