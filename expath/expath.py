import os
from pathlib import Path


# 'a/b/c' + 'd/e' -> 'a/b/c/d/e'
def __add__(self, other) -> Path:
    return self.__truediv__(other)

def __radd__(self, other) -> Path:
    return self.__rtruediv__(other)


# 'b/c' @ a/b/c' -> 'a'
def __matmul__(self, other) -> Path:
    return Path(os.path.relpath(self, other))

def __rmatmul__(self, other) -> Path:
    return Path(os.path.relpath(other, self))


# 'a/b/c' + 'b/c' -> 'a'
def __sub__(self, other) -> Path:
    return Path(os.path.relpath(other, self))

def __rsub__(self, other) -> Path:
    return Path(os.path.relpath(self, other))


# TODO: 'a/b/c' ^ 'a' -> 'b/c'
def __xor__(self, other) -> Path:
    raise NotImplemented

def __rxor__(self, other) -> Path:
    raise NotImplemented


# 'a/b/c' & a/b/d' -> 'a/b/'
def __and__(self, other) -> Path:
    return Path(os.path.commonpath([self, other]))

def __rand__(self, other) -> Path:
    return Path(os.path.commonpath([self, other]))


__extra_attr__ = [
    '__add__', 
    '__radd__', 
    '__matmul__', 
    '__rmatmul__', 
    '__sub__', 
    '__rsub__', 
    # '__xor__', 
    # '__rxor__', 
    '__and__', 
    '__rand__', 
]

def set_attr():
    for attr in __extra_attr__:
        if hasattr(Path, attr):
            print('warn: attr already existed:', attr)
        setattr(Path, attr, eval(attr))
    

def unset_attr():
    for attr in __extra_attr__:
        if hasattr(Path, attr):
            delattr(Path, attr)
