from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework.generics import RetrieveAPIView

from .models import Place
from .serializers import PlaceSerializer
from rest_framework import viewsets


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'place_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['place'] = self.object
        return context
