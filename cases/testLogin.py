import pytest
import allure

'''
    1、命令行执行：pytest -v -m "ios" ，则只会运行标记为ios的用例
    2、命令行执行：pytest -v -m "not ios" ，则会运行没有标记ios的用例

'''

@allure.feature("测试TestLogin")
class TestLogin(object):

    # @@allure.MASTER_HELPER.step("定义被测函数")
    @allure.step("定义被测函数")
    @pytest.mark.dependence(name="test_001")
    @pytest.mark.run(order=1)
    def test_001(self):
        print(111)
        return 3

    @pytest.mark.dependence(depends=["test_001"])
    def test_002(self):
        print(222)
        print("{} + {}的计算结果是：{}".format(self.test_001, 4, self.test_001()+4))

    # @allure.MASTER_HELPER.story("被测场景")
    @allure.story("被测场景")
    # @allure.MASTER_HELPER.severity("blocker")
    @allure.severity("blocker")
    # @allure.MASTER_HELPER.step("断言结果")
    @allure.step("断言结果")
    @pytest.mark.dependence(name="test_004")
    def test_004(self):
        assert 1==0

    @pytest.mark.dependence(depends=["test_004"])
    def test_005(self):
        print(11111111111111)

    @pytest.mark.ios
    def test_c(self):
        print("iOS 测试用例")

    @pytest.mark.android
    def test_d(self):
        print("android 测试用例")


if __name__ == "__main__":
    pytest.main(["-s", "testLogin.py"])
