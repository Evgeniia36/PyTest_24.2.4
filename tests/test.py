import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division(self):
        assert self.calc.division(self,8, 4) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_subtraction(self):
        assert self.calc.subtraction(self,6, 5) == 1

    def test_adding(self):
        assert self.calc.adding(self, 2, 3) == 5

    def teardown(self):
        print('Teardown')
