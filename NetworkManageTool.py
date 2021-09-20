#!/bin/user/python3

import os

from rich.prompt import Prompt
from rich import style
from rich.console import Console

console = Console()


def assign_ip_add():
    ip = input('Enter ip address to add on interface : ')
    inter_choice=Prompt.ask('Enter a interface name: ')
    cmd = f'sudo ip address add {ip} dev {inter_choice}'
    res = os.popen(cmd).read()
    console.print(res, style="bold italic #FF00FF")
    console.print('Ip address assigned successfully', style='bold green')

def delete_ip_add():
    ip = input('Enter ip address to delete  on interface : ')
    inter_choice=Prompt.ask('Enter a interface name:-')
    cmd = f'sudo ip address delete {ip} dev {inter_choice}'
    res = os.popen(cmd).read()
    console.print(res, style="bold italic #FF00FF")
    console.print('Ip address deleted successfully', style='link https://google.com')


def display_ip_add():
    command = f'ip -c -br address'
    res = os.popen(command).read()
    console.print(f'___________display ip address______________\n\n{res}', style='link https://google.com')

def display_all_interfaces():
    cmd= f'ip l'
    res = os.popen(cmd).read()
    console.print(f'**********All Interfaces Name Details******************\n\n{res}', style='rgb(175,0,255)')

def configure_routing():
    network_addr = input('Enter network Address with /mask : ')
    getway_ip = input('Enter Gateway ip address : ')
    cmd = f'ip r add {network_addr} via {getway_ip}'
    res = os.popen(cmd).read()
    console.print(res, style='bold green')
    console.print('Roting configuration completed ',style='bold italic #74EFA2')

def turn_off_interface():
    interface_name=input('Enter an interface name:- ')
    cmd = f' sudo ip link set dev {interface_name}  down'
    res = os.popen(cmd).read()
    console.print(f'interface is successfully turn off ', style='bold red')

def turn_on_interface():
    interface_name=input('Enter an interface name:- ')
    cmd = f' sudo ip link set dev {interface_name} up'
    res = os.popen(cmd).read()
    console.print(f'interface is successfully turn on ', style='bold green' )


def add_ARP_entry():
        ip = input('Enter ip address  :- ')
        mac_address=input('Enter Mac address :- ' )
        interface_name=input('Enter a interface Name:- ')
        cmd = f'sudo ip n add {ip} lladdr {mac_address} dev {interface_name} nud permanent'
        res = os.popen(cmd).read()
        arp_cache = os.popen('ip n show ').read()
        console.print(f'ARP cache {arp_cache}',style='bold #CAEF74')
        console.print('ARP Entry added successfully ', style='bold #CAEF74')

def delete_arp_entry():
        ip = input('Enter ip address  :- ')
        interface_name=input('Enter a interface Name:- ')
        cmd = f'sudo ip n del {ip}  dev {interface_name} '
        res = os.popen(cmd).read()
        arp_cache = os.popen('ip n show ').read()
        console.print(f'ARP cache {arp_cache}',style='bold #CAEF74')
        console.print('ARP Entry deleted successfully ', style='bold #CAEF74')


def Restart_network():
    cmd1 = 'sudo systemctl restart networking'
    cmd2 = 'sudo systemctl status networking'
    res=os.popen(cmd1).read()
    console.print(f'Network services restarted ',style='bold #CAEF74')
    res=os.popen(cmd2).read()
    console.print(f'network status network {res}',style='bold #CAEF74')

def Change_hostname():
    host_name = input("Enter new host name :")
    cmd = f'hostnamectl set-hostname {host_name}'
    os.popen(cmd).read()
    console.print(f'new host name {host_name} set successfully ',style='bold red')

def add_dns_server():
        ip=input('Enter ip address to add on interface:')
        cmd=f'sudo cat nameserver {ip} >>/etc/resolv.conf'
        res =os.popen(cmd).read()
        console.print('Nameserver added successfully {res} ', style='bold #F90D02')

