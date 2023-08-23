from django.shortcuts import render
from rest_framework import viewsets
from .serializers import testserializer
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
# Create your views here.


class testroute(viewsets.ModelViewSet):
    serializer_class = testserializer
    queryset = routemodel.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'