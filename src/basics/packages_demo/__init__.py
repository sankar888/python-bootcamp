'''
Package is a higer level collection of modules or sub-packages.
A python can have have a __init__.py file at the root of the package to denote it as a pacakge, but it is optionnal from version 3.3
A python __init__.py file can have metadata about the package or code which should run when we import modules
A package can be imported as a whole or a specific module can be imported from package

we use . notation to denite multiple directory structure while importing
ex:
from a.b.c import module_d
import a.b.c.module_d as d

import a
# if we import whole package the functions can be accessed using a.b.c.module_d.function()
'''