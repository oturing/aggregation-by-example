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

Not idiomatic, but works and anyone can read:

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

Version 1: using ``groupby`` and a named function
=================================================

The ``itertools`` module has several interesting functions that take iterables
and return generators. Very useful for large-scale data processing.

The ``itertools.groupby`` function takes an iterable with sorted keys and
returns a generator which yields ``(key, group)`` tuples, where ``key`` is
the grouping key and ``group`` is another generator yielding the items in each
group. The result of ``groupby`` is usually processed using two nested ``for``
loops, as in this example.

The second argument to ``groupby`` is a function used to extract the key from
each input item.

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


The main problem with anonymous functions: they have no name. This often
makes code harder to read.


Version 2: (possibly) dangerous shortcut
========================================

If you know with absolute certainty that every single line in the reduce
input has the value 1, then you can use the whole line as key, and don't
need to provide a function to ``grouby``. You can simply count the
lines in each group, instead of adding all the 1's:

::

    import sys
    from itertools import groupby

    for key, group in groupby(sys.stdin):
        count = 0
        for item in group:
            count += 1
        print '%s\t%i' % (key.split()[0], count)


Version 3: lazily splitting items with a generator expression
=============================================================

Versions 1 and 1b above split each line twice, which is wasteful.
This version uses a generator expression to convert the ``sys.stdin``
iterable into a generator that yields each line split as a
``[key, value]`` list. Generator expressions are lazy: they produce
a generator which yields the processed items on demand.

Also, instead of using a custom function to extract the key from the pair,
here we use the ``itemgetter`` higher-order function which just produces
a function to extract the item at a certain index, in this case
the item at 0. In other words, ``itemgetter(0)`` is another way of saying
``lambda x: x[0]``.

::

    import sys
    from itertools import groupby
    from operator import itemgetter

    split_stdin = (item.split() for item in sys.stdin)

    for key, group in groupby(split_stdin, itemgetter(0)):
        count = 0
        for key, value in group:
            count += int(value)
        print '%s\t%i' % (key, count)


Version 4: replacing the inner loop with ``sum``
================================================

A generator expression can be used with the ``sum`` built-in function
to do the work of the inner ``for`` loop faster, and with less code.
It's faster because the loop implicit in ``sum`` is executed in compiled C
code.

::

    import sys
    from itertools import groupby
    from operator import itemgetter

    split_stdin = (item.split() for item in sys.stdin)

    for key, group in groupby(split_stdin, itemgetter(0)):
        count = sum(int(value) for key, value in group)
        print '%s\t%i' % (key, count)








