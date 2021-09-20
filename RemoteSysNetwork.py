import paramiko
import time

from rich.prompt import Prompt
from rich import style
from rich.console import Console

console = Console()


def connect(hostname, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Connecting.............")
    ssh_client.connect(hostname=hostname, port=port,
                       username=username, password=password)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_cmd(shell,cmd):
    print(f"Sending...{cmd}")
    shell.send(cmd+"\n")
    time.sleep(1)

def show(shell):
    output = shell.recv(10000)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print("Disconnecting.............")
        ssh_client.close()


if __name__ == "__main__":
    client=connect("192.168.1.1",22,"superuser","root")
    shell=get_shell(client)

    send_cmd(shell,"ls")
    send_cmd(shell,"free -m ")
    send_cmd(shell,'w')
    send_cmd(shell,'route -n')
    send_cmd(shell,'uptime')

    output = show(shell)
    console.print(f'{output}',style='bold italic green')
