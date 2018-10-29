from mydict import *

class mython(list):
    def __getitem__(self, item):
        # print ("getitem..", item)
        if type(item) == int:               #slices?
            return list.__getitem__(self, item)
        else:
            return self.handle_text_key(item)

    def handle_text_key(self, exp):
        # print ("EXP:", exp)
        while '.' in exp:
            beg = exp.find('.')
            if ' ' in exp[beg:]:
                end = beg + exp[beg:].find(' ')
            else:
                end = len(exp)
            key = exp[beg+1:end]
            if key != "":
                exp = exp[:beg] + '__x__["""' + key + '"""]' + exp[end:]
            else:
                exp = exp[:beg] + '__x__' + exp[end:]
        # print ("handle_text:", exp)
        ret = mython()
        for __x__ in self:
            try:
                if eval(exp):
                    ret.append(__x__)
            except:
                # print ("~~~", __x__)
                pass
        return ret

if __name__=="__main__":
    my=mython()
    my.append(mydict(foo = 2))
    my.append(mydict(foo = 11, bar=1, baz=3))
    my.append(mydict(box = mydict(bee = 555)))
    my.append(mydict(bar = 4))
    print()
    print()
    print('my')
    print(my)
    print()
    print('my[".foo"]')
    print(my[".foo"])
    print()
    print("""my["not .foo"]""")
    print(my["not .foo"])
    print()
    print('my[".foo == 2"]')
    print(my[".foo == 2"])
    print()
    print("""my["'foo' in . and .foo >= 2 or (.bar > 2 and .bar < 6)"]""")
    print(my["'foo' in . and .foo >= 2 or (.bar > 2 and .bar < 6)"])
    print()
    print('my[".foo > .bar"]')
    print(my[".foo > .bar"])
    print()
    print('my[".baz or .bar == 4"]')
    print(my[".baz or .bar == 4"])
    print()
    print('my["not .foo"][".bee"]')
    print(my["not .foo"][".box"])
    print()
    print('my["not .foo"][".box"][0].box.bee')
    print(my["not .foo"][".box"][0].box.bee)