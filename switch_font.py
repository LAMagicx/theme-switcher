#!/usr/bin/python3
import yaml, os, re

ALA_CONFIG_FILE_NAME = "fonts.yml"
ALA_CONFIG_FILE_DIR = os.path.expanduser("~/.config/alacritty/")
ALA_CONFIG_FILE_PATH = os.path.join(ALA_CONFIG_FILE_DIR, ALA_CONFIG_FILE_NAME)

FONT_NAME_SEARCH = "family: *([\S ]+)"
FONT_NAME_TEMPLATE = "    family:{}\n"

def get_terminal_fonts():
    file = os.path.join(ALA_CONFIG_FILE_DIR, "tmp")
    os.system("fc-list : family style file | grep -v 'Noto' | cut -d ':' -f 2 | cut -d ',' -f 1 > "+file)
    fonts = open(file,"r").read().split("\n")
    os.remove(file)
    return list(set(fonts))[1:]

def set_terminal_font(font):
    with open(ALA_CONFIG_FILE_PATH, "r") as f:
        lines = f.readlines()

    indexes = []

    for i,line in enumerate(lines):
        match = re.search(FONT_NAME_SEARCH, line)
        if match is not None:
            indexes.append(i)

    for i in indexes:
        lines[i] = FONT_NAME_TEMPLATE.format(font)

    with open(ALA_CONFIG_FILE_PATH, "w") as f:
        for line in lines:
            f.write(line)

def get_current_font():
    with open(ALA_CONFIG_FILE_PATH, "r") as f:
        lines = f.readlines()

    for i,line in enumerate(lines):
        match = re.search(FONT_NAME_SEARCH, line)
        if match is not None:
            return match.group(1)

    return "Hack"

def switch_terminal_font():
    fonts = get_terminal_fonts()
    set_terminal_font(fonts[(fonts.index(" "+get_current_font())+1)%len(fonts)])
    print(get_current_font())

if __name__ == "__main__":
    switch_terminal_font()
    os.system("python reload.py")
