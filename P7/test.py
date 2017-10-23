from inspect import getmembers, isfunction
import test.s as my_module

functions_list = [o for o in getmembers(my_module) if isfunction(o[1])]
print functions_list
