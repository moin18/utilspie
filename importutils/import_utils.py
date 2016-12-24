"""
Utility functions for import related operations
"""

import sys


def delete_module(modname):
    """
    Delete module and sub-modules from `sys.module`
    """
    try:
        _ = sys.modules[modname]
    except KeyError:
        raise ValueError("Module not found in sys.modules: '{}'".format(modname))

    for module in list(sys.modules.keys()):
        if module and module.startswith(modname):
            del sys.modules[module]


def reload_module(module):
    """
    Reload the Python module
    """
    try:
        # For Python 2.x
        reload(module)
    except (ImportError, NameError):
        # For <= Python3.3:
        import imp
        imp.reload(module)
    except (ImportError, NameError):
        # For >= Python3.4
        import importlib
        importlib.reload(module)


def lazy_load_modules(*modules):
    """
    Decorator to load module to perform related operation for specific function
    and delete the  module from imports once the task is done. GC frees the memory
    related to module during clean-up.
    """
    def decorator(function):
        def wrapper(*args, **kwargs):

            module_dict = {}
            for module_string in modules:
                module = __import__(module_string)

                # Add `module` entry in `sys.modules`. After deleting the module
                # from `sys.modules` and re-importing the module don't update
                # the module entry in `sys.modules` dict
                sys.modules[module.__package__] = module
                reload_module(module)
                module_dict[module_string] = module

            func_response = function(*args, **kwargs)

            for module_string, module in module_dict.items():
                # delete idna module
                delete_module(module_string)
                del module  # delete reference to idna

            return func_response
        return wrapper
    return decorator
