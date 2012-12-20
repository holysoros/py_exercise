Number
==================

>>> a = 131.1415
>>> round(a, 3)
131.142
>>> round(a, 1)
131.1
>>> round(a, 0)
131.0
>>> round(a, -1)
130.0
>>> round(a, -2)
100.0


String
==================
Python中string有多种形式:

hello = "This is a rather long string containing\n\
several lines of text just as you would do in C.\n\
    Note that whitespace at the beginning of the line is\
 significant."

Or, strings can be surrounded in a pair of matching triple-quotes: """ or '''

print """
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
NOTE: 这里面的\n\t等仍有效, 即使是'''
"""

Or, 以'r'开始的string:

hello = r"This is a rather long string containing\n\
several lines of text much as you would do in C."


world = 'Help' 'A'	# 'HelpA'
world = world + 'B' * 3	# 'HelpABBB'
world[-2:]		# 'BB'
world[0] = 'X'		# Error: python strings cannot be changed.
len(world)		# 2


List
====================
>>> a = ['spam', 'eggs', 100, 1234]
>>> a
['spam', 'eggs', 100, 1234]

>>> a[1:-1]
['eggs', 100]
>>> a[:2] + ['bacon', 2*2]
['spam', 'eggs', 'bacon', 4]
>>> 3*a[:3] + ['Boo!']
['spam', 'eggs', 100, 'spam', 'eggs', 100, 'spam', 'eggs', 100, 'Boo!']

>>> a[:]
['spam', 'eggs', 100, 1234]

>>> # Replace some items:
... a[0:2] = [1, 12]
>>> a
[1, 12, 123, 1234]
>>> # Remove some:
... a[0:2] = []
>>> a
[123, 1234]
>>> # Insert some:
... a[1:1] = ['bletch', 'xyzzy']
>>> a
[123, 'bletch', 'xyzzy', 1234]
>>> # Insert (a copy of) itself at the beginning
>>> a[:0] = a
>>> a
[123, 'bletch', 'xyzzy', 1234, 123, 'bletch', 'xyzzy', 1234]
>>> # Clear the list: replace all items with an empty list
>>> a[:] = []
>>> a
[]

>>> q = [2, 3]
>>> p = [1, q, 4]
>>> len(p)
3
>>> p[1]
[2, 3]
>>> p[1][0]
2
>>> p[1].append('xtra')     # See section 5.1
>>> p
[1, [2, 3, 'xtra'], 4]
>>> q
[2, 3, 'xtra']

Note that in the last example, p[1] and q really refer to the same object!

Assignment
============

	>>> # Fibonacci series:
	... # the sum of two elements defines the next
	... a, b = 0, 1
	>>> while b < 10:
	...     print b
	...     a, b = b, a+b
	...
	1
	1
	2
	3
	5
	8

- The first line contains a multiple assignment: the variables a and b simultaneously get the new values 0 and 1. On the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated first before any of the assignments take place. The right-hand side expressions are evaluated from the left to the right.

- The condition may also be a string or list value, in fact any sequence; anything with a non-zero length is true, empty sequences are false.
