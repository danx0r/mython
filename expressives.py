class expressive(object):

    def __init__(self, name):
        self.name = name

    def __eq__(self, b):
        print (self, "==", b)
        return {'eq': [self, b]}

    def __repr__(self):
        return ".%s" % self.name

class expressive_maker(object):

    def __getattr__(self, name):
        # print ("getattr:", name)
        return expressive(name)
    
_ = expressive_maker()

if __name__=="__main__":
    # b = _.bar
    # print (b, b.name)
    # print (_.bar == _.foo)
    print (_.bar == (_.foo == _.baz))