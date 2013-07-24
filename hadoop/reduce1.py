import sys
from itertools import groupby

def get_key(line):
    return line.split()[0]

for key, group in groupby(sys.stdin, get_key):
    count = 0
    for item in group:
        count += int(item.split()[1])
    print '%s\t%i' % (key, count)
