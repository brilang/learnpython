from colorama import init, Fore
init(autoreset=True)

def display(message, isWarning = False):
    if isWarning:
        print(Fore.RED + f"Warning: {message}")
    else:
        print(Fore.BLUE + message)
