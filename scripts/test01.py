import pytest


class Test:
    def test01(self):
        print("test01被执行")

    def test02(self):
        print("test02被执行")

    def test03(self):
        print("test03被执行")

    def test04(self):
        print("test04被执行")


if __name__ == '__main__':
    pytest.main("-s test01.py")
