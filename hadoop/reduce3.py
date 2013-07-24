import sys
from itertools import groupby
from operator import itemgetter

split_stdin = (item.split() for item in sys.stdin)

for key, group in groupby(split_stdin, itemgetter(0)):
    count = 0
    for key, value in group:
        count += int(value)
    print '%s\t%i' % (key, count)
