import sys

class clrs:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    sys.argv[1]
except IndexError:
    print(clrs.FAIL + "Boi, we need a file." + clrs.ENDC)
    sys.exit()
else:
    file_arg = str(sys.argv[1])

try:
    sys.argv[2]
except IndexError:
    inspect_flag = False
else:
    if sys.argv[2] == "-i":
        inspect_flag = True
    else:
        inspect_flag = False


def read_file(dir):
    with open(dir, 'r') as boiCode:
        data = boiCode.read().replace('\n', '')
    return data
