import pytest
class TestDemo():

    @pytest.mark.ios
    def test_g(self):
        print("方法7")

    @pytest.mark.android
    def test_t(self):
        print("方法8")

@pytest.mark.skip(reason='无条件跳过用例')
class TestCaseLogin:

    def test_login_01(self):
        print('test case -01')

    def test_login_02(self):
        print('test case -02')

class TestCaseReg():
    @pytest.mark.skipif(1<2, reason="有条件跳过")
    def test_reg_01(self):
        print('test case -03')

    @pytest.mark.skipif(1 == 2, reason="有条件跳过")
    def test_reg_02(self):
        print('test case -04')

if __name__ == "__main__":
    pytest.main(["-s", "test04.py"])
    # command_line = ["-s", "test02.py", "--alluredir=report"]
    # pytest.main(command_line)