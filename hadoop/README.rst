======================================================
Variations on a Hadoop reduce script written in Python
======================================================

Hadoop allows map and reduce processing to be performed in any language that
supports reading and writing to standard IO.

The reduce stage takes sorted input like this::

    ERROR   1
    INFO    1
    INFO    1
    INFO    1
    INFO    1
    WARN    1
    WARN    1

And must output aggregated results like this::

    ERROR   1
    INFO    4
    WARN    2

Here are some ways of doing that, using different idioms. All of the
following implementations use a constant ammount of memory, regardless
of the size of the input or output.

Version 0: basic Python
=======================

Not idiomatic, but works and anyone can read::

::

    import sys

    previous_key = ''
    sum = 0
    for line in sys.stdin:
        key, value = line.split()
        value = int(value)
        if key == previous_key:
            sum = sum + value
        else:
            if previous_key != '':
                print '%s\t%i' % (previous_key, sum)
            previous_key = key
            sum = 1
    print '%s\t%i' % (previous_key, sum)

Version 1: using `groupby` and a named function
===============================================

::

    import sys
    from itertools import groupby

    def extract_key(line):
        return line.split()[0]

    for key, group in groupby(sys.stdin, extract_key):
        count = 0
        for item in group:
            count += int(item.split()[1])
        print '%s\t%i' % (key, count)


Version 1b: same as above, with an anonymous function
=====================================================

Some pythonistas are not very fond of lambdas, but here is another way.

::

    import sys
    from itertools import groupby

    for key, group in groupby(sys.stdin, lambda l: l.split()[0]):
        count = 0
        for item in group:
            count += int(item.split()[1])
        print '%s\t%i' % (key, count)


The main problem with anonymous functions: they have no name.


Version 2: possibly dangerous shortcut
======================================

If you now with absolute certainty that every single line

::

    import sys
    from itertools import groupby

    for key, group in groupby(sys.stdin):
        count = 0
        for item in group:
            count += 1
        print '%s\t%i' % (key.split()[0], count)










