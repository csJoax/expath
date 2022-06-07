import os
from os import PathLike
from pathlib import Path, PurePath

# TODO: test
class XPath:
    pass

class XPath(Path):
    # 'a/b/c' + 'd/e' -> 'a/b/c/d/e'
    def __add__(self, other) -> XPath:
        return self.__truediv__(other)

    def __radd__(self, other) -> XPath:
        return self.__rtruediv__(other)

    # 'b/c' @ a/b/c' -> 'a'
    def __matmul__(self, other) -> XPath:
        return XPath(os.path.relpath(self, other))

    def __rmatmul__(self, other) -> XPath:
        return XPath(os.path.relpath(other, self))

    # 'a/b/c' + 'b/c' -> 'a'
    def __sub__(self, other) -> XPath:
        return XPath(os.path.relpath(other, self))

    def __rsub__(self, other) -> XPath:
        return XPath(os.path.relpath(self, other))

    # TODO: 'a/b/c' ^ 'a' -> 'b/c'
    # TODO: 'a/b/c'['a'] -> 'b/c'
    def __xor__(self, other) -> XPath:
        raise NotImplemented

    def __rxor__(self, other) -> XPath:
        raise NotImplemented

    # 'b/c' @ a/b/c' -> 'a'
    def __and__(self, other) -> XPath:
        return XPath(os.path.commonpath([self, other]))

    def __rand__(self, other) -> XPath:
        return XPath(os.path.commonpath([self, other]))
