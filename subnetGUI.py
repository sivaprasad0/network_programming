from subnetcalulator import *
import tkinter as tk


win = tk.Tk()
win.title("Subnet Calculator")
win.geometry("600x400")

ipaddress = tk.StringVar(win)
subnetaddress = tk.IntVar(win)
networkaddress =tk.StringVar(win)
brodcastaddress = tk.StringVar(win)
availablehosts = tk.StringVar(win)
rang = tk.StringVar(win)

def clear():
	ipaddress.set('')
	subnetaddress.set(0)
	networkaddress.set('')
	brodcastaddress.set('')
	availablehosts.set('')
	range.set('')
	

def cal():
	ip_addr = [int(x) for x in ipaddress.get().split(".")]
	sub = subnetaddress.get()
	network_addr = net_addr(ip_addr,sub)
	lst = []
	lst1 = []
	for i in network_addr:
		lst.append(str(i))
	networkaddress.set(".".join(lst))
	broadcast_addr = broad_addr(ip_addr,sub)
	for i in broadcast_addr:
		lst1.append(str(i))
	brodcastaddress.set(".".join(lst1))
	no_avail,host_ip = available_host(ip_addr,sub)
	avail_host.set(f"Available: {no_avail} Actual avail: {host_ip}")
	network_addr[3] = int(network_addr[3]) + 1
	start_range = ".".join(map(str, network_addr))
	broadcast_addr[3] = int(broadcast_addr[3]) - 1
	end_range = ".".join(map(str, broadcast_addr))
	rang.set(f"{start_range}  '-'  {end_range}")



tk.Label(win,text = "IP ADDRESS").grid(row=0,column=0)
ipfield = tk.Entry(win,textvariable=ipaddress)
ipfield.grid(row=0,column=1)

tk.Label(win, text="SUBNET").grid(row=1, column=0)
subnetfield = tk.Entry(win, textvariable=subnet)
subnetfield.grid(row=1, column=1)


tk.Button(win,text="CALCULATE",command = cal).grid(row=3,column=0)
tk.Button(win,text="Clear",command = clear).grid(row=3,column=1)

tk.Label(win,text = "NETWORK ADDRESS").grid(row=5,column=0)
netwfield = tk.Entry(win,textvariable=networkaddress)
netwfield.grid(row=5,column=1)

tk.Label(win, text="BRODCAST ADDRESS").grid(row=6, column=0)
brodfield = tk.Entry(win, textvariable=brodcastaddress)
brodfield.grid(row=6, column=1)

tk.Label(win,text = "AVAILABLE IP").grid(row=7,column=0)
avail_hostfield = tk.Entry(win,textvariable=availablehosts)
avail_hostfield.grid(row=7,column=1)

tk.Label(win,text = "RANGE").grid(row=8,column=0)
rangefield = tk.Entry(win,textvariable=RANGE)
rangefield.grid(row=8,column=1)

win.mainloop()
