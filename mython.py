from mydict import mydict

class mython(list):
    def __getattr__(self, item):
        # print ("getattr..", item)
        return self.handle_text_key(item)

    # def __setattr__(self, key, value):
    #     self[key] = value

    def __getitem__(self, item):
        # print ("getitem..", item)
        if type(item) == int:               #slices?
            return list.__getitem__(self, item)
        else:
            return self.handle_text_key(item)

    def __eq__(self, b):
        # print (self, "==", b)
        return mython([x for x in self if x[self.__propertyname__]==b])

    def handle_text_key(self, item):
        ret = mython([x for x in self if isinstance(x, dict) and item in x])
        ret.__propertyname__=item
        return ret

if __name__=="__main__":
    my=mython([1,{'foo':2},mydict(bar=1, foo=2, baz=3),{'bar':4}])
    print(my)
    print(my[1])
    print(my.foo)
    print(my['bar'])
    print ("==================")
    print(my.bar == 4)
    md=mydict()
    md.bar=4
    md.foo="bax"
    my.insert(1,md)
    print(my.bar == 4)
