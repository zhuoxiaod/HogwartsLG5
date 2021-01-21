import pytest
import yaml
import os

from pythoncode.calculator import Calculator

yaml_file_path = os.path.dirname(__file__) + '/calc.yml'
with open('./calc.yml') as f:
    datas = yaml.safe_load(f)
    datas_add = datas['add']
    datas_mul = datas['mul']
    datas_sub = datas['sub']
    datas_div = datas['div']
    datas_ids = datas['myids']

#获取计算实例
@pytest.fixture(scope='module')
def get_calc():
    print('获取计算实例')
    calc =  Calculator()
    return calc

@pytest.fixture(scope='function')
def beg_end():
    print('开始计算')
    yield
    print('结束计算')

@pytest.fixture(params=datas_add,ids=datas_ids)
def get_add(request):
    add = request.param
    return add


@pytest.fixture(params=datas_sub,ids=datas_ids)
def get_sub(request):
    sub = request.param
    return sub

@pytest.fixture(params=datas_mul,ids=datas_ids)
def get_mul(request):
    mul = request.param
    return mul

@pytest.fixture(params=datas_div,ids=datas_ids)
def get_div(request):
    div = request.param
    return div

