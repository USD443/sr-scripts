import json
import shutil
import time
import os
from pathlib import Path
from scripts.colors import color

with open('./path.json', 'r') as f:
    path_data = json.load(f)

start_path_files = os.listdir(Path(path_data['START_PATH']))
destination_path_files = os.listdir(Path(path_data['END_PATH']))


def move_files():
    srt_time = time.perf_counter()
    print(color('green', '\nCommand started: Moving Records'))
    for file in start_path_files:
        file_name = os.path.join(path_data['START_PATH'], file)
        shutil.move(file_name, path_data['END_PATH'])
    end_time = time.perf_counter()
    final_time = "{:.4f}".format(end_time - srt_time)
    print(f"{color('green', 'Task completed!')} {color('blue', final_time)} seconds")


def load_stats():
    print(f"Loading path data from --> {color('yellow', 'path.json')}\n")
    print(
        f"{color('blue', '<--')} {path_data['START_PATH']} {color('blue', '(' + str(len(start_path_files)) + ' files)')}")
    print(
        f"{color('blue', '-->')} {path_data['END_PATH']} {color('blue', '(' + str(len(destination_path_files)) + ' files)')}")

    user_choice = input(
        f"\nRead to move files? {color('blue', '[1]:Yes [2]:No')}: ")
    try:
        if int(user_choice) == 1:
            move_files()
        elif int(user_choice) == 2:
            print(color('yellow', '\nScript terminated by user'))
        else:
            print(
                f"{color('yellow', 'Enter a valid option [1] or [2]')} {color('red', '(script exited)')}")
    except ValueError:
        print(f"{color('yellow', 'Please only use numbers to select the command')} {color('red', '(script exited)')}")


def move():
    print(color('underline', 'Moving Records\n'))
    load_stats()
