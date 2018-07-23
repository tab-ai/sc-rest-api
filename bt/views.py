# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.urls import reverse
from .models import Band
# from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .serializers import BandSerializer

# ViewSets define the view behavior.
class BandViewSet(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
