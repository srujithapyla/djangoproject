from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication

# Create your views here.

class smpleviewset(viewsets.ModelViewSet):
    serializer_class = sampleserializers
    queryset = routemodel1.objects.all()
    lookup_field = 'id'
