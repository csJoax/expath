# ExPath
CN | [EN](readme.md)

Extend Path，扩展路径库。该库在pathlib的基础上增添一些符号重载函数，以改进易用性。

## 安装
```
# method 1
git clone https://github.com/csJoax/expath.git
cd expath
pip install .

# method 2
pip install git+https://github.com/csJoax/expath.git
```

## 卸载
```
pip uninstall expath
```

## 使用
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
