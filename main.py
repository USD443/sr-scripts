import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


term_colors = {
    'BLUE': '\033[94m',
    'RED': '\033[91m'
}

cls()
print(
    f"{term_colors['BLUE']}Student Records Scripts\nCreated by Carlos Rodriguez\nVersion 1.0")
