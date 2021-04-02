import pytest

"""
一、’conftest特点：

1、可以跨.py文件调用，有多个.py文件调用时，可让conftest.py只调用了一次fixture，或调用多次fixture

2、conftest.py与运行的用例要在同一个pakage下，并且有__init__.py文件

3、不需要import导入 conftest.py，pytest用例会自动识别该文件，放到项目的根目录下就可以全局目录调用了，如果放到某个package下，那就在改package内有效，可有多个conftest.py

4、conftest.py配置脚本名称是固定的，不能改名称

5、conftest.py文件不能被其他文件导入

6、所有同目录测试文件运行前都会执行conftest.py文件

二、’conftest用法：

conftest文件实际应用需要结合fixture来使用，fixture中参数scope也适用conftest中fixture的特性，这里再说明一下


conftest文件实际应用需要结合fixture来使用，fixture中参数scope也适用conftest中fixture的特性，这里再说明一下

1、fixture源码详解

fixture（scope='function'，params=None，autouse=False，ids=None，name=None）：
fixture里面有个scope参数可以控制fixture的作用范围，scope：有四个级别参数"function"（默认），"class"，"module"，"session

params：一个可选的参数列表，它将导致多个参数调用fixture功能和所有测试使用它。
autouse：如果True，则为所有测试激活fixture func可以看到它。如果为False则显示需要参考来激活fixture
ids：每个字符串id的列表，每个字符串对应于params这样他们就是测试ID的一部分。如果没有提供ID它们将从params自动生成
name：fixture的名称。这默认为装饰函数的名称。如果fixture在定义它的统一模块中使用，夹具的功能名称将被请求夹具的功能arg遮蔽，解决这个问题的一种方法时将装饰函数命令"fixture_<fixturename>"然后使用"@pytest.fixture（name='<fixturename>'）"。

2、fixture的作用范围

fixture里面有个scope参数可以控制fixture的作用范围：session>module>class>function

-function：每一个函数或方法都会调用

-class：每一个类调用一次，一个类中可以有多个方法

-module：每一个.py文件调用一次，该文件内又有多个function和class

-session：是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module

function默认模式@pytest.fixture(scope='function')或 @pytest.fixture()

3、conftest结合fixture的使用

conftest中fixture的scope参数为session，所有测试.py文件执行前执行一次

conftest中fixture的scope参数为module，每一个测试.py文件执行前都会执行一次conftest文件中的fixture

conftest中fixture的scope参数为class，每一个测试文件中的测试类执行前都会执行一次conftest文件中的fixture

conftest中fixture的scope参数为function，所有文件的测试用例执行前都会执行一次conftest文件中的fixture

三、conftest应用场景

1、每个接口需共用到的token

2、每个接口需共用到的测试用例数据

3、每个接口需共用到的配置信息
————————————————
原文链接：https://blog.csdn.net/qq_36502272/article/details/102975467
"""

# conftest.py
# 多个.py文件只调用1次fixture
@pytest.fixture(scope='session')
def get_token():
    token = 'qeehfjejwjwjej11sss@22'
    print('获取到token:%s' % token)
    return token

# 多个.py文件只调用多次fixtur
# @pytest.fixture(scope='session')
# def get_token():
#     token = 'qeehfjejwjwjej11sss@33'
#     print('获取到token:%s' % token)


def pytest_addoption(parser):
    parser.addoption("--name", action="store", default="default name")

# @pytest.fixture
# def name(request):
#     return request.config.getoption("--name")

def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.name
    if 'name' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("name", [option_value])
