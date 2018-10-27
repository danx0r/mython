class expressive(object):

    def __init__(self, exp):
        self.exp = exp

    def __eq__(self, b):
        # print (self, "==", b)
        ret = expressive({'==': [self, b]})
        # print (" RET:", ret)
        return ret

    def __ge__(self, b):
        # print (self, "==", b)
        ret = expressive({'>=': [self, b]})
        # print (" RET:", ret)
        return ret

    def __lt__(self, b):
        # print (self, "==", b)
        ret = expressive({'<': [self, b]})
        # print (" RET:", ret)
        return ret

    def __and__(self, b):
        # print (self, "==", b)
        ret = expressive({'&': [self, b]})
        # print (" RET:", ret)
        return ret

    def __repr__(self):
        if hasattr(self.exp, 'capitalize'):
            return ".%s" % self.exp
        else:
            return "%s" % self.exp

class expressive_maker(object):

    def __getattr__(self, exp):
        # print ("getattr:", exp)
        return expressive(exp)
    
_ = expressive_maker()

if __name__=="__main__":
    from pprint import pprint
    print ()
    # bf = _.bar == _.foo
    # print(bf)
    # print ("==================")
    # fz = _.foo == _.zap
    # print(fz)
    # print ("==================")
    # bz = (bf == fz)
    # print(bz)
    # pprint (_.bar >= _.foo & _.baz < _.zap)
    pprint (_.bar >= _.foo < _.zap)
    pprint (_.bar >= (_.foo < _.zap))
