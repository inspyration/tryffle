from django.urls import path, include
from rest_framework.routers import DefaultRouter

from lists.views import basic_list, real_list, SebViewSet, data_source


router = DefaultRouter()
router.register(r'flat_data', SebViewSet)


urlpatterns = [
    path('basic/', basic_list, name="basic_list"),
    path('real/', real_list, name="basic_list"),
    path('data/', data_source, name="data_source"),
    path('', include(router.urls)),
]
