import pytest


class TestCalc:

    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_add, beg_end):
        r_add = None
        try:
            r_add = get_calc.add(get_add[0],get_add[1])
            if isinstance(r_add,float):
                r_add = round(r_add,2)
        except Exception as f:
            print(f)
            assert r_add == get_add[2]

    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_div, beg_end):
        try:
            r_div = get_calc.div(get_div[0],get_div[1])
            r_div = round(r_div,2)
            assert r_div == get_div[2]
        except ZeroDivisionError:
            print('注意：除数不可为0')

    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_sub, beg_end):
        r_sub = get_calc.sub(get_sub[0],get_sub[1])
        assert r_sub == get_sub[2]

    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, get_mul, beg_end):
        r_mul = get_calc.mul(get_mul[0],get_mul[1])
        assert r_mul == get_mul[2]

