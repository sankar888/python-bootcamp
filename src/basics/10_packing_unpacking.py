'''
pacing and unpacking in python:
Packing: packing refers to pack different independent values to a container type and assign it to a single variable 
Unpacking: unpacking is the reverse of packing which expands the packed values and assigns it to independent variables
'''
from utils import m_header
from utils import f_header

def packing_demo():
    '''
    demonstrates the packing of values as container types
    '''
    # indenpendent values are packed as list
    l = [1,2,3]
    n1, n2, n3 = 100, 200, 300
    l1 = [n1, n2, n3]
    
    # usually tuple is used for packing values as tuple is immutable
    t1 = (1,2, n3)
    t2 = n1, n2, n3
    print(f'packing demo: type(t2): {type(t2)}, value of t2: {t2}')

    # we could pass multiple arguments to a functions using packing
    # * could be used to receive multiple parameters in a function as tuple
    def add(*tuple):
        total = 0
        for item in tuple:
            total += item
        return total
    
    print(f'add(1,2,3) = {add(1,2,3)}')
    print(f'add(1) = {add(1)}')
    print(f'add() = {add()}') # empty tuple

    # ** can be used to receive multiple keyed arguments as a map
    def set_attributes(**kvarg):
        print(f'packaging demo: type of kvarg: {type(kvarg)}')
        for key, val in kvarg.items():
            print(f'config: {key}={val}')
        else:
            print('attribute dict empty')

    set_attributes(name='yeman', age=101, sex='zombie')
    set_attributes()

def unpacking_demo():
    '''
    unpacking expands the iterable objects to individual objects
    * and ** can be used to unpack sequence and dict respectively
    '''
    id, age, salary = (1001, 24, '100k')
    print(f'unpacking demo: id = {id}, age = {age}, salary = {salary}')

    # we could unpack any sequence type not just tuples
    id, age, salary = [1001, 24, '100k']
    print(f'unpacking demo: id = {id}, age = {age}, salary = {salary}')

    # what if there is more values but not enougf variables. ValueError: too many values to unpack (expected 2)
    # id, age = (1001, 24, '100k')
    # print(f'unpacking demo: id = {id}, age = {age}')

    # what if there is more valriables but not enougf values. ValueError: too many values to unpack (expected 3)
    # id, age, salary = [1001, 24, '100k', 'London']
    # print(f'unpacking demo: id = {id}, age = {age}, salary = {salary}')

    # we could use * as a solution to the obove unpacking problem
    # the extra values will be packed in attrs
    id, age, *attrs = (1001, 24, '100k', 'London')
    print(f'unpacking demo: id = {id}, age = {age}, attrs = {attrs}')

    id, *attrs, place = (1001, 24, '100k', 'London')
    print(f'unpacking demo: id = {id}, attrs = {attrs}, place = {place}')

    *attrs, place = (1001, 24, '100k', 'London')
    print(f'unpacking demo: attrs = {attrs}, place = {place}')

if __name__ == '__main__':
    m_header('Packing and Unpacking in Python')
    f_header('packing basics', packing_demo)
    packing_demo()

    f_header('unpacking in python', unpacking_demo)
    unpacking_demo()
    