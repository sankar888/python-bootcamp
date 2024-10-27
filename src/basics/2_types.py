'''
2_types.py

This module introduces type system in python. 

Every value is an object in python and has an associated type. Even primary data types are built-in objects and they have a type associated with them.
Python Objects have attributes and methods. 

Functions which deal with type system, identity are as follows
    - type(obj) - returns the type of an object
    - id(obj) - Return the unique “identity” of an object. usually the memory address of an object
    - isinstance(obj, class) - Return True if the object argument is an instance of the class argument, or of a (direct, indirect, or virtual) subclass thereof.
    - issubclass(obj, class) - Return True if class is a subclass (direct, indirect, or virtual) of classinfo.
'''

def type_demo():
    '''
    Demo of type system in python
    '''
    a = 10 # type of 10 is int
    print(f'val of {a} is {type(a)}')

    b = 10.2 # float type
    print(f'val of {b} is {type(b)}')

    c = 3 + 10j # complex type
    print(f'val of {c} is {type(c)}')

    d = 'string' # str type
    print(f'val of {d} is {type(d)}')

    e = True # bool type
    print(f'val of {e} is {type(e)}')

    # Complex types
    f = [1,2,3] # list type
    print(f'val of {f} is {type(f)}')

    g = {a: 1, b: 2} # dict type
    print(f'val of {g} is {type(g)}')

    h = object() # object type
    print(f'val of {h} is {type(h)}')

def type_hierarchy_demo():
    '''
    Demo of type system in python. 
    object is the root of type hierarchy. All objects is subsclass of object and inherit the common attributes and methods of object
    
    Common Attributes:
    __class__: Represents the class the object belongs to.
    __dir__(): Lists all available attributes and methods for the object.
    __doc__: Contains the documentation string for the class.
    
    Common Methods:
    __str__(): Provides a "nice" string representation of the object, used by str() and print().
    __repr__(): Offers an "official" string representation, often used for debugging.
    __eq__(): Compares two objects for equality using the == operator.
    __ne__(): Checks for inequality (!=), opposite of __eq__().
    __hash__(): Returns the hash value of the object, used in hash-based collections.
    __new__(): Creates a new instance of the class.
    __init__(): Initializes the instance after it is created.
    
    These attributes and methods establish the basic behavior of all Python objects, with the ability to override them for custom behavior.
    '''

def type_casting_demo():
    pass


if __name__ == '__main__':
    '''
    python doesn't have a main entrypoint function. instead it executes the module given to python interpretor.
    before code execution some global variables and values are set. one of them is __name__.
    The __name__ variable holds the name of the module if imported to and called from other modules.
    If the mdule is directly executed by python interpreted __name__ is set to value "__main__"
    We could use this behaviour to create a main entrypoint for the moudule if it were to be executed as utility script.
    '''
    type_demo()


# todo: complete the hierarchy and casting demo