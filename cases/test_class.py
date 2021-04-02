import pytest
'''
pytest中有两种跳过：
pytest.mark.skip(reason=“无条件跳过”)
pytest.mark.skipif(condition=表达式， reason=“跳过原因”)，当表达式为True的时候，才触发跳过。

'''

#在类下面实现依赖关系，第一种方式
class TestClass(object):

    @pytest.mark.dependency()
    # @pytest.mark.xfail(reason="deliberate fail")
    def test_a(self):
        print("方法1")
        assert True

    @pytest.mark.dependency()
    def test_b(self):
        print("方法2")
        assert False

    @pytest.mark.dependency(depends=["TestClass::test_a"])
    def test_c(self):
        print("方法3")

    @pytest.mark.dependency(depends=["TestClass::test_b"])
    def test_d(self):
        print("方法4")

    @pytest.mark.dependency(depends=["TestClass::test_b", "TestClass::test_c"])
    def test_e(self):
        print("方法5")

    # @pytest.mark.run(order=1)
    @pytest.mark.first
    def test_f(self):
        print("方法6")

    # @pytest.mark.run(order=2)
    @pytest.mark.second
    def test_f1(self):
        print("方法9")

    # @pytest.mark.run(order=-2)
    @pytest.mark.sencond_to_last
    @pytest.mark.ios
    def test_g(self):
        print("方法7")

    # @pytest.mark.run(order=-1)
    @pytest.mark.last
    @pytest.mark.android
    def test_h(self):
        print("方法8")

    def test_i(self):
        pytest.assume(3 == 3)
        pytest.assume(5 == 5)
        pytest.assume(4 == 4)

@pytest.mark.skip(reason='无条件跳过用例')
class TestCaseLogin:

    def test_login_01(self):
        print('test case -01')
        assert 1
    def test_login_02(self):
        print('test case -02')
        assert 1

class TestCaseReg():
    @pytest.mark.skipif(1<2, reason="有条件跳过")
    def test_reg_01(self):
        print('test case -01')
        assert 1

    @pytest.mark.skipif(1 == 2, reason="有条件跳过")
    def test_reg_02(self):
        print('test case -02')
        assert 1


if __name__ == "__main__":
    pytest.main(["-s", "test_class.py"])