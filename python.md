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
