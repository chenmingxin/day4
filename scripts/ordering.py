import pytest


class Test:
    @pytest.mark.run(order=4)
    def test_1(self):
        print("test_1被执行")

    @pytest.mark.run(order=3)
    def test_2(self):
        print("test_2被执行")

    @pytest.mark.run(order=2)
    def test_3(self):
        print("test_3被执行")

    @pytest.mark.run(order=1)
    def test_4(self):
        print("test_4被执行")

if __name__ == '__main__':
    pytest.main("-s ordering.py")