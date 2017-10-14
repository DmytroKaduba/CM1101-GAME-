def draw_ascii(path):
    ascii_file = open(path, 'r')
    for line in ascii_file:
        new_line = line[:-1]
        print(new_line)
