from mython import *
my=mython()

my
1> [{'bar': 4, 'foo': 5}, {'bar': 'three'}, {'foo': 6}]

my.bar                      #try not being lazy for once
1> [{'bar': 4, 'foo': 5}, {'bar': 'three'}]

my.bar == 4
1> [{'bar': 4, 'foo': 5}]

my.foo
1> [{'bar': 4, 'foo': 5}, {'foo': 6}]

my.bar < my.foo
1> [{'bar': 4, 'foo': 5}]

not my.foo          #returns list where members do not have .foo
1> [{'bar': 'three'}]

(not my.foo) & my.bar == 'three'
1> [{'bar': 'three'}]

not (my.foo == 6)
1> [{'bar': 4, 'foo': 5}, {'bar': 'three'}]
