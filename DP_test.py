from fib import fiban
from ball import bounce
from unittest import TestCase
from unittest.mock import Mock
from counting import tabl
class Test_1():
    def test_1(TestCase):
        assert fiban(0) == None
    def test_2(TestCase):
        assert fiban(1) == 1
    def test_3(TestCase):
        assert fiban(5) == 5
    def test_4(TestCase):
        assert fiban(30) == 832040 
class Test_2():
    def test_1(TestCase):
        assert bounce([]) == None
    def test_2(TestCase):
        assert bounce([6], 2, 3) == 6
    def test_3(TestCase):
        assert bounce([2, 5, 56, 12, 1, 11], 2, 3) == 69
    def test_4(TestCase):
        assert bounce([11, 13, 9, 4, 3, 0, 4, 1, 14, 7, 1, 10, 14, 15, 0, 14, 11, 12, 10, 8], 2, 3) == 100
class Test_3():
    def test_1(TestCase):
        assert tabl([[]]) == None
    def test_2(TestCase):
        assert tabl([[6], [15,12]]) == 33
    def test_3(TestCase):
        assert tabl([[1, 3, 56, 12],[57, 14],[2]]) == 72
    def test_4(TestCase):
        assert tabl([[31],[54]]) == 85
    def test_5(TestCase):
        assert tabl([[31],[54]]) == 85
    def test_6(TestCase):
        assert tabl([[  25, 12, 45, 2, 24, 9, 8, 25], [7, 25, 56, 1, 5, 7, 8, 14], [12, 33, 4, 24, 14, 8, 4, 6], [36, 12, 32, 21, 33, 25, 5, 24], [25, 26, 18, 24, 19, 6, 9, 15]]) == 285
