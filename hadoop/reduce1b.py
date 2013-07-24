import sys
from itertools import groupby

for key, group in groupby(sys.stdin, lambda l: l.split()[0]):
    count = 0
    for item in group:
        count += int(item.split()[1])
    print '%s\t%i' % (key, count)
