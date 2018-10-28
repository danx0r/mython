"""
alternate syntaxi 2  -- Simplicio
"""


from mython import *
my=mython()

my
1> [{'bar': 4, 'foo': 5}, {'bar': 'three'}, {'foo': 6}]

my["bar"]
1> [{'bar': 4, 'foo': 5}, {'bar': 'three'}]

my["bar == 4"]
1> [{'bar': 4, 'foo': 5}]

my["foo"]
1> [{'bar': 4, 'foo': 5}, {'foo': 6}]

my["bar < foo"]
1> [{'bar': 4, 'foo': 5}]

my["!foo"]          #returns list where members do not have .foo
1> [{'bar': 'three'}]

my["!foo && bar==three"]
1> [{'bar': 'three'}]

my["!(foo == 6)"]
1> [{'bar': 4, 'foo': 5}, {'bar': 'three'}]

#spaces:
my["'foo bar' == 'Asperger Syndrome'"]
1> []

#strings not numbers:
my["foo == '3'"]
1> []
