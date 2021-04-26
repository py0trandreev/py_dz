import sys

BAKERY = 'bakery.csv'

# check args number
if len(sys.argv) > 2:
    print("Too many arguments")
    sys.exit(1)

with open(BAKERY, 'a', encoding="utf-8") as f:
    f.write(('' if f.tell() == 0 else '\n') + sys.argv[1])
