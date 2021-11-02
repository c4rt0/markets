def isiterable(object):
    try:
        iter(object)
        
        return [True, print(object), print( "is iterable")]
    except TypeError: #not iterable
        return False