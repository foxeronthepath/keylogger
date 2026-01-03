import os
import sys
from pynput import keyboard
from colorama import init, Fore, Style

# Initialize colorama for Windows
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════╗
{Fore.CYAN}║{Fore.GREEN}                                                      {Fore.CYAN}║
{Fore.CYAN}║{Fore.GREEN}      ██╗  ██╗███████╗██╗   ██╗██╗      ██████╗       {Fore.CYAN}║
{Fore.CYAN}║{Fore.GREEN}      ██║ ██╔╝██╔════╝╚██╗ ██╔╝██║     ██╔═══██╗      {Fore.CYAN}║
{Fore.CYAN}║{Fore.GREEN}      █████╔╝ █████╗   ╚████╔╝ ██║     ██║   ██║      {Fore.CYAN}║
{Fore.CYAN}║{Fore.GREEN}      ██╔═██╗ ██╔══╝    ╚██╔╝  ██║     ██║   ██║      {Fore.CYAN}║
{Fore.CYAN}║{Fore.GREEN}      ██║  ██╗███████╗   ██║   ███████╗╚██████╔╝      {Fore.CYAN}║
{Fore.CYAN}║{Fore.GREEN}      ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝       {Fore.CYAN}║
{Fore.CYAN}║{Fore.GREEN}                                                      {Fore.CYAN}║
{Fore.CYAN}╠══════════════════════════════════════════════════════╣
{Fore.CYAN}║{Fore.YELLOW}  Status: {Fore.GREEN}● CONNECTION ESTABLISHED{Fore.YELLOW}                    {Fore.CYAN}║
{Fore.CYAN}║{Fore.YELLOW}  Mode: {Fore.WHITE}ACTIVE LISTENING                              {Fore.CYAN}║
{Fore.CYAN}╠══════════════════════════════════════════════════════╣
{Fore.CYAN}║{Fore.WHITE}  Captured Input:                                     {Fore.CYAN}║
{Fore.CYAN}╚══════════════════════════════════════════════════════╝
{Style.RESET_ALL}

"""
    print(banner, end='', flush=True)

def on_press(key):
    try:
        # Print regular character keys
        if hasattr(key, 'char') and key.char is not None:
            print(f"{Fore.GREEN}{key.char}{Style.RESET_ALL}", end='', flush=True)
        # Handle special keys
        elif key == keyboard.Key.space:
            print(f"{Fore.GREEN} {Style.RESET_ALL}", end='', flush=True)
        elif key == keyboard.Key.enter:
            print(f"{Fore.GREEN}\n{Style.RESET_ALL}", end='', flush=True)
        elif key == keyboard.Key.backspace:
            print('\b \b', end='', flush=True)
        elif key == keyboard.Key.tab:
            print(f"{Fore.GREEN}    {Style.RESET_ALL}", end='', flush=True)
    except Exception as e:
        pass

def main():
    clear_screen()
    print_banner()
    
    # Start listening to keyboard events
    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            clear_screen()
            print(f"\n{Fore.RED}Session terminated.{Style.RESET_ALL}\n")

if __name__ == "__main__":
    main()

