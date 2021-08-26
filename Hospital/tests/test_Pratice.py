import sys

import pytest

from tests.sample import add
class TestDemo():
    @pytest.mark.promo
    def test_add(self):
        assert add(1, 2) == 3

    @pytest.mark.skip(reason="just for checking purpose.")
    def test_add_num(self):
        assert add(1,2) == 3

    @pytest.mark.skipif(sys.version_info > (3,7),reason="skip it") #if i pass (3,9) it will pass
    def test_add_str(self):
        assert add("a","b") == "ab"

    @pytest.mark.xfail(sys.platform == "win32", reason="Don't run on windows")
    def test_add_list(self):
        assert add([1],[2]) ==[1,2]
        raise Exception()

    @pytest.mark.parametrize("a,b,c",[(1,2,3),("a","b","ab"),([1,2],[3],[1,2,3])],ids=["num","str","list"])
    def test_all(self,a,b,c):
        assert add(a,b) == c
#******************************************************

@pytest.fixture(params=['apple','banana','orange'])
def fruit(request):
    return request.param
@pytest.mark.fixture
def test_fruit(fruit):
    print(f"fruit")




# @pytest.mark.usefixtures("add")
def test_ad(setUp):
    print("test add....")
def test_add2(setUp):
    print("test Add2")
# @pytest.fixture
def test_adding(demo_add):
    print("fixture name:",demo_add)
    assert demo_add(2, 3) == 5
