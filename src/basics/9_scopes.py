'''
scopes and namespaces:
    In Python, scopes and namespaces are closely related concepts but serve different roles:
1. Scope
Definition: Scope refers to the region of the code where a variable or name is accessible.

Types of Scopes in Python:
Local: Inside a function or method.
Enclosing: In an outer function, when functions are nested.
Global: At the top level of a module or script.
Built-in: Names provided by Python itself (like print, len, etc.).
Variables are only accessible within their defined scope, and once outside, they are inaccessible.

2. Namespace
Definition: A namespace is a mapping that holds names (identifiers) as keys and objects (values) as values.

Types of Namespaces:
Local: Holds names defined within a function.
Global: Holds names at the module level.
Built-in: Contains Python's built-in functions and exceptions.

Namespaces exist as long as the scope they belong to; local namespaces are destroyed after a function exits, while global and built-in namespaces persist longer.
'''

# python namespaces are references to list of names which are visible in current namespace
# The functions globals(), locals() and dir(__builtins__) will return a dict object with valid names in the respective scope
print(f'globals namespace names: {globals()}')
print(f'local namespace names: {locals()}')
print(f'gloabls() == locals() as we are in global scope the local namesace is same as gloabl namespace: {(locals() == globals())}')

# Namespace demo
def outerFunction():
    '''
        Every function will create a new namespace of its own. this function demos it
    '''
    print(f'locals() = {locals()}')
    print(f'gloabls() != locals() as the function will create a new scope: {(locals() != globals())}')
    x = 10
    print(f'after declaring x=10 locals() = {locals()}')
    def innerFunction():
        print(f'scope inside innerFunction, a function will create a new scope: locals() = {locals()}')
    innerFunction()

outerFunction()

# Scopes
print(f'the print() function is available in builtin scope which could be used anywhere without import. "print" in dir(__builtins__) = {"print" in dir(__builtins__)}')

# var a is available in global namespace of this module. which is accessible to enclosing namespaces within this module.
# if imported it is accessible in other modules too.
a = 10

def enclosingFunction1():
    # a is available here, unless it is shadowed by another variable in this namespace
    print(f'scope demo: value of a is {a}')
    def enclosingFunction2():
        print(f'scope demo: value of a in inner function {a}')
    enclosingFunction2()

enclosingFunction1()

# global value is overriden
def enclosingFunction1():
    a = 20
    print(f'scope demo override global: value of a is {a}')
    def enclosingFunction2():
        print(f'scope demo override global: value of a in inner function {a}')
    enclosingFunction2()

enclosingFunction1()

# each function will have a enclosing namespace
# the names in the enclosing namespace is accessible within the inner namespace
def enclosingFunction1():
    a = 20
    print(f'scope demo enclosing: value of a is {a}')
    def enclosingFunction2():
        a = 30
        print(f'scope demo enclosing override: value of a in inner function {a}')
    enclosingFunction2()

enclosingFunction1()

# each function will have a enclosing namespace
# the names in the enclosing namespace is accessible within the inner namespace
a = 1
def enclosingFunction1():
    # uncommenting the below line will throw an error.
    # in the function scope variable a is not available, the enclosing scoped varibale can only be accessed but could not be modified
    # a = a + 1
    print(a)
    print(f'scope demo enclosing: value of a is {a}')

enclosingFunction1()

def enclosingFunction1():
    c = 100
    def enclosingFunction2():
        # uncommenting the below line with throw error
        # c = c + 1
        print(f'scope demo enclosing: value of c is {c}')
    enclosingFunction2()

enclosingFunction1()