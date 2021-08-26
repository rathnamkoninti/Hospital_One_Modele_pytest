import pytest
import pytest


@pytest.fixture(scope="session")
def setUp():
    print("before connect")
    yield
    print("after connect")


@pytest.fixture
def demo_add(x, y):
    return x + y
