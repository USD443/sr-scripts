import json
import os
from scripts.colors import color

with open('./path.json', 'r') as f:
    path_data = json.load(f)

start_path_files = len(os.listdir(path_data['START_PATH']))
destination_path_files = len(os.listdir(path_data['END_PATH']))


def load_stats():
    print("Loading path data from path.json\n")
    print(
        f"{color('green', '<--')} {path_data['START_PATH']} {color('blue', '(' + str(start_path_files) + ' files)')}")
    print(
        f"{color('green', '-->')} {path_data['END_PATH']} {color('blue', '(' + str(destination_path_files) + ' files)')}")


def move():
    print(color('underline', 'Moving Records\n'))
    load_stats()
