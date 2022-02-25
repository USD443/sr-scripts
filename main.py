import os
from scripts.move import move
from scripts.rename import rename
from scripts.colors import color


script_version = 1.0


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    cls()
    print(color("green", "Student Records Scripts"))
    print(f"Created by Carlos Rodriguez")
    print(f"Version {script_version}\n")


def launch_script(num: int):
    welcome()
    if num == 1:
        move()
    elif num == 2:
        rename()
    else:
        print(
            f"{color('yellow', 'Please enter a valid option')}{color('red', ' (script exited)')}")


def get_script():
    print(color('underline', 'What would you like to do?\n'))
    print(color('blue', '[1]: Move Records'))
    print(color('blue', '[2]: Rename Records'))

    user_choice = input(
        color('bold', '\nEnter the number corresponding to the command: '))
    try:
        launch_script(int(user_choice))
    except ValueError:
        print(
            f"{color('yellow', 'Please use only numbers')}{color('red', ' (script exited)')}")


welcome()
get_script()
