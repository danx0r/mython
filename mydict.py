class mydict(dict):
    def __getattr__(self, item):
        try:
            return self[item]
        except:
            pass

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except:
            pass

    def __setattr__(self, key, value):
        self[key] = value

if __name__=="__main__":
    my=mydict(foo=11, bar="ZAP!")
    print (my)
    print (my.foo, my.bar)
    my.foo="FOO"
    print (my.foo, my['foo'])
    print (my.ape)
    print (my['ape'])