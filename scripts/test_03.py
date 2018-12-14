import pytest


class Test:
    @pytest.mark.run(order=4)
    def test_delete(self):
        print("test_delete被执行")

    @pytest.mark.run(order=3)
    def test_get(self):
        print("test_get被执行")

    @pytest.mark.run(order=2)
    def test_put(self):
        print("test_put被执行")

    # @pytest.mark.run(order=1)
    # def test_post(self):
    #     print("test_post被执行")
    
    def test_01(self):
        print("test_01被执行")
        assert 0

if __name__ == '__main__':
    pytest.main("-s test03.py")