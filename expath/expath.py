import os
from pathlib import Path


# 'a/b/c' + 'd/e' -> 'a/b/c/d/e'
def __add__(self, other) -> Path:
    return self.__truediv__(other)

# 'a/b/c' + 'd/e' -> 'a/b/c/d/e'
def __radd__(self, other) -> Path:
    return self.__rtruediv__(other)


class PathError(ValueError):
    pass


# 'b/c' @ 'a/b/c' -> 'a'
def at(self, other) -> Path:
    self = Path(self)
    other = Path(other)
    for _s, _o in zip(self.parts[::-1], other.parts[::-1]):
        if _s != _o:
            raise PathError('no such path about `at`', self, other)
    return Path(*other.parts[:-len(self.parts)])

# 'b/c' @ 'a/b/c' -> 'a'
def __matmul__(self, other) -> Path:
    return at(self, other)

# 'b/c' @ 'a/b/c' -> 'a'
def __rmatmul__(self, other) -> Path:
    return at(other, self)

# 'a/b/c' - 'b/c' -> 'a'
def __sub__(self:str, other) -> Path:
    return at(other, self)

# 'a/b/c' - 'b/c' -> 'a'
def __rsub__(self, other) -> Path:
    return at(self, other)


# 'a/b/c' ^ 'a' -> 'b/c'
def __xor__(self, other) -> Path:
    return Path(os.path.relpath(self, other))

# 'a/b/c' ^ 'a' -> 'b/c'
def __rxor__(self, other) -> Path:
    return Path(os.path.relpath(other, self))


# 'a/b/c' & a/b/d' -> 'a/b/'
def __and__(self, other) -> Path:
    return Path(os.path.commonpath([self, other]))

# 'a/b/c' & a/b/d' -> 'a/b/'
def __rand__(self, other) -> Path:
    return Path(os.path.commonpath([self, other]))


__extra_attr__ = [
    '__add__', 
    '__radd__', 
    'at', 
    '__matmul__', 
    '__rmatmul__', 
    '__sub__', 
    '__rsub__', 
    '__xor__', 
    '__rxor__', 
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
