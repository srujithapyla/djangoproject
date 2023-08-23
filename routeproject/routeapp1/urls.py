from django.urls import path,include
from rest_framework.routers import SimpleRouter,DefaultRouter
from .views import *

router=SimpleRouter()
router.register('test1',smpleviewset)


urlpatterns = [
    path('test/',include(router.urls)),
    path('auth/',include('rest_framework.urls')),

]