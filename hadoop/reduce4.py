import sys
from itertools import groupby
from operator import itemgetter

split_stdin = (item.split() for item in sys.stdin)

for key, group in groupby(split_stdin, itemgetter(0)):
    count = sum(int(value) for key, value in group)
    print '%s\t%i' % (key, count)
