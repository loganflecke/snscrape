# import pkgutil


# __all__ = []


# def _import_modules():
# 	prefixLen = len(__name__) + 1
# 	for importer, moduleName, isPkg in pkgutil.iter_modules(__path__, prefix = f'{__name__}.'):
# 		assert not isPkg
# 		moduleNameWithoutPrefix = moduleName[prefixLen:]
# 		__all__.append(moduleNameWithoutPrefix)
# 		module = importer.find_module(moduleName).load_module(moduleName)
# 		globals()[moduleNameWithoutPrefix] = module


# _import_modules()

import pkgutil
import importlib

all = [] # Define all here

def _import_modules():
	prefixLen = len(name) + 1
	for _, moduleName, _ in pkgutil.iter_modules(path, prefix=f'{name}.'):
	moduleNameWithoutPrefix = moduleName[prefixLen:]
	all.append(moduleNameWithoutPrefix)
	module = importlib.import_module(moduleName)
	globals()[moduleNameWithoutPrefix] = module
_import_modules()

