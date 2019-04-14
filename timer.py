
from time import time
def timer(func):
    '''wrapper'''
        def f(*args, **kwargs):
            '''
            timer decorator
            separates additional behavior from the main functionality.
            provides mechanism of extending functionality without modifying 
            the business logic itself 
            '''
            before = time()
            rv = func(*args, **kwargs)
            after = time()
            print 'elapsed', after - before
            return rv
    return f

