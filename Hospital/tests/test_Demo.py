import pytest
from testapp.models import Hospital
from mixer.backend.django import mixer
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db


class TestHospitalAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_hospital_list(self):
        print("List method...............")

        student = mixer.blend(Hospital, name="Rk Hospital")

        student2 = mixer.blend(Hospital, name="Mv Hospital")

        url = reverse("hospital_list")

        # call the url
        response = self.client.get(url)

        # print(dir(response), "response")

        # aseertions
        # - json
        # - status
        assert response.json() != None

        assert len(response.json()) == 2

        assert response.status_code == 200

    def test_hospital_create(self):
        # data
        print("Create method...............")
        input_data = {
            "name": "BBC Hospital",
            "mobile": 8464055655

        }

        url = reverse("hospital")

        # call the url
        response = self.client.post(url, data=input_data)

        print(response.data)

        assert response.status_code == 201
        assert Hospital.objects.count() == 1

    def test_hospital_detail(self):
        # create a student
        print("Detail method...............")

        hospital = mixer.blend(Hospital, pk=1, name="RK Hospital",mobile=8464088937)
        print(Hospital.objects.last().pk, "qs")
        url = reverse("hospital_detail", kwargs={"pk": 1})
        response = self.client.get(url)

        # student2 = mixer.blend(Hospital, pk=2, name="Naomi")
        # url2 = reverse("student_detail_api", kwargs={"pk": 2})
        # response2 = self.client.get(url2)

        # assertions
        # - json
        # - status

        print(response.json(), "response json")

        assert response.json() != None
        assert response.status_code == 200
        assert response.json()["name"] == "RK Hospital"
        assert response.json()["mobile"] == 8464088937

        # assert response2.json()["first_name"] == "Naomi"
        # assert response2.json()["username"] == "naomi"

    def test_hospital_delete(self):
        # create a student
        print("Destroy method................")
        student = mixer.blend(Hospital, pk=1, name="RK Hospital", mobile=8464088937)
        assert Hospital.objects.count() == 1

        url = reverse("hospital_delete", kwargs={"pk": 1})
        response = self.client.delete(url)
        # assertions
        # - json
        # - status

        print(dir(response.json), "response json")
        print((response.status_code), "response json")

        assert response.status_code == 204

        assert Hospital.objects.count() == 0
