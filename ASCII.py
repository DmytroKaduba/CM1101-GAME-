from utilities import clear
from time import sleep


def draw_ascii(path):
    ascii_file = open(path, 'r')
    for line in ascii_file:
        new_line = line[:-1]
        print(new_line)

def draw_anim_ascii(path):

    a_file = open(path, 'r')
    length = len(a_file.readline())

    for i in range(0, length):
        clear()

        ascii_file = open(path, 'r')
        for line in ascii_file:
            new_line = line[:-1]
            print(new_line[0:i])

        sleep(0.1)
