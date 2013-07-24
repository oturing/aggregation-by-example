import sys
from itertools import groupby
from operator import itemgetter

def parse_line(line):
    key, value = line.rsplit(None, 1)
    return key, int(value)

split_stdin = (parse_line(l) for l in sys.stdin)

for key, group in groupby(split_stdin, itemgetter(0)):
    count = sum(int(value) for key, value in group)
    print '%s\t%i' % (key, count)
