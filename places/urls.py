from django.conf.urls import url, include
from django.urls import path, re_path
from rest_framework import routers

from places.views import  PlacesViewSet, RatesViewSet

router = routers.DefaultRouter()
router.register('places', PlacesViewSet)
router.register('rates', RatesViewSet)
app_name = 'places'

urlpatterns =[
    re_path('^', include(router.urls)),
    ]

