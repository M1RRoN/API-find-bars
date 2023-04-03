from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from api_bars.serializers import CreateUserSerializer
from establishments.models import Place


def index(request):
    return render(request, 'index.html')


class SearchView(ListView):
    model = Place
    template_name = 'search_results.html'
    context_object_name = 'places'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            results = Place.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            return results
        else:
            return Place.objects.none()


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)
