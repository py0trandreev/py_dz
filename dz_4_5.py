import utils
import sys

if len(sys.argv) > 2:
    print('You have specified too many arguments')
    sys.exit()

if len(sys.argv) < 2:
    print('You need to specify the path to be listed')
    sys.exit()

input_currency = sys.argv[1]
print(utils.currency_rates(input_currency))

