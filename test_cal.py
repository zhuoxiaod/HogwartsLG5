import pytest
import yaml

from pythoncode.calculator import Calculator



class TestCalc:

    # def get_data(self):
    #     with open('/.calc.yml') as f:
    #         datas = yaml.safe_load(f)
    #         return datas
    def setup(self):
        print('\n开始计算')
    # def setup_class(self):
    #     print('\n开始计算')
        self.calc = Calculator()

    def teardown(self):
        print('\n计算结束')

    # def teardown_class(self):
    #     print('\n计算结束')


    @pytest.mark.parametrize("a,b,expect", [(4, 4, 8), (-5, -5, -10), (2000, 2000, 4000)])
    def test_add(self, a,b,expect):
        result = self.calc.add(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", [(4, 2, 2), (-5, -5, 0), (2000, 2000, 0)])
    def test_sub(self, a,b,expect):
        result = self.calc.sub(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", [(4, 4, 16), (-5, -5, 25), (45, 3, 135)])
    def test_mul(self, a,b,expect):
        result = self.calc.mul(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", [(4, 4, 1), (-5, -5, 1), (2000, 500, 4)])
    def test_div(self, a,b,expect):
        result = self.calc.div(a,b)
        assert result == expect