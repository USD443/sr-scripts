import os
from scripts.move import move

script_version = 1.0

term_colors = {
    'BLUE': '\033[94m',
    'RED': '\033[91m',
    "YELLOW": '\033[93m',
    "GREEN": '\033[92m',
    'CLEAR': '\033[0m',
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[4m'
}


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    cls()
    print(
        f"{term_colors['BOLD']}{term_colors['GREEN']}Student Records Scripts{term_colors['CLEAR']}")
    print(f"Created by Carlos Rodriguez")
    print(f"Version {script_version}\n\n")


def launch_script(num: int):
    welcome()
    if num == 1:
        move()
    else:
        print("2 was picked")


def get_script():
    print(
        f"{term_colors['UNDERLINE']}What would you like to do?{term_colors['CLEAR']}\n")
    print(f"{term_colors['BLUE']}1: Move records")
    print(f"2: Rename records{term_colors['CLEAR']}\n\n")
    user_choice = input(
        f"{term_colors['BOLD']}Enter the number corresponding to the command: {term_colors['CLEAR']}")
    launch_script(int(user_choice))


welcome()
get_script()
