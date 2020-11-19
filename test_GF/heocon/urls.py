from django.urls import include, path
from rest_framework import routers
from . import views
from .views import AgLitterViewSet
from django.conf.urls import url
router = routers.DefaultRouter()
router.register(r'aglitter', AgLitterViewSet, basename='aglitter/history')
# router.register(r'agParity', views.AgParityViewSet)
# router.register(r'herd', views.HerdViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # url(r'^test$', views.tutorial_list),
    # url(r'^test/(?P<pk>[0-9]+)$', views.tutorial_detail),
]
