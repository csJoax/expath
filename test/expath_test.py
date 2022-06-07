# %%
import sys
sys.path.append('.')
import unittest
from expath import Path
# %%

class Tester(unittest.TestCase):
    def test__add__(self):
        # %% 
        # 'a/b/c' + 'd/e' -> 'a/b/c/d/e'
        res1 = Path('a/b/c') + 'd/e'
        res2 = 'a/b/c' + Path('d/e')
        assert res1 == res2 == Path('a/b/c/d/e')
        # %%

    def test_at(self):
        # %% 
        res1 = Path('b/c').at('a/b/c')
        print(res1)
        assert res1 == Path('a/')

        a = Path('d/c')
        from expath import PathError
        self.assertRaises(PathError, a.at, 'a/b/c')
        # %%

    def test__matmul__(self):
        # %% 
        # 'b/c' @ 'a/b/c' -> 'a'
        res1 = Path('b/c') @ 'a/b/c'
        res2 = 'b/c' @ Path('a/b/c')
        assert res1 == res2 == Path('a')
        # %%

    def test__sub__(self):
        # %% 
        # 'a/b/c' - 'b/c' -> 'a'
        res1 = Path('a/b/c') - 'b/c'
        res2 = 'a/b/c' - Path('b/c')
        assert res1 == res2 == Path('a')
        # %%

    def test__and__(self):
        # %% 
        # 'a/b/c' & a/b/d' -> 'a/b/'
        res1 = Path('a/b/c') & 'a/b/d'
        res2 = 'a/b/c' & Path('a/b/d')
        assert res1 == res2 == Path('a/b')
        # %%

    def test__xor__(self):
        # %% 
        # 'a/b/c' ^ 'a' -> 'b/c'
        res1 = Path('a/b/c') ^ 'a'
        res2 = 'a/b/c' ^ Path('a')
        print(res1)
        print(res2)
        assert res1 == res2 == Path('b/c')
        # %%

if __name__ == '__main__':
    unittest.main()
