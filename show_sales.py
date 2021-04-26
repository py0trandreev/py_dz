from pathlib import Path
import sys

BAKERY = 'bakery.csv'

def enumerate_lines(file_obj, lines_to_read_ls):
    for position, line in enumerate(file_obj, start=1):
        if position in lines_to_read_ls:
            print(line, end='')


# check if the files exists
if not Path(BAKERY).is_file():
    print("File {} does not exist!".format(BAKERY))
    sys.exit(1)

# check args number
if len(sys.argv) > 3:
    print("Too many arguments")
    sys.exit(1)

with open(BAKERY, 'r', encoding="utf-8") as f:
    if len(sys.argv) > 2:  # 3 args
        lines_to_read = [el for el in range(int(sys.argv[1]), 1+int(sys.argv[2]))]
        enumerate_lines(f, lines_to_read)

    elif len(sys.argv) > 1:  # 2 args
        lines_to_read2 = [el for el in range(int(sys.argv[1]), 1+len(f.readlines()))]
        f.seek(0)
        enumerate_lines(f, lines_to_read2)

    else:  # 1 arg
        whole_list = f.read()
        print(whole_list)
