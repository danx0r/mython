class mydict(dict):
    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        self[key] = value

if __name__=="__main__":
    my=mydict(foo=11, bar="ZAP!")
    print (my)
    print (my.foo, my.bar)
    my.foo="FOO"
    print (my.foo, my['foo'])