#!/usr/bin/python3

#Menu driven network scanning tool:
 
import nmap
import os


def scan_single_host():
	nm = nmap.PortScanner() 
	ip_address = input("\tEnter the IP : ")
	print("Wait.......................")
	try:
		scan = nm.scan(hosts=ip_address,ports="1-2000")
		for port in scan["scan"][ip_address]['tcp'].items():
			print(scan)
			print(f"{port[0]}, {port[1]['state']} , {port[1]['name']}")
	except:
		print("Use root priviliege")

def scan_range():
	nm = nmap.PortScanner() 
	ip_address = input("\tEnter the IP : ")
	range=input('enter a range number:-')
	print("Wait........................")
	try:

		scan = nm.scan(ip_address ,range)
		print(scan)
		for port in scan["scan"][ip_address]['tcp'].items():
			print(f"{port[0]}, {port[1]['state']} , {port[1]['name']}")
	except:
		print("Use root priviliege")


def scan_netwrk():
        nm = nmap.PortScanner()
        ip_address = input("\tEnter the IP address  with mask : ")
        print("Wait........................")
        try:
                scan = nm.scan(ip_address)
                print(scan)
        except:
                print('use root privillage')

def aggrisave_scan():
	nm = nmap.PortScanner()
	ip_address = input("\tEnter the IP : ")
	arg='-T4'
	print('Wait--------------------')
	scan=nm.scan(ip_address,arg)
	print(scan)

def scan_arp_packet() :
	nm = nmap.PortScanner() 
	ip_address = input("\tEnter the IP : ")
	arg='-PR'
	print("Wait........................")
	try:
		scan = nm.scan(ip_address ,arg)
		print(scan)
	except:
		print("Use root priviliege")

def scan_all_port():
	nm = nmap.PortScanner() 
	ip_address = input("\tEnter the IP : ")
	arg='-pn'
	print("Wait........................")
	try:
		scan = nm.scan(ip_address , arg)
		print(scan)
	except:
		print("Use root priviliege")


def scan_verbose_mode():
        nm = nmap.PortScanner()
        ip_address=input('Enter the ip  address:-')
        arg='-v'
        prin('wait------------------')
        scan=nm.scan(ip_address,arg)
        print(scan)

