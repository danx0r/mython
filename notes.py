"""
alternate syntaxi
"""


from mython import *
my=mython()

my
1> [{'bar': 4, 'foo': 5}, {'bar': 'three'}, {'foo': 6}]

my[this.bar]
1> [{'bar': 4, 'foo': 5}, {'bar': 'three'}]

my[this.bar == 4]
1> [{'bar': 4, 'foo': 5}]

my[this.foo]
1> [{'bar': 4, 'foo': 5}, {'foo': 6}]

my[this.bar < this.foo]
1> [{'bar': 4, 'foo': 5}]

my[not this.foo]          #returns list where members do not have .foo
1> [{'bar': 'three'}]

my[(not this.foo) & (this.bar == 'three')]
1> [{'bar': 'three'}]

my[not (this.foo == 6)]
1> [{'bar': 4, 'foo': 5}, {'bar': 'three'}]
