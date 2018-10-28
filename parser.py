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
    if ret == '(':
        # print ("PARSE PAREN CLAUSE:", toks)
        ret = _parse()
        # print ("PARSED: %s REMAIN: %s", (ret,toks))
        end = toks.pop(0)
        if end != ')':
            print ("SYNTAX ERROR: expected )", end, toks)
            return 
    if len(toks) and toks[0] != ')':            #so slick
        op = toks.pop(0)
        if op not in BINARIES:
            print ("SYNTAX ERROR: expected binary operator", op, toks)
            return
        ret = {op: [ret, _parse()]}
    return ret

if __name__=="__main__":
    s = ".bar"
    print(parse(s))
    s = ".bar == 4"
    print(parse(s))
    s = ".bar == 4  > 5"
    print(parse(s))
    s = ".bar and .foo > 5"
    print(parse(s))
    s = "( a > b ) and ( c < d )"
    print(parse(s))
