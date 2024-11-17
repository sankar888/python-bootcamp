'''
utils.py

This module cntains the common utilities function used in all modules
'''
import types

def m_header(header: str):
    print(f"\n{10 * '#'} {header} {10 * '#'}")

def f_header(header: str, fn: types.FunctionType):
    print("\n")
    print(f"{3 * '*'} {header} {3 * '*'}:")
    if fn.__doc__ is not None:
        print(fn.__doc__)