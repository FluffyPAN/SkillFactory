# Задание: написать положительные тесты для калькулятора
#
import pytest
from app.Calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_division_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_multiply_subtraction_correctly(self):
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_multiply_adding_correctly(self):
        assert self.calc.adding(self, 3, 2) == 5