import sys

previous_key = ''
sum = 0
for line in sys.stdin:
    key, value = line.split()
    value = int(value)
    # continued on next slide
    # continued from previous slide
    if key == previous_key:
        sum = sum + value
    else:
        if previous_key != '':
            print '%s\t%i' % (previous_key, sum)
        previous_key = key
        sum = 1
print '%s\t%i' % (previous_key, sum)
