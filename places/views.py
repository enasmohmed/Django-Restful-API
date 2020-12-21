from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from places.models import Place, Rate
from places.serializer import PlaceSerializer, RateSerializer




# مخطط بيانات للمكان التاريخي 
class PlacesViewSet(ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer



# مخطط بيانات تقييمات المكان التاريخي 
class RatesViewSet(ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Rate.objects.all()
    serializer_class = RateSerializer







class RatesViewSet(ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


