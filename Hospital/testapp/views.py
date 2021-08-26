from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework import status, permissions, authentication

from rest_framework.views import APIView

from rest_framework.response import Response

from .serializers import HospitalSerializer
from testapp.models import Hospital



@api_view(['GET','POST'])

def hospital_get_post(request):
    serializers = HospitalSerializer(data=request.data)

    if request.method == 'GET':
        hospital = Hospital.objects.all()
        serializers = HospitalSerializer(hospital,many=True)
        return Response(serializers.data)

    # elif(request.method == 'POST'):
    #     serializers = HospitalSerializer(data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data,status=status.HTTP_201_CREATED)
    #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)











class HospitalListAPIView(ListAPIView):
    serializer_class = HospitalSerializer
    model = Hospital
    queryset = Hospital.objects.all()


class HospitalCreateAPIView(CreateAPIView):
    serializer_class = HospitalSerializer
    model = Hospital
    queryset = Hospital.objects.all()

class HospitalDetailAPIView(RetrieveAPIView):
    serializer_class = HospitalSerializer
    model = Hospital
    queryset = Hospital.objects.all()

class HospitalDestroyAPIView(DestroyAPIView):
    serializer_class = HospitalSerializer
    model = Hospital
    queryset = Hospital.objects.all()