import pytest


class Test_ABC:
    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    def test_a(self):
        print("------->test_a")
        assert 1

    @pytest.mark.skipif()
    def test_b(self):
        print()