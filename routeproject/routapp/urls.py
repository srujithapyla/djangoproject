from django.urls import path,include
from .views import *
from rest_framework.routers import SimpleRouter,DefaultRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

router=SimpleRouter()
router.register('reg',testroute)

schema_view = get_schema_view(
    openapi.Info(
        title="LifeEazy",
        default_version="1.0",
        name='openapi-schema',
    ),)

urlpatterns = [
    path('test/',include(router.urls)),
    path('swagger/' , schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
