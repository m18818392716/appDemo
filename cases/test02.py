import pytest
"""
    生成pytest自带的测试报告;pytest -s ./cases/test02.py --html=./Reports/666.html
    
    pytest -s ./cases/test02.py --reruns 2 --alluredir=./result/xml
    pytest -s ./cases/test02.py --reruns 1 --alluredir=./result/xml
    pytest -s ./cases/test02.py --alluredir=./result/xml
    
    1、生成xml下的json文件：pytest -s ./cases/test02.py --alluredir=./result/xml
    2、生成html测试报告：allure generate ./result/xml -o report/allure_report --clean
"""

# test02.py
class Test(object):
    def test2(self, get_token):
        token = 'qeehfjejwjwjej11sss@22'
        print("【执行test02.py-Test类-test2用例,获取get_token：%s】" % get_token)
        assert get_token == token

    def test_print_name(name):
        print("Displaying name: %s" % name)
        print("Displaying name: {}".format(name))
        print(name)


if __name__ == "__main__":
    pytest.main(["-s", "test02.py", "test03.py", "--name abc"])
    # command_line = ["-s", "test02.py", "--alluredir=report"]
    # pytest.main(command_line)