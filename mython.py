class mython(list):
    def __getitem__(self, item):
        # print ("getitem..", item)
        if type(item) == int:               #slices?
            return list.__getitem__(self, item)
        else:
            return self.handle_text_key(item)

    def handle_text_key(self, exp):
        print ("EXP:", exp)
        while '.' in exp:
            beg = exp.find('.')
            if ' ' in exp[beg:]:
                end = beg+exp[beg:].find(' ')
            else:
                end = len(exp)
            key = exp[beg+1:end]
            exp = exp[:beg]+'__x__["""'+key+'"""]'+exp[end:]
        print ("handle_text:", exp)
        ret = []
        for __x__ in self:
            try:
                if eval(exp):
                    ret.append(__x__)
            except:
                print ("~~~", __x__)
                pass
        return ret

if __name__=="__main__":
    my=mython([{'foo':2}, dict(bar=1, foo=11, baz=3), {'bar':4}])
    print(my)
    # print(my[".foo"])
    # print(my["not .foo"])
    # print(my[".foo == 2"])
    print(my[".bar > 2 and .bar < 6 or .foo == 2"])
