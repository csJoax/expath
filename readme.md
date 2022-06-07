# ExPath
[CN](readme-cn.md) | EN

Extend Path. Contained some overloaded ops based on pathlib.

## install
```
# method 1
git clone https://github.com/csJoax/expath.git
cd expath
python ./setup.py install

# method 2
pip install git+https://github.com/csJoax/expath.git
```

## uninstall
```
pip uninstall expath
```

## usage
```python
from expath import Path

# to join:
# 'a/b/c' + 'd/e' -> 'a/b/c/d/e'
Path('a/b/c') + 'd/e'
# or
Path('a/b/c') / 'd/e'

# to solve the root
# 'b/c' @ 'a/b/c' -> 'a'
Path('b/c') @ 'a/b/c'

# to drop the tail
# 'a/b/c' - 'b/c' -> 'a'
Path('a/b/c') - 'd/e'

# to drop the hat
# 'a/b/c' ^ 'a' -> 'b/c'
Path('a/b/c') ^ 'b/c'

# to compute the common path
# 'a/b/c' & a/b/d' -> 'a/b/'
Path('a/b/c') & 'a/b/d'
```
