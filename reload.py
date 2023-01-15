#!/usr/bin/python3
import os

ALA_CONFIG_FILE_NAME = "alacritty.yml"
ALA_CONFIG_FILE_DIR = os.path.expanduser("~/.config/alacritty/")
ALA_CONFIG_FILE_PATH = os.path.join(ALA_CONFIG_FILE_DIR, ALA_CONFIG_FILE_NAME)

with open(ALA_CONFIG_FILE_PATH, "r") as f:
    lines = f.readlines()
    lines.append("#added")

with open(ALA_CONFIG_FILE_PATH, "w") as f:
    for line in lines:
        f.write(line)


with open(ALA_CONFIG_FILE_PATH, "w") as f:
    for line in lines[:-1]:
        f.write(line)
