import sys
from itertools import groupby

for key, group in groupby(sys.stdin):
    count = 0
    for item in group:
        count += 1
    print '%s\t%i' % (key.split()[0], count)
