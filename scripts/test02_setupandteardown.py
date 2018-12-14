import pytest


class Test:
    def setup_class(self):
        print("setup_class被执行")

    def teardown_class(self):
        print("teardown_class被执行")

    def setup(self):
        print("setup被执行")

    def teardown(self):
        print("teardown被执行")

    def test01(self):
        print("test01被执行")

    def test02(self):
        print("test02被执行")


if __name__ == '__main__':
    pytest.main("-s test_*.py")
