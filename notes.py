my.bar          #(lazy) returns my where there is a bar key

my.bar == 4

my.bar < my.foo

(my.bar & my.foo) | (my.xap in my.baz)

# implementation:
#
# lazy -- doesn't compute output until asked. so:

my.bar

#returns an object which, if subscripted, returns values:

my.bar[1]

#but if used in an expression, remains lazy:

x=my.bar > 10       #still lazy after all these years

x[0]                #computes values (generator?)

not my.bar          #returns list where members do not have .bar

(not my.bar) & my.foo   #members with foo & not bar
