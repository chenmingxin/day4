import pytest

def get_data():

    return [("张三","男",24,"1班"),("李四","男",20,"2班"),("王五","男",22,"3班"),("赵六","男",26,"4班")]


class Test_abc:
    def test_1(self):
        print("test_1被执行")
    def test_2(self):
        print("test_2被执行")


    @pytest.mark.parametrize("name,sex,age,bj",get_data())
    def test_3(self,name,sex,age,bj):
        # print("test_3被执行")
        print(name,sex,age,bj)

if __name__ == '__main__':
    pytest.main("-s pram.py")