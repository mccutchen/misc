import sys

def trace(f):
    def tracedfunc(*args, **kwds):
        name = f.func_name
        argstring = ', '.join(map(lambda x: '%s %s' % (x, type(x)), args))
        print >> sys.stderr, '%s(%s)' % (name, argstring)
        result = f(*args, **kwds)
        print >> sys.stderr, 'returned', result
        return result
    return tracedfunc

@trace
def prn(x):
    print x

@trace
def mult(x, y):
    return x * y

prn(mult(2,2))
