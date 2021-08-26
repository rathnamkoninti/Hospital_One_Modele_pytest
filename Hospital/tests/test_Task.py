import pytest
from django.test import Client
from testapp.models import Hospital
from mixer.backend.django import mixer
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from django import urls

# 1. Test cases for whether the view is rendering properly or not.
# 4. How can we use cases for multiple test cases?
pytestmark = pytest.mark.django_db
@pytest.mark.parametrize('param',[('hospital_list'),('hospital_get_post')])
def test_render_views(client,param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200


# 2. Test with URL endpoints
class TestHospitalAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        yield

    def test_hospital_list(self):
        url = reverse("hospital_list")
        response = self.client.get(url)
        print(response)
        assert response.status_code == 200

    def test_endpoint(self):
        base='http://127.0.0.1:8000/hospital'
        endpoint = base + "/list"
        resp = self.client.get(endpoint)
        print(resp)
        assert resp.status_code ==200

    def test_hospital_create(self):
        # data
        print("Create method...............")
        input_data = {"name": "BBC Hospital","mobile": "8464055655"}

        url = reverse("hospital")
        # call the url
        response = self.client.post(url, data=input_data)

        print(response.data)
        assert response.status_code == 201
        assert Hospital.objects.count() == 1

#5. How can we pass arguments to the test cases?


def add(a,b):
    return a+b

@pytest.mark.parametrize("a,b,c",[(1,2,3),("a","b","ab"),([1,2],[3],[1,2,3])],ids=["num","str","list"])
def test_all(a,b,c):
    assert add(a,b) == c

#6. How can skip that particular test case?

@pytest.mark.skip(reason="just for checking purpose.")
def test_add_num(self):
    print("skip test")

#7. How can we use fixtures in a test case?
""""
@pytest.fixture

"""

"""
8. How to use the markers?

By using the pytest.mark helper you can easily set metadata on your test functions.
ex: @pytest.mark.skip
"""


"""
9.Where will we configure the pytest configuration?

we can configure the pytest configuration in pytest.ini file
	
[pytest]
DJANGO_SETTINGS_MODULE=Hospital.settings
python_files = tests.py test_*.py *_tests.py

"""