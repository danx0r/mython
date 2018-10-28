"""
parse text string into tokens
"""

#
# dead-simple binary parser
#
def parse(s):
    global toks
    toks = s.split()            #FIXME: deal w spaces, etc
    # print (toks)
    return _parse()

BINARIES = ['<', '>', '==', '<=', '>=', '!=', 'and', 'or']

def _parse():
    ret = toks.pop(0)
    if len(toks):
        op = toks.pop(0)
        if op not in BINARIES:
            print ("SYNTAX ERROR")
            return
        ret = {op: [ret, _parse()]}
    return ret

if __name__=="__main__":
    s = ".bar"
    print(parse(s))
    s = ".bar == 4"
    print(parse(s))
    s = ".bar == 4  > 5"
    s = ".bar and .foo > 5"
    print(parse(s))
